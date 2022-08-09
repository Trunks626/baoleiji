import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import pyautogui
def  baolei(string1,string2,string3,string4):
    # 设置chrome驱动
    #driver = webdriver.Chrome("chromedriver.exe")
    driver = webdriver.Edge("msedgedriver.exe")

    #driver = webdriver.Chrome('C:\Program Files\Google\Chrome\Application\chromedriver.exe')


    # 设置等待时间
    driver.implicitly_wait(5)
    # 打开堡垒机地址
    driver.get("https://10.70.0.220/#/login")

    # 如果是警告画面处理点击
    element = driver.find_element(By.ID,'details-button')

    element.click()

    driver.implicitly_wait(5)

    element2 = driver.find_element(By.ID,'proceed-link')

    element2.click()



    #手机令牌登录

    mobile = driver.find_element(By.XPATH,'//*[@id="login-root"]/div/div[2]/div/div/div[1]/div/div[1]/div[1]/div/div[2]/div')

    mobile.click()




    # 登录账号密码

    # userName = driver.find_element(By.CSS_SELECTOR,'#login-root > div > div.login-content-container > div > div > div.login-content-layout > div > div:nth-child(1) > div.tab-content > div:nth-child(1) > div > form > div:nth-child(2) > div > div > input')
    #
    # password = driver.find_element(By.CSS_SELECTOR,'#login-root > div > div.login-content-container > div > div > div.login-content-layout > div > div:nth-child(1) > div.tab-content > div:nth-child(1) > div > form > div:nth-child(3) > div > div > input')
    #
    # login = driver.find_element(By.CSS_SELECTOR,'#login-root > div > div.login-content-container > div > div > div.login-content-layout > div > div:nth-child(1) > div.tab-content > div:nth-child(1) > div > button')


    userName = driver.find_element(By.CSS_SELECTOR,'#login-root > div > div.login-content-container > div > div > div.login-content-layout > div > div:nth-child(1) > div.tab-content > div:nth-child(2) > div > form > div:nth-child(2) > div > div > div > div > input')

    password = driver.find_element(By.CSS_SELECTOR,'#login-root > div > div.login-content-container > div > div > div.login-content-layout > div > div:nth-child(1) > div.tab-content > div:nth-child(2) > div > form > div:nth-child(3) > div > div > div > div > input')

    pwd = driver.find_element(By.CSS_SELECTOR,'#login-root > div > div.login-content-container > div > div > div.login-content-layout > div > div:nth-child(1) > div.tab-content > div:nth-child(2) > div > form > div:nth-child(4) > div > div > div > div > input')


    login = driver.find_element(By.CSS_SELECTOR,'#login-root > div > div.login-content-container > div > div > div.login-content-layout > div > div:nth-child(1) > div.tab-content > div:nth-child(2) > div > button')

    file = open('user.txt','r',encoding='UTF-8')

    strData = file.readline()

    str1 = strData.split('||')

    file.close()

    userName.send_keys(str1[0])
    #userName.send_keys("chenweiwei")
    #userName.send_keys("lishuiqing")

    password.send_keys(str1[1])
    #password.send_keys("!QAZxsw2")
    #password.send_keys("Susan546~")

    print(string1)
    pwd.send_keys(string1)

    login.click()


    driver.implicitly_wait(5)

    # 按掉提示

    x = driver.find_element(By.CSS_SELECTOR,'#guideOverlap > div > div > div:nth-child(1) > div:nth-child(1)')

    x.click()



    # 选中集团正式环境服务器

    # rgButton = driver.find_element(By.CSS_SELECTOR,'#host-operation-root > div > div.t-body > div:nth-child(1) > div:nth-child(6) > div > div')
    #
    # print(rgButton)
    #
    # rgButton.click()

    # 服务器选择
    print('开始寻找服务器------')
    table = driver.find_element(By.XPATH,'//*[@id="host-operation-root"]/div/div[3]')

    trlist = table.find_elements(By.CLASS_NAME,'t-body-tr.tr')

    check = ''

    print('服务器判断')
    # 集团正式
    if string2 == '集团正式':
        check = '10.70.11.202:15202'
    else:
        # 抛账中心
        check = '10.70.11.201:15201'

    flag = 0
    count = 1
    finalCount = 0
    for element in trlist:
        tdlist = element.find_elements(By.CLASS_NAME,'t-body-td.td')
        print(element.text)
        for element2 in tdlist:
            print(count)
            # 服务器判断
            if element2.text == check:
                flag = 1
                finalCount = count
                break
        count = count + 1

        if flag == 1:
            break

        #if flag == 1:
        #    for element2 in tdlist:
        #        if element2.text == '登录':
        #            x, y = element2.location["x"], element2.location["y"]

                    # host-operation-root > div > div.t-body > div:nth-child(1) > div:nth-child(6) > div > div

                    # host-operation-root > div > div.t-body > div:nth-child(2) > div:nth-child(6) > div > div

                    # host-operation-root > div > div.t-body > div:nth-child(5) > div:nth-child(6) > div > div


        #            print(x,y)
        #            element2.click()
        #            break


        #if flag == 1:
        #    break
    t = '# host-operation-root > div > div.t-body > div:nth-child('+str(finalCount)+') > div:nth-child(6) > div > div'
    t2 = '#host-operation-root > div > div.t-body > div:nth-child(1) > div:nth-child(6) > div > div'
    print(t2)

    print(t)
    #登录按钮点击
    g = driver.find_element(By.CSS_SELECTOR,'#host-operation-root > div > div.t-body > div:nth-child('+str(finalCount)+') > div:nth-child(6) > div > div')
    g.click()




    # 输入集团正式环境账号密码

    rgUserName = driver.find_element(By.CSS_SELECTOR,'#resource-manual-login > div > div:nth-child(1) > div > div.yab-input-layout-css > div > input')


    rgPassword = driver.find_element(By.CSS_SELECTOR,'#resource-manual-login > div > div.yab-input.item-distance > div > div.yab-input-layout-css > div > input')

    scheam = driver.find_element(By.CSS_SELECTOR,'#resource-manual-login > div > div:nth-child(4) > div > div.yab-input-layout-css > div > input')


    rgUserName.send_keys(string3)

    rgPassword.send_keys(string4)



    if string2 == '集团正式':
        # rgUserName.send_keys("r4admin")
        #
        # rgPassword.send_keys("r4admin")

        scheam.send_keys("rgdbprod")
    else:

        # rgUserName.send_keys("bcadmin")
        #
        # rgPassword.send_keys("bcadmin")

        scheam.send_keys("bcdbprod")


    time.sleep(2)

    pyautogui.press('enter')

    time.sleep(2)

    pyautogui.press('left')

    time.sleep(2)

    pyautogui.press('enter')

    time.sleep(2)

    pyautogui.press('enter')

    driver.quit()


