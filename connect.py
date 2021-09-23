#!/usr/bin/env python
# -*- coding: utf-8 -*-


from selenium import webdriver
import time

options=webdriver.ChromeOptions()
options.add_argument('--no-sandbox')
options.add_argument('--headless')

driver = webdriver.Chrome(options=options)
driver.get("https://lanauth.it.osakac.ac.jp/")

time.sleep(5)

login_id = driver.find_element_by_name("username")
login_id.send_keys("学籍番号")

# パスワードを入力
password = driver.find_element_by_name("password")
password.send_keys("パスワード")

#ログインボタンをクリック
login_btn = driver.find_element_by_name("Submit")
login_btn.click()

time.sleep(5)

driver.close()
