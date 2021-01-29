from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import pandas as pd
import time

# Ouvertur de la page Chrome, Démarrage du robot
driver = webdriver.Chrome('chromedriver.exe')
# Lien de la page formulaire
driver.get('https://www.vite-un-depanneur.fr/recherche/auto/06/petits%20travaux')

nextBtn = driver.find_element_by_xpath('//*[@id="pagination"]/nav/span[6]/i')
nextBtn.click()
#driver.find_element_by_xpath('//*[@id="tel_4"]').click()
driver.find_element_by_xpath('//*[@id="article-3"]/div/div[2]/div[1]/span/b').click()
driver.find_element_by_xpath('//*[@id="tel_1"]/a').click()
print(driver.find_element_by_xpath('//*[@id="tel_1"]/a').text)
driver.back()
#for i in range(0,18):
 #   print(driver.find_element_by_xpath('//*[@id="article-' + str(i) + '"]/div/div[2]/div[1]').text)
  #  print(driver.find_element_by_xpath('//*[@id="article-' + str(i) + '"]/div/div[2]/div[3]').text)










