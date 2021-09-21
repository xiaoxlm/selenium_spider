import spider as spi

if __name__ == '__main__':
    url = 'https://data.eastmoney.com/bkzj/hy.html'

    s = spi.SpiderForEastMoney(url)

    firstPageElements = s.get_elements("//table[@style='display: table;']/tbody/tr")

    for ele in firstPageElements:
        print(ele.text)