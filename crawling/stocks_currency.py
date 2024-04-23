from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# 브라우저 옵션 설정
chrome_options = Options()

# 셀러니움에서 크롬 브라우저를 헤드가 없는 모양(headless)으로 설정하겠다.
# headless : GUI(Graphic User Interface) 없이 실행하겠다.
chrome_options.add_argument("--headless")
# >> 실제 브라우저 창이 눈에 보이지 않게 해준다.
# >> 아래 detach 코드와 반대되는 개념
chrome_options.add_experimental_option("detach", True)

# 브라우저를 자동화한 후 >> browser window 창 유지 (따로 띄워 놓은 상태를 유지하겠다.)
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
# excludeSwitches : 불필요한 로깅 메시지 >> 브라우저에서 제외

# selenium 에서 크롬 웹 드라이버를 자동으로 다운로드 및 설치하는 코드
service = Service(executable_path=ChromeDriverManager().install())

driver = webdriver.Chrome(service=service, options=chrome_options)

# 드라이버를 구동시키면서 10초 씩 기다렸다 구동하도록 해주는 코드
wait = WebDriverWait(driver, 10)

# 원하는 웹페이지로 이동
# path = 'https://www.google.com/search?q=애플 주식'
# driver.get(path)


# 주소 위치로 이동

keyword_list = ['애플', '삼성전자', 'SK하이닉스']

for kw in keyword_list:
    url = (f'https://www.google.com/search?q={kw}+주식')
    
    driver.get(url)
    
    # wait를 사용할때 (driver.find_element)는 사용 불가
    # WebDriverWqit(driver, timeout) >> wait
    # EC.presence_of_element_located
    name = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,".DoxwDb"))).text
    price = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,".IsqQVc"))).text
    high_price = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"div[data-attrid='최고']"))).text
    low_price = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"div[data-attrid='최저']"))).text
    currency = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".knFDje"))).text
    
    if currency == 'KRW':
        price = price + 'won'
        high_price = high_price + 'won'
        low_price = low_price + 'won'
    elif currency == 'USD':
        price = price + '$'
        high_price = high_price + '$'
        low_price = low_price + '$'

    # 데이터 출력
    print(f'{kw} 주식 정보 수집 현황')
    print(f'주식명 : {name}')
    print(f'현재가격 : {price}')
    print(f'최고가격 : {high_price}')
    print(f'최저가격 : {low_price}\n')
    
driver.quit()



