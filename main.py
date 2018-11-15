"""
    author : Shachuan
    Description : 自动登录联通先锋网站，完成浏览文章的任务
    version : 1.0
"""
import re
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from urllib import request

#broswer = webdriver.Chrome()
account = {'shac':'Pyltwlyhsc92!'}


def login(name,secret):
    """
    broswer.get(
    "http://sso.portal.unicom.local/eip_sso/ssoLogin.html?appid=np000&success=http%3A%2F%2Fwww.portal.unicom.local%2Fuser%2Ftoken&error=http%3A%2F%2Fwww.portal.unicom.local%2Fuser%2Ferror&return=http%3A%2F%2Fwww.portal.unicom.local%2Fdefault%2Fhome")
    user = broswer.find_element_by_id("login")
    user.send_keys(name)
    password = broswer.find_element_by_id("password")
    password.send_keys(secret)
    valid_code = input("请输入验证码\n")
    valid = broswer.find_element_by_id("verifyCode")
    valid.send_keys(valid_code)
    password.send_keys(Keys.ENTER)
    sleep(8)
    xianfeng = broswer.find_element_by_id("xianfeng")
    xianfeng.click()
    sleep(4)
    broswer.get("http://10.245.7.150/page/home/homePage.html")
    sleep(5)
    url = "http://10.245.7.150/api/home/Jrxw?token=ac6989fe044e4381a575ef9d7b385d67&_=1542279463096"
    response = request.urlopen(url)
    content = response.read().decode('utf-8')
    """
    with open('html.txt','r',encoding='utf-8') as f:
        content = f.read()
        print(content)










if __name__ == '__main__':
    for user,password in account.items():
        login(user,password)