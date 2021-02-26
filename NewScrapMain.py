from selenium import webdriver
import pandas as pd
import time

# Ouvertur de la page Chrome, Démarrage du robot
from selenium.webdriver.common.by import By

driver = webdriver.Chrome('chromedriver.exe')
driver.maximize_window()

pageActuel = ''
print('Entrer le metier : ')
metier = input()
print('Entrer le département : ')
departement = input()
# Lien de la page formulaire
driver.get('https://www.vite-un-depanneur.fr/recherche/auto/'+str(departement)+'/'+metier)

#eneleverCookie
time.sleep(2)
btnCookies = driver.find_element_by_xpath('//*[@id="privacy-cookie-banner"]/div/p/strong[2]')
btnCookies.click()
comptPage = 2
raisonSociales = []
adresses = []
tels = []
pageContinuer = True

while(pageContinuer):
    for i in range(0, 20):
        try:

            print(driver.find_element(By.CSS_SELECTOR, "#article-"+str(i)+" .adp-rs").text)
            raison = driver.find_element(By.CSS_SELECTOR, "#article-"+str(i)+" .adp-rs").text

            print(driver.find_element(By.CSS_SELECTOR, "#article-"+str(i)+" .adp-listing-result__address").text)
            adresse = driver.find_element(By.CSS_SELECTOR, "#article-"+str(i)+" .adp-listing-result__address").text

            time.sleep(1)
            driver.find_element_by_xpath('//*[@id="tel_'+str(i+1)+'"]/a').click()
            tel = driver.find_element_by_xpath('//*[@id="tel_'+str(i+1)+'"]/a').text
            if (tel != ''):
                raisonSociales.append(raison)
                adresses.append(adresse)
                tels.append(tel)
                print(driver.find_element_by_xpath('//*[@id="tel_' + str(i + 1) + '"]/a').text)
            else :
                print('null')

        except:
            print('null')

    #affiche numero de page*
    try:
        if ( pageActuel == driver.find_element_by_class_name('adp-current-page').text):
            print('fin')
            pageContinuer = False
        else :
            print(driver.find_element_by_class_name('adp-current-page').text)
            pageActuel = driver.find_element_by_class_name('adp-current-page').text
            nextBtn = driver.find_element_by_xpath('//*[@class="adp-icon adp-icon--chevron-droit"]')
            time.sleep(1)
            nextBtn.click()
    except:
        print('fin')
        pageContinuer = False

#Mise en forme du tableau
test = pd.DataFrame({
    'Raison Sociale' : raisonSociales,
    'Adresses' : adresses,
    'Telephone' : tels

})
print(test)
#Creation de fichier csv contenant les donnees scrapees
test.to_csv(metier+departement+'ViteDepan.csv',sep="|", encoding = 'iso-8859-1')
