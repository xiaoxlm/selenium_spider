from spider.my_spider import SpiderForEastMoney

if __name__ == '__main__':
    url = 'https://data.eastmoney.com/bkzj/hy.html'

    spider = SpiderForEastMoney(url)

    firstPageElements = spider.get_elements("//table[@style='display: table;']/tbody/tr")

    for ele in firstPageElements:
        spider.format_dfcf_data(ele)