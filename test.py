import time
import ddddocr
from selenium import webdriver

from selenium.webdriver.common.by import By


# 设置chrome驱动
# driver = webdriver.Chrome("chromedriver.exe")
driver = webdriver.Edge("msedgedriver.exe")

# 设置等待时间
driver.implicitly_wait(5)
# 打开堡垒机地址
driver.get("https://vpnsms.baosteel.com/")

# 设置用户名密码
file = open('userVpn.txt','r',encoding='UTF-8')

strData = file.readline()

str1 = strData.split('||')

file.close()


userName = driver.find_element(By.CSS_SELECTOR,'#uname')
passowrd = driver.find_element(By.CSS_SELECTOR,'#userpwd')

userName.send_keys(str1[0])
passowrd.send_keys(str1[1])




# 设置验证码
img = driver.find_element(By.XPATH,'//*[@id="numImg"]')

img.click()

time.sleep(1)

img1 = driver.find_element(By.XPATH,'//*[@id="numImg"]')

img1.screenshot('test.jpg')



time.sleep(2)

orc = ddddocr.DdddOcr()

time.sleep(2)

with open('test.jpg','rb') as f:
    img1 = f.read()


res = orc.classification(img1)

code = driver.find_element(By.CSS_SELECTOR,'#authCode')

code.send_keys(res)
time.sleep(1)

# 短信密码

pwd = driver.find_element(By.CSS_SELECTOR,'#pwd')
pwd.send_keys(str1[2])
time.sleep(1)

#登录

login  = driver.find_element(By.CSS_SELECTOR,'#login_form > table > tbody > tr:nth-child(5) > td:nth-child(2) > input')
login.click()

time.sleep(1)
#启动链接

start = driver.find_element(By.CSS_SELECTOR,'#vpnOn')
start.click()
