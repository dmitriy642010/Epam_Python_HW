import asynctest


from Epam_training_HW.hw.Task_10 import hw_10_task_1
from Epam_training_HW.hw.Task_10.hw_10_task_1 import (
    get_companies_from_page,
    get_company_info,
    get_page,
)

import pytest


@pytest.fixture()
def mock_get_page(monkeypatch):
    def fake_page(url):
        with open("test/MMM.html") as file:
            return file.read()

    fake_get_page = asynctest.CoroutineMock(get_page, side_effect=fake_page)
    monkeypatch.setattr(hw_10_task_1, "get_page", fake_get_page)
    return fake_get_page


@pytest.mark.asyncio
async def test_get_company_info(mock_get_page):
    res = {
        "name": "3M",
        "href": "/stocks/mmm-stock",
        "growth": -1.52,
        "code": "MMM",
        "P/E": 20.12,
        "price": 12860.75,
        "potential profit": 0.6,
    }
    actual_res = await get_company_info(["3M", "/stocks/mmm-stock", -1.52], 70)
    assert res["name"] == actual_res["name"]
    assert res["href"] == actual_res["href"]
    assert res["growth"] == actual_res["growth"]
    assert res["P/E"] == actual_res["P/E"]
    assert res["potential profit"] == actual_res["potential profit"]


@pytest.fixture()
def mock_get_start_page(monkeypatch):
    def fake_page(url):
        with open("test/start_page.html") as file:
            return file.read()

    fake_get_page = asynctest.CoroutineMock(get_page, side_effect=fake_page)
    monkeypatch.setattr(hw_10_task_1, "get_page", fake_get_page)
    return fake_get_page


@pytest.mark.asyncio
async def test_get_companies_from_page(mock_get_start_page):

    actual_res = await get_companies_from_page("path", 1)
    assert actual_res[0][0] == "3M"
    assert actual_res[1][0] == "AO Smith"
    assert actual_res[2][0] == "Abbott Laboratories"
