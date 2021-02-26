from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import pandas as pd
import time

# Ouvertur de la page Chrome, Démarrage du robot
driver = webdriver.Chrome('chromedriver.exe')
driver.maximize_window()

# Lien de la page formulaire
driver.get('https://www.vite-un-depanneur.fr/recherche/auto/06/petits%20travaux')

#eneleverCookie
time.sleep(2)
btnCookies = driver.find_element_by_xpath('//*[@id="privacy-cookie-banner"]/div/p/strong[2]')
btnCookies.click()
comptPage = 2
raisonSociales = []
adresses = []
tels = []

for i in range(2,4):

    for i in range(0, 18):
        nextBtn = driver.find_element_by_xpath('//*[@class="adp-icon adp-icon--chevron-droit"]')
        for page in range(1, comptPage):
            # page Suivante
            nextBtn.click()

        try:

            driver.find_element_by_xpath('//*[@id="article-' + str(i) + '"]/div/div[2]/div[1]/span/b').click()
            raisonSocial = driver.find_element_by_xpath('//*[@id="adp-js-core"]/main/header/h1').text
            print(driver.find_element_by_xpath('//*[@id="adp-js-core"]/main/header/h1').text)
            adresse = driver.find_element_by_xpath('//*[@id="adp-js-core"]/main/div[2]/div[1]/div[1]/div[2]/div[1]/span/a/span[1]').text
            print(driver.find_element_by_xpath('//*[@id="adp-js-core"]/main/div[2]/div[1]/div[1]/div[2]/div[1]/span/a/span[1]').text)
            driver.find_element_by_xpath('//*[@id="tel_1"]/a').click()
            tel = driver.find_element_by_xpath('//*[@id="tel_1"]/a').text
            print(driver.find_element_by_xpath('//*[@id="tel_1"]/a').text)



            raisonSociales.append(raisonSocial)
            adresses.append((adresse))
            tels.append(tel)

        except:
            print('null')
        # page précédente
        driver.back()
        comptPage = comptPage + 1



#Mise en forme du tableau
test = pd.DataFrame({
    'Raison Sociale' : raisonSociales,
    'Adresses' : adresses,
    'Telephone' : tels

})
print(test)
#Creation de fichier csv contenant les donnees scrapees
test.to_csv('petitTravaux06.csv',sep="|", encoding = 'iso-8859-1')

























