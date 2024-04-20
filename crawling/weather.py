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
path = "https://www.google.com/search?q=weather"
# path의 링크만 바꾸면 어떤 링크도 가능
driver.get(path)

# css 선택자 사용, 원하는 클래스를 가진 웹 요소 접근
# #wob_tm

element = driver.find_element(By.ID, 'wob_tm').text
# print(element)

location = driver.find_element(By.CSS_SELECTOR, 'span.BBwThe').text

print('-' * 30)
print(f"현재 {location}의 온도는 {element}도 입니다.")

driver.quit()
