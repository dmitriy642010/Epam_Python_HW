import asynctest

from Epam_training_HW import hw
from Epam_training_HW.hw.Task_10.hw_10_task_1 import (
    get_companies_from_page,
    get_company_info,
    get_page,
)

import pytest


@pytest.mark.asyncio
async def test_get_company_info(monkeypatch):
    def fake_page(url):
        with open("mmm.html") as file:
            return file.read()

    fake_get_page = asynctest.CoroutineMock(get_page, side_effect=fake_page)
    monkeypatch.setattr(hw.Task_10.hw_10_task_1, "get_page", fake_get_page)
    res = {
        "name": "3M",
        "href": "/stocks/mmm-stock",
        "growth": -1.52,
        "code": "MMM",
        "P/E": 20.12,
        "price": 12216.4,
        "potential profit": 0.6,
    }
    actual_res = await get_company_info(["3M", "/stocks/mmm-stock", -1.52], 70)
    assert res == actual_res


@pytest.mark.asyncio
async def test_get_companies_from_page(monkeypatch):
    def fake_page(url):
        with open("first_page.html") as file:
            return file.read()

    fake_get_page = asynctest.CoroutineMock(get_page, side_effect=fake_page)
    monkeypatch.setattr(hw.Task_10.hw_10_task_1, "get_page", fake_get_page)

    actual_res = await get_companies_from_page("path", 1)
    assert actual_res[0][0] == "3M"
    assert actual_res[1][0] == "AO Smith"
    assert actual_res[2][0] == "Abbott Laboratories"
