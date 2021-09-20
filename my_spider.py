import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.common.by import By

# WebElement
from selenium.webdriver.remote.webelement import WebElement

STOCK_NAME_INDEX = 1
STOCK_INCREASE_PERCENT_INDEX = 5
STOCK_NET_INDEX = 6  # 净额

def echoElement(ele:WebElement):
    text = ele.text
    data = text.split(" ")
    print(count, ":", data[STOCK_NAME_INDEX], "|", data[STOCK_INCREASE_PERCENT_INDEX], "|", data[STOCK_NET_INDEX])


if __name__ == '__main__':
    options = Options()
    options.add_argument("--headless")
    user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36'
    options.add_argument('user-agent={0}'.format(user_agent))
    driver = webdriver.Chrome(options=options)

    driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
        "source": """
        Object.defineProperty(navigator, 'webdriver', {
          get: () => false
        })
      """
    })

    driver.get('https://data.eastmoney.com/bkzj/hy.html')
    try:
        elementFromFirstPage = driver.find_elements(By.XPATH, "//table[@style='display: table;']/tbody/tr")
        count = 0

        for ele in elementFromFirstPage:
            count += 1
            echoElement(ele)
    except Exception as e:
        print(e)

    # 下一页
    try:
        driver.find_element(By.XPATH, "//*[@id='dataview']/div[3]/div[1]/a[2]").click()
        time.sleep(1)
        elementFromSecondPage = driver.find_elements(By.XPATH, "//table[@style='display: table;']/tbody/tr")

        for ele2 in elementFromSecondPage:
            count += 1
            echoElement(ele2)
    except Exception as e2:
        print(e2)

    driver.quit()