#### https://beomi.github.io/gb-crawling/posts/2017-01-20-HowToMakeWebCrawler.html
####
#### parser.py
import requests

### parser.py
import requests
from bs4 import BeautifulSoup
import json
import os

## python파일의 위치
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

### HTTP GET Request
#req = requests.get('https://test.lavana.cc')
### HTML 소스 가져오기
#html = req.text
### BeautifulSoup으로 html소스를 python객체로 변환하기
### 첫 인자는 html소스코드, 두 번째 인자는 어떤 parser를 이용할지 명시.
### 이 글에서는 Python 내장 html.parser를 이용했다.
#soup = BeautifulSoup(html, 'html.parser')

##print(html)

### CSS Selector를 통해 html요소들을 찾아낸다.
#my_titles = soup.select(
#    'body > div'
#    )
#print(my_titles)

##data = {}

##for title in my_titles:
##    data[title.text] = title.get('href')
##    #print(data)

##with open(os.path.join(BASE_DIR, 'result.json'), 'w+') as json_file:
##    json.dump(data, json_file)

##with open(os.path.join(BASE_DIR, 'result.json'), 'w+') as json_file:
##    json.dump(my_titles, json_file)


### https://beomi.github.io/gb-crawling/posts/2017-02-27-HowToMakeWebCrawler-With-Selenium.html

from selenium import webdriver

##크롬드라이버를 Headless모드(창없음)로 동작하게 하기 위한 옵션
#options = webdriver.ChromeOptions()
#options.add_argument('headless')
#options.add_argument('window-size=1920x1080')
#options.add_argument("disable-gpu")
## 혹은 options.add_argument("--disable-gpu")
#driver = webdriver.Chrome('env\chromedriver', chrome_options=options)
driver = webdriver.Chrome('env\chromedriver')

## 암묵적으로 웹 자원 로드를 위해 3초까지 기다려 준다.
driver.implicitly_wait(3)

## url에 접근한다.
driver.get('https://test.lavana.cc/category/100-001')

## Chrome의 경우 | 아까 받은 chromedriver의 위치를 지정해준다.
##driver = webdriver.Chrome('env\chromedriver.exe')

##driver.find_element_by_xpath(
##    '//*[@id="root"]/div/div/header/div/div[1]/button'
##    ).click() ## 버튼클릭하기
#버튼이 실제 버튼이 아니라 가상 버튼이라 그런지 클릭이벤트가 없음

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

cat_title = soup.select('section > div > p')
for t in cat_title:
    print(t.text.strip())

lecturesincat = soup.select('section > div > a')
cnt = 0
for n in lecturesincat:
    #print(n.text.strip())
    cnt = cnt+1

print(cnt)
driver.quit
#data = {}
#for title in my_titles:
#    data[title.text] = title.get('title')
#    cnt = cnt+1

#with open(os.path.join(BASE_DIR, 'result.json'), 'w+') as json_file:
#    json.dump(data, json_file)


### PhantomJS의 경우 | 아까 받은 PhantomJS의 위치를 지정해준다.
#driver = webdriver.PhantomJS('env\phantomjs.exe')
