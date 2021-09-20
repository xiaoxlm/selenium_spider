import time
from spider.my_spider import SpiderForEastMoney, iteration_web_elements

if __name__ == '__main__':

    url = 'https://data.eastmoney.com/bkzj/hy.html'
    spider = SpiderForEastMoney(url)

    firstPageElements = spider.get_elements("//table[@style='display: table;']/tbody/tr")

    try:
        iteration_web_elements(firstPageElements)
    except Exception as e:
        print(e)
        exit(-1)

    # next page
    spider.get_element("//*[@id='dataview']/div[3]/div[1]/a[2]").click()
    time.sleep(1)
    secondPageElements = spider.get_elements("//table[@style='display: table;']/tbody/tr")

    try:
        iteration_web_elements(secondPageElements)
    except Exception as e:
        print(e)
        exit(-1)

    spider.quit()
