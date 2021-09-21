import json
import time

# WebElement
from selenium.webdriver.remote.webelement import WebElement

import model.bk_trade as bk_trade
import spider.spider as spi

STOCK_NAME_INDEX = 1
STOCK_PERCENT_INDEX = 5
STOCK_MONEY_INDEX = 6  # 净额


def action():
    url = 'https://data.eastmoney.com/bkzj/hy.html'
    s = spi.SpiderForEastMoney(url)

    first_page_elements = s.get_elements("//table[@style='display: table;']/tbody/tr")

    try:
        iteration_web_elements(first_page_elements)
    except Exception as e:
        print(e)
        exit(-1)

    # next page
    s.get_element("//*[@id='dataview']/div[3]/div[1]/a[2]").click()
    time.sleep(1)
    second_page_elements = s.get_elements("//table[@style='display: table;']/tbody/tr")

    try:
        iteration_web_elements(second_page_elements)
    except Exception as e:
        print(e)
        exit(-1)

    s.quit()


def build_east_money_model(element=WebElement):
    tex = element.text
    data = tex.split(" ")

    without_percent = bk_trade.parse_up_down_percent(data[STOCK_PERCENT_INDEX])

    model = bk_trade.BkTrade(
        data[STOCK_NAME_INDEX],
        without_percent,
        data[STOCK_MONEY_INDEX],
        )

    print(json.dumps(model, default=bk_trade.bk_trade_to_dict, ensure_ascii=False))


# List[WebElement]
def iteration_web_elements(elements):
    for ele in elements:
        build_east_money_model(ele)



