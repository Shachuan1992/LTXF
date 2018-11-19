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

broswer = webdriver.Chrome()
account = {'shac':'Pyltwlyhsc92!','wangld30':'Landiwang30.'}


def login(name,secret):
    # 打开云门户主页面
    broswer.get(
    "http://sso.portal.unicom.local/eip_sso/ssoLogin.html?appid=np000&success=http%3A%2F%2Fwww.portal.unicom.local%2Fuser%2Ftoken&error=http%3A%2F%2Fwww.portal.unicom.local%2Fuser%2Ferror&return=http%3A%2F%2Fwww.portal.unicom.local%2Fdefault%2Fhome")
    # 根据字典填入用户名及密码
    user = broswer.find_element_by_id("login")
    user.send_keys(name)
    password = broswer.find_element_by_id("password")
    password.send_keys(secret)
    valid_code = input("请输入验证码\n")
    valid = broswer.find_element_by_id("verifyCode")
    valid.send_keys(valid_code)
    password.send_keys(Keys.ENTER)
    sleep(10)
    # 找到联通先锋的按钮
    xianfeng = broswer.find_element_by_id("xianfeng")
    xianfeng.click()
    sleep(5)
    # 去往主页
    broswer.get("http://10.245.7.150/page/home/homePage.html")
    sleep(5)
    # 获取cookies，使用正则表达式从中提取token
    cookies = str(broswer.get_cookies())
    p1 = re.compile(r"\'value\':\s\'([^\"]*)\'")
    token = re.findall(p1, cookies)[0]
    # 重定向到今日新闻主页面
    url = "http://10.245.7.150/api/home/Jrxw?token="+token
    # 寻找infoID标签
    response = request.urlopen(url)
    content = response.read().decode('utf-8')
    p2 = re.compile(r'\"infoId\":\"([^\"]*)\"')
    _infoId = re.findall(p2, content)
    num = 0
    for link_id in _infoId:
        # 浏览页面
        link = "http://10.245.7.150/page/home/detailPage.html?id="+link_id
        broswer.get(link)
        num = num +1
        print("已经浏览 %d 篇\n" % num)
        sleep(5)
        if num == 50:
            print("%s的浏览任务完成\n" % name)
            break


if __name__ == '__main__':
    for user,password in account.items():
        login(user,password)