from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import pandas as pd
import time




# Ouvertur de la page Chrome, Démarrage du robot
driver = webdriver.Chrome('chromedriver.exe')
driver.maximize_window()

# Lien de la page formulaire
driver.get('https://www.vite-un-depanneur.fr/recherche/auto/44/chauffagiste')


#eneleverCookie
time.sleep(2)
btnCookies = driver.find_element_by_xpath('//*[@id="privacy-cookie-banner"]/div/p/strong[2]')
btnCookies.click()

for i in range(1,40):
        print(driver.find_element_by_class_name('adp-current-page').text)
        nextBtn = driver.find_element_by_xpath('//*[@class="adp-icon adp-icon--chevron-droit"]')
        time.sleep(2)
        nextBtn.click()