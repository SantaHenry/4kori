########################################################################################################
##
### 참조한 블로그 https://beomi.github.io/gb-crawling/posts/2017-01-20-HowToMakeWebCrawler.html
##
########################################################################################################
##
## _4Kori.py
##
## 필요: bs4, selenium, chromedriver, openpyxl, jdcal
##
########################################################################################################

from bs4 import BeautifulSoup
from selenium import webdriver

#크롬드라이버를 Headless모드(창없음)로 동작하게 하기 위한 옵션
myoptions = webdriver.ChromeOptions()
myoptions.add_argument('headless')
myoptions.add_argument('window-size=1920x1080')
myoptions.add_argument("disable-gpu")
myoptions.add_experimental_option('excludeSwitches', ['enable-logging'])
# 혹은 options.add_argument("--disable-gpu")

driver = webdriver.Chrome('env\chromedriver', options=myoptions)

## 암묵적으로 웹 자원 로드를 위해 3초까지 기다려 준다.
driver.implicitly_wait(3)

driver.get('https://test.lavana.cc/category/100-001')

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

cat_title = soup.select('section > div > p')
for t in cat_title:
    print(t.text.strip())

lecturesincat = soup.select('section > div > a')
cnt = 0
for n in lecturesincat:
    ## 아래 출력부를 활성화시키면 내용이 출력됨
    #print(n.text.strip())
    cnt = cnt+1

print(cnt)
driver.quit

cnt=0
soup.clear