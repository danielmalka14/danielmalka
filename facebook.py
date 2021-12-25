from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
chrome_driver = webdriver.Chrome(executable_path=r"c:\users\daniel.malka\downloads\chromedriver_win32\chromedriver.exe")
chrome_driver.get("https://www.facebook.com/")
chrome_driver.find_element(By.ID,value='email').send_keys("danielma1412@gmail.com")
chrome_driver.find_element(By.ID,value='pass').send_keys("password")
chrome_driver.find_element(By.NAME,value='login').click()