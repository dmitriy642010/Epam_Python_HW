"""
Задача спарсить информацию о компаниях, находящихся в индексе S&P 500 с данного сайта:
https://markets.businessinsider.com/index/components/s&p_500

Для каждой компании собрать следующую информацию:

    Текущая стоимость в рублях (конвертацию производить по текущему курсу, взятому с сайта центробанка РФ)
    Код компании (справа от названия компании на странице компании)
    P/E компании (информация находится справа от графика на странице компании)
    Годовой рост/падение компании в процентах (основная таблица)
    Высчитать какую прибыль принесли бы акции компании (в процентах), если бы они были куплены на уровне 52 Week Low и
    проданы на уровне 52 Week High (справа от графика на странице компании)
"""


import asyncio
import json
import re
from heapq import nlargest
from typing import Dict, List

import aiohttp

from bs4 import BeautifulSoup


async def get_page(url: str) -> str:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()


async def get_exchange_rate() -> float:

    url_cbr = "http://www.cbr.ru/scripts/XML_daily.asp"
    page = await get_page(url_cbr)
    page = BeautifulSoup(page, "lxml")
    exchange_rate = page.find(id="R01235").find_next("value").get_text()
    return float(exchange_rate.replace(",", "."))


async def get_companies_from_page(path: str, page: int) -> List:

    start_page = path + "index/components/s&p_500"
    base_url = start_page + " ?p={}"
    companies = []
    page = BeautifulSoup(await get_page(base_url.format(page)), "lxml")
    table = page.find(class_="table table-small")

    for row in table.find_all("tr")[1:]:
        name = row.find("a")["title"]
        href = row.find("a")["href"]
        growth = row.find_all("td")[9].text.split()[1]
        companies.append([name, href, float(growth[:-1])])
    return companies


async def page_count(path: str) -> int:
    """Return number of pages with tables."""
    start_page = path + "index/components/s&p_500"
    page = await get_page(start_page)
    page = BeautifulSoup(page, "lxml")
    pages = page.find("div", class_="finando_paging").find_all("a")
    return int(pages[-1].text)


async def get_companies_from_all_pages() -> List[List]:

    path = "https://markets.businessinsider.com/"
    pages = await page_count(path)
    tasks = [get_companies_from_page(path, i) for i in range(1, pages + 1)]
    return await asyncio.gather(*tasks)


async def get_company_info(company: List, exchange_rate: float) -> Dict:

    start_page = "https://markets.businessinsider.com"
    base_url = start_page + company[1]
    page = BeautifulSoup(await get_page(base_url), "lxml")
    table = page.find("span", class_="price-section__category")
    code = table.find("span").text[2:]
    table = page.find(class_="price-section__current-value")
    price = float(table.text.replace(",", "")) * exchange_rate
    script = page.find("div", class_="snapshot").find("script")
    week_low = float(re.findall(r"low52weeks: (\d*.\d*),", script.string)[0])
    week_high = float(re.findall(r"high52weeks: (\d*.\d*),", script.string)[0])
    try:
        pe = float(
            page.find("div", class_="snapshot")
            .find_all(class_="snapshot__data-item")[6]
            .text.split()[0]
        )
    except ValueError:
        pe = -1
    return {
        "name": company[0],
        "href": company[1],
        "growth": company[2],
        "code": code,
        "P/E": pe,
        "price": round(price, 2),
        "potential profit": round((week_high - week_low) / week_low, 2),
    }


def save_to_json(filename: str, value_name: str, data: List[Dict]) -> None:
    with open(filename + ".json", "w") as file:
        top_10 = [
            {
                "name": data[i]["name"],
                "code": data[i]["code"],
                f"{value_name}": data[i][value_name],
            }
            for i in range(10)
        ]
        json.dump(top_10, file, indent=4)


async def get_all_information() -> List[Dict]:

    companies = await get_companies_from_all_pages()
    exchange_rate = await get_exchange_rate()
    tasks = []
    for page in companies:
        for company in page:
            tasks.append(get_company_info(company, exchange_rate))
    return await asyncio.gather(*tasks)


def main() -> None:

    companies_info = asyncio.run(get_all_information())
    save_to_json(
        "top_growth",
        "growth",
        nlargest(10, companies_info, key=lambda x: x["growth"]),
    )
    save_to_json(
        "top_PE",
        "P/E",
        nlargest(10, companies_info, key=lambda x: x["P/E"]),
    )
    save_to_json(
        "top_price",
        "price",
        nlargest(10, companies_info, key=lambda x: x["price"]),
    )
    param = "potential profit"
    save_to_json(
        "top_potential_profit",
        param,
        nlargest(10, companies_info, key=lambda x: x[param]),
    )
