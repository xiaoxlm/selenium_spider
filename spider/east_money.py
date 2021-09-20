import json
import time
from typing import List

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.common.by import By

# WebElement
from selenium.webdriver.remote.webelement import WebElement

import model.bk_trade as bk_trade

STOCK_NAME_INDEX = 1
STOCK_PERCENT_INDEX = 5
STOCK_MONEY_INDEX = 6  # 净额


def action():
    url = 'https://data.eastmoney.com/bkzj/hy.html'
    spider = SpiderForEastMoney(url)

    first_page_elements = spider.get_elements("//table[@style='display: table;']/tbody/tr")

    try:
        iteration_web_elements(first_page_elements)
    except Exception as e:
        print(e)
        exit(-1)

    # next page
    spider.get_element("//*[@id='dataview']/div[3]/div[1]/a[2]").click()
    time.sleep(1)
    second_page_elements = spider.get_elements("//table[@style='display: table;']/tbody/tr")

    try:
        iteration_web_elements(second_page_elements)
    except Exception as e:
        print(e)
        exit(-1)

    spider.quit()


def build_east_money_model(element=WebElement):
    tex = element.text
    data = tex.split(" ")

    without_percent = bk_trade.parse_up_down_percent(data[STOCK_PERCENT_INDEX])
    money_dict = bk_trade.parse_money(data[STOCK_MONEY_INDEX])

    model = bk_trade.BkTrade(
        data[STOCK_NAME_INDEX],
        without_percent,
        money_dict[bk_trade.MONEY_KET],
        money_dict[bk_trade.INCREASE_DECREASE_KEY],
        )

    print(json.dumps(model, default=bk_trade.bk_trade_to_dict, ensure_ascii=False))


# List[WebElement]
def iteration_web_elements(elements):
    for ele in elements:
        build_east_money_model(ele)


class SpiderForEastMoney(object):
    def __init__(self, url=""):
        options = Options()
        options.add_argument("--headless")
        user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36'
        options.add_argument('user-agent={0}'.format(user_agent))

        self.Driver = webdriver.Chrome(options=options)
        self.Driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
            "source": """
        Object.defineProperty(navigator, 'webdriver', {
          get: () => false
        })
      """
        })
        self.Driver.get(url)

    def get_element(self, xpath="") -> WebElement:
        return self.Driver.find_element(By.XPATH, xpath)

    def get_elements(self, xpath="") -> List[WebElement]:
        return self.Driver.find_elements(By.XPATH, xpath)

    def quit(self):
        self.Driver.quit()
