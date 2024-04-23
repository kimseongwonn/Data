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
path = 'https://www.google.com/search?q=애플 주식'
driver.get(path)

name = driver.find_element(By.CSS_SELECTOR,".DoxwDb").text
price = driver.find_element(By.CSS_SELECTOR,".IsqQVc").text
high_price = driver.find_element(By.CSS_SELECTOR,"div[data-attrid='최고']").text
low_price = driver.find_element(By.CSS_SELECTOR,"div[data-attrid='최저']").text

print(f'주식명 : {name}')
print(f'현재가격 : {price}')
print(f'최고가격 : {high_price}')
print(f'최저가격 : {low_price}')

print('-'*50)

# 주소 위치로 이동

keyword_list = ['애플', '삼성전자', 'SK하이닉스']

for kw in keyword_list:
    driver.get(f'https://www.google.com/search?q={kw}+주식')
    
    name = driver.find_element(By.CSS_SELECTOR,".DoxwDb").text
    price = driver.find_element(By.CSS_SELECTOR,".IsqQVc").text
    high_price = driver.find_element(By.CSS_SELECTOR,"div[data-attrid='최고']").text
    low_price = driver.find_element(By.CSS_SELECTOR,"div[data-attrid='최저']").text

    print(f'주식명 : {name}')
    print(f'현재가격 : {price}')
    print(f'최고가격 : {high_price}')
    print(f'최저가격 : {low_price}\n')
    
driver.quit()



