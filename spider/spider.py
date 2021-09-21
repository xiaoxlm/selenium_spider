from typing import List
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By


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