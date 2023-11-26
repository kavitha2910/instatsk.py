import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.instagram.com/guviofficial/")
driver.maximize_window()
driver.implicitly_wait(10)
driver.find_element(By.XPATH,"//span[@aria-label='Close']").click()
followers=driver.find_element(By.XPATH,"//header[@class='x1qjc9v5 x78zum5 x1q0g3np x2lah0s x1n2onr6 x1qsaojo xc2v4qs x1xl8k2i x1ez9qw7 x1kcpa7z']//li[2]//button[1]")
following=driver.find_element(By.XPATH,"//header[@class='x1qjc9v5 x78zum5 x1q0g3np x2lah0s x1n2onr6 x1qsaojo xc2v4qs x1xl8k2i x1ez9qw7 x1kcpa7z']//li[3]//button[1]")                        

followers_count = followers.text
following_count = following.text
print("Following: " + following_count)
print("Followers: " + followers_count)
driver.close()






