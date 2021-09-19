from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# WebElement
from selenium.webdriver.remote.webelement import WebElement


def echoElement(ele:WebElement):
    text = ele.text
    data = text.split(" ")
    print(count, ":", data[1], "|", data[6])


if __name__ == '__main__':
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36'
    chrome_options.add_argument('user-agent={0}'.format(user_agent))

    driver = webdriver.Chrome(options=chrome_options)
    driver.get('https://data.10jqka.com.cn/funds/hyzjl')
    driver.save_screenshot('1.png')   #截图保存
    print(driver.title)
    try:
        # element = driver.find_elements_by_xpath("//table[@class='m-table J-ajax-table']/tbody/tr/td[@class='tl']/a")
        element = driver.find_elements_by_xpath("//table[@class='m-table J-ajax-table']/tbody/tr")
        count = 0

        for i in element:
            count += 1
            # print(count, ":", i.accessible_name)
            echoElement(i)
    except Exception as e:
        print(e)

    driver.quit()