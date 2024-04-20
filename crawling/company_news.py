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

# 키워드 입력 받기
# keyword = input("뉴스 키워드를 입력해 주세요: ")
keyword = '멀티캠퍼스'
# path = "https://search.naver.com/search.naver?ssc=tab.news.all&where=news&sm=tab_jum&query="
# path : 네이버 뉴스 >> 검색 '푸바오' (=%ED%91%B8%EB%B0%94%EC%98%A4)
driver.get(f"https://search.naver.com/search.naver?ssc=tab.news.all&where=news&sm=tab_jum&query={keyword}")

# 뉴스 타이틀 >> news_tit
title_list = driver.find_elements(By.CLASS_NAME, 'news_tit')
company_list = driver.find_elements(By.CLASS_NAME, 'info.press')
content_list = driver.find_elements(By.CLASS_NAME, 'dsc_wrap')

# for title  in title_list:
#     title = title.text
#     print(title)

# for company in company_list:
#     company = company.text
#     print(company)

# for content in content_list:
#     content = content.text
#     print(content)

for title, company, content in zip(title_list, company_list, content_list):
    title = title.text
    company = company.text
    content = content.text
    print(f'{company}의 기사 \n제목:{title} \n내용:{content}''\n')
    print('-' * 15)

driver.quit()

