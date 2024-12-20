import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
import time


username="saad.elkabche@e-polytechnique.ma"
password="S@@delkabche12"




with uc.Chrome() as driver:

    driver.get("https://altissia.org/fr")
    waiter=WebDriverWait(driver=driver,timeout=20)
    
    connexion_btn:WebElement=waiter.until(EC.element_to_be_clickable((By.CLASS_NAME,"Header-login__link__ltWmH")))
    connexion_btn.click()
    
    username_input:WebElement=waiter.until(EC.presence_of_element_located((By.ID,"username")))
    username_input.send_keys(username)

    password_input:WebElement=waiter.until(EC.presence_of_element_located((By.ID,"password")))
    password_input.send_keys(password)

    login_btn:WebElement=waiter.until(EC.element_to_be_clickable((By.XPATH,"(//button)[4]")))
    login_btn.click()

    time.sleep(3)
   

    levels_container:WebElement=waiter.until(EC.presence_of_element_located((By.XPATH,'//*[@id="theme-provider"]/div[1]/main/div/div[1]/div/div[1]/div')))
    levels=levels_container.find_elements(By.XPATH,"./*")
    print(f"================================={len(levels)}")
    while True:
        for level in levels:
            level.click()
            buttons=waiter.until(EC.presence_of_all_elements_located((By.XPATH,'//button[@data-test="mission-button"]')))
            for index,modul in enumerate(buttons):
                time.sleep(3)
                modul.click()
                time.sleep(3)
                driver.back()
            time.sleep(5)
        

        

        




