#!/usr/bin/env python
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import datetime
import time

twoweeks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

#memberU is the usernames
#memberP is the passwword of each individual
memberU = ['#1', '#2', '#3', '#4']
memberP = {'#1': 'P1', '#2': 'P2', '#3': 'P3', '#4': 'P4'}

#add location of driver for ##
chromedriver = "##"
driver = webdriver.Chrome(chromedriver)

tot = (range(len(memberU)))
u = 0
for a in tot:
    print(memberU[u])
    driver = webdriver.Chrome(chromedriver)
    driver.get("###")
    #enter website of reservation room for ###
    time.sleep(0.5)
    for x in twoweeks:
        date_button = driver.find_element_by_xpath('//*[@id="eq-time-grid"]/div[1]/div[1]/div/button[2]')
        date_button.click()
        #this clicks to forward 2 weeks
    time.sleep(1)
    t = u * 6 + 1
    x = memberU[u]
    y = memberP.get(x)
    max_of_slot = range(6)
    time.sleep(1)
    slotelement = driver.find_element_by_xpath('//*[@id="eq-time-grid"]/div[2]/div/table/tbody/tr/td[3]/div/div/div/div[1]/div/table/tbody/tr/td/div/div/a['+str(t)+']/span')
    for e in max_of_slot:
        if slotelement != None:
        slotelement.click()
        t += 1
        extraclick = driver.find_element_by_xpath('//*[@id="s-lc-group-description"]')
        extraclick.click()
        time.sleep(0.5)

    submit_times = driver.find_element_by_xpath('//*[@id="submit_times"]')
    submit_times.click()

    time.sleep(1)

    username_input = driver.find_element_by_xpath('//*[@id="weblogin_netid"]')
    username_input.send_keys(x)
    password_input = driver.find_element_by_xpath('//*[@id="weblogin_password"]')
    password_input.send_keys(y)

    submit_up = driver.find_element_by_xpath('//*[@id="submit_button"]')
    submit_up.click()

    confirm_click = driver.find_element_by_xpath('//*[@id="terms_accept"]')
    confirm_click.click()

    DisplayName = driver.find_element_by_xpath('//*[@id="nick"]')
    DisplayName.send_keys("####")
    #enter display name for ####

    final_submit = driver.find_element_by_xpath('//*[@id="s-lc-eq-bform-submit"]')
    final_submit.click()

    time.sleep(1)

    logoutbutton = driver.find_element_by_xpath('//*[@id="s-lc-eq-auth-lobtn"]')
    logoutbutton.click()
    u += 1
    driver.close()
