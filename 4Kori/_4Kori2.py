from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

##크롬드라이버를 Headless모드(창없음)로 동작하게 하기 위한 옵션
myoptions = webdriver.ChromeOptions()
myoptions.add_argument('headless')
myoptions.add_argument('window-size=1920x1080')
myoptions.add_argument("disable-gpu")
myoptions.add_experimental_option('excludeSwitches', ['enable-logging'])
## 혹은 options.add_argument("--disable-gpu")
driver = webdriver.Chrome('env\chromedriver', options=myoptions)

## 암묵적으로 웹 자원 로드를 위해 3초까지 기다려 준다.
driver.implicitly_wait(3)

## url에 접근한다.
driver.get('https://test.lavana.cc')

driver.find_element_by_xpath(
    '//*[@id="root"]/div/div/header/div/div[1]/button'
    ).send_keys(Keys.ENTER) 

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

data_url = {}
my_title = soup.select('#category-menu-list-grow > ul > a')
for p in my_title:
    #print(p.get('href'))
    data_url[p.text] = p.get('href')

driver.quit

soup.clear

print(data_url)