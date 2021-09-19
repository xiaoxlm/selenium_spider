from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")

driver = webdriver.Chrome(options=chrome_options)
driver.get('http://www.baidu.com')
driver.save_screenshot('1.png')   #截图保存
data = driver.page_source   #获取网页文本

print(data)
driver.quit()