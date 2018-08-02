#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
                            _ooOoo_  
                           o8888888o  
                           88" . "88  
                          (|  -_-  |)  
                           O\  =  /O  
                        ____/`---'\____  
                      .   ' \\| |// `.  
                       / \\||| : |||// \  
                     / _||||| -:- |||||- \  
                       | | \\\ - /// | |  
                     | \_| ''\---/'' | |  
                      \ .-\__ `-` ___/-. /  
                   ___`. .' /--.--\ `. . __  
                ."" '< `.___\_<|>_/___.' >'"".  
               | | : `- \`.;`\ _ /`;.`/ - ` : | |  
                 \ \ `-. \_ __\ /__ _/ .-` / /  
         ======`-.____`-.___\_____/___.-`____.-'======  
                            `=---='  
  
         .............................................  
                  佛祖镇楼                  BUG辟易  
          佛曰:  
                  写字楼里写字间，写字间里程序员；  
                  程序人员写程序，又拿程序换酒钱。  
                  酒醒只在网上坐，酒醉还来网下眠；  
                  酒醉酒醒日复日，网上网下年复年。  
                  但愿老死电脑间，不愿鞠躬老板前；  
                  奔驰宝马贵者趣，公交自行程序员。  
                  别人笑我忒疯癫，我笑自己命太贱；  
                  不见满街漂亮妹，哪个归得程序员？ 
'''
# @File  : publish.py
# @Author: huguangzhi
# @ContactEmail : huguangzhi@ucsdigital.com.com 
# @ContactPhone : 13121961510 
# @Date  : 2018-08-01 - 18:45
# @Desc  : 发布影视作品

from time import sleep

from selenium import webdriver
from selenium.webdriver.support.select import Select

import ReleaseInfo

name = ReleaseInfo.UserInfo.username
passwd = ReleaseInfo.UserInfo.passwd
moviename = ReleaseInfo.MovieInfo.moviename
movieothername = ReleaseInfo.MovieInfo.movieothername
copyrightstart = ReleaseInfo.MovieInfo.copyrightstart
copyrightend = ReleaseInfo.MovieInfo.copyrightend
fileshoot = ReleaseInfo.MovieInfo.fileshoot
filescreen = ReleaseInfo.MovieInfo.filescreen
director = ReleaseInfo.MovieInfo.director
artistor = ReleaseInfo.MovieInfo.artistor
timeline = ReleaseInfo.MovieInfo.timeline
releasetime = ReleaseInfo.MovieInfo.releasetime
moviediscrib = ReleaseInfo.MovieInfo.moviediscrib
abstract = ReleaseInfo.MovieInfo.abstract
perprice = ReleaseInfo.MovieInfo.price
poster = ReleaseInfo.MovieInfo.poster
sourcefile = ReleaseInfo.MovieInfo.sourcemp4
movienum = ReleaseInfo.MovieInfo.paicihao


browser = webdriver.Chrome("../chromedriver.exe")


def login():
    browser.get("http://movmall.com/MVM/HTML/user/login.html")
    browser.find_element_by_xpath('//*[@id="mycookie"]/label/div/input').send_keys(name)
    browser.find_element_by_xpath('/html/body/div[2]/section/div/div[3]/label/div/input').send_keys(passwd)
    browser.find_element_by_xpath('/html/body/div[2]/section/div/a').click()


login()
sleep(2)
browser.get('http://movmall.com/MVM/HTML/seller/publish_film.html')
def publishMovieinfo():
    browser.find_element_by_id('pName').send_keys(moviename)
    browser.find_element_by_id('pEName').send_keys(movieothername)

    # 自主版权
    browser.find_element_by_xpath('//*[@id="select05001"]').click()
    # # 代理版权独家
    # browser.find_element_by_xpath('//*[@id="select05002"]').click()
    # # 代理版权非独家
    # browser.find_element_by_xpath('//*[@id="select05003"]').click()
    # 可授权力
    browser.find_element_by_xpath('//*[@id="filmlist-info"]/ul[1]/li[3]/div/div[3]/div[1]/label[1]').click()
    browser.find_element_by_xpath('//*[@id="filmlist-info"]/ul[1]/li[3]/div/div[3]/div[1]/label[3]').click()
    browser.find_element_by_xpath('//*[@id="filmlist-info"]/ul[1]/li[3]/div/div[3]/div[1]/label[2]').click()
    browser.find_element_by_xpath('//*[@id="start_time"]').send_keys(copyrightstart)
    browser.find_element_by_xpath('//*[@id="end_time"]').send_keys(copyrightend)
    # 可授权地区
    browser.find_element_by_xpath('//*[@id="filmlist-info"]/ul[1]/li[3]/div/div[5]/div[1]/label[1]').click()
    browser.find_element_by_xpath('//*[@id="filmlist-info"]/ul[1]/li[3]/div/div[5]/div[1]/label[2]').click()
    browser.find_element_by_xpath('//*[@id="filmlist-info"]/ul[1]/li[3]/div/div[5]/div[1]/label[3]').click()
    browser.find_element_by_xpath('//*[@id="filmlist-info"]/ul[1]/li[3]/div/div[5]/div[1]/label[4]').click()
    browser.find_element_by_xpath('//*[@id="filmlist-info"]/ul[1]/li[3]/div/div[5]/div[1]/label[5]').click()
    browser.find_element_by_xpath('//*[@id="filmlist-info"]/ul[1]/li[3]/div/div[5]/div[1]/label[6]').click()
    # 收益模式
    browser.find_element_by_xpath('//*[@id="filmlist-info"]/ul[1]/li[3]/div/div[6]/div[1]/div[1]/label').click()
    browser.find_element_by_xpath('//*[@id="filmlist-info"]/ul[1]/li[3]/div/div[6]/div[1]/div[2]/label').click()
    browser.find_element_by_xpath('//*[@id="filmlist-info"]/ul[1]/li[3]/div/div[6]/div[1]/div[3]/label').click()
    browser.find_element_by_xpath('//*[@id="filmlist-info"]/ul[1]/li[3]/div/div[6]/div[1]/div[4]/label').click()
    browser.find_element_by_xpath('//*[@id="filmlist-info"]/ul[1]/li[3]/div/div[6]/div[1]/div[5]/label').click()
    # 拍摄许可证
    browser.find_element_by_xpath("//*[@id='file_produce']").click()
    browser.find_element_by_xpath('//*[@id="file_produce"]').send_keys(fileshoot)
    # 公映许可证
    browser.find_element_by_xpath('//*[@id="file_play"]').click()
    browser.find_element_by_xpath('//*[@id="file_play"]').send_keys(filescreen)

    browser.find_element_by_xpath('//*[@id="filmlist-info"]/ul[1]/li[4]/div/div[1]/div[1]/label').click()

    # 电影题材：共计3行6列，只需要改动倒数第一个[行]和倒数第二个[列]
    browser.find_element_by_xpath('//*[@id="filmlist-info"]/ul[1]/li[4]/div/div[2]/div[2]/div[1]/label[1]').click()
    browser.find_element_by_xpath('//*[@id="filmlist-info"]/ul[1]/li[4]/div/div[2]/div[2]/div[1]/label[2]').click()
    browser.find_element_by_xpath('//*[@id="filmlist-info"]/ul[1]/li[4]/div/div[2]/div[2]/div[2]/label[1]').click()

    # 制片地区:中国
    browser.find_element_by_xpath('//*[@id="filmlist-info"]/ul[1]/li[4]/div/div[3]/div[1]/label[1]').click()

    browser.find_element_by_xpath('//*[@id="director"]').send_keys(director)
    browser.find_element_by_xpath('//*[@id="tostar"]').send_keys(artistor)

    browser.find_element_by_xpath('//*[@id="film_time"]').send_keys(timeline)
    browser.find_element_by_xpath('//*[@id="timeBirth"]').send_keys(releasetime)
    browser.find_element_by_xpath('//*[@id="filmlist-info"]/ul[1]/li[4]/div/div[10]/input').send_keys(moviediscrib)
    browser.find_element_by_xpath('//*[@id="filmlist-info"]/ul[1]/li[4]/div/div[11]/textarea').send_keys(abstract)

    # 价格设置
    for i in range(1, 4):
        Select(browser.find_element_by_xpath("//*[@id='product_system']")).select_by_value("0400" + str(i))
        for j in range(1, 6):
            Select(browser.find_element_by_xpath("//*[@id='product_buy']")).select_by_value("0900" + str(j))
            try:
                browser.find_element_by_xpath("//*[@id='product_price']").send_keys(perprice)
            except:
                pass
            browser.find_element_by_xpath("//*[@id='submit_price']").click()
            sleep(0.2)

    browser.find_element_by_xpath('//*[@id="no-inventory"]').click()

    # 海报
    browser.find_element_by_xpath('//*[@id="filmlist-info"]/ul[1]/li[9]/div[1]/div/div/div/div[2]/div/a').click()
    browser.find_element_by_xpath(
        '//*[@id="filmlist-info"]/ul[1]/li[9]/div[1]/div/div/div/div[2]/div/input[1]').send_keys(poster)
# 正片文件
browser.find_element_by_xpath("//*[@id='filmlist-info']/ul[1]/li[9]/div[3]/div/div/a[1]").click()
Select(browser.find_element_by_xpath('//*[@id="feature_file"]')).select_by_value('17002')

browser.find_element_by_xpath('//*[@id="04001-10001"]').click()
try:
    browser.find_element_by_xpath('//*[@id="material_box"]/div[1]/div/div[1]/div/input').send_keys(movienum)
except:
    pass
browser.find_element_by_xpath('//*[@id="04002-10012"]').click()
browser.find_element_by_xpath('//*[@id="full-tip"]/section/div[1]/div[5]/div[1]/span[3]/a').click()
browser.find_element_by_xpath("//*[@id='full-tip']/section/div[1]/div[5]/div[1]/span[3]/a/input").send_keys(sourcefile)
going = browser.find_element_by_xpath('//*[@id="full-tip"]/section/div[1]/div[5]/div[2]/div/table/tbody/tr/td[5]')
print(going)

# 确认正片
# browser.find_element_by_xpath("//*[@id='full-tip']/section/div[2]/a[1]").click()

# browser.find_element_by_xpath('').send_keys()