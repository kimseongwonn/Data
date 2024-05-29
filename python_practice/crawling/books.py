from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# 브라우저 옵션 설정
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
# 브라우저를 자동화한 후 >> browser window 창 유지 (따로 띄워 놓은 상태를 유지하겠다.)
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
# excludeSwitches : 불필요한 로깅 메시지 >> 브라우저에서 제외

driver = webdriver.Chrome(options=chrome_options)
# 원하는 웹페이지로 이동
path = 'https://product.kyobobook.co.kr/bestseller/online?period=001&page=1&per=50'
driver.get(path)

titles = driver.find_elements(By.CLASS_NAME,'prod_info')
authors = driver.find_elements(By.CLASS_NAME, 'prod_author')
prices = driver.find_elements(By.CLASS_NAME, 'price')
rank = 0

for title, author, price in zip(titles, authors, prices):
    rank += 1
    title = title.text
    author = author.text
    price = price.text

    if rank <= 5:
        print(f'순위 : {rank} \n제목 : {title} \n저자 : {author} \n가격 : {price}''\n')
        print('-'*30)

driver.quit()