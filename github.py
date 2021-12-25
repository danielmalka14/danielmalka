from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
chrome_driver = webdriver.Chrome(executable_path=r"c:\users\daniel.malka\downloads\chromedriver_win32\chromedriver.exe")
chrome_driver.get("https://github.com/")
chrome_driver.find_element(By.NAME,value='q').send_keys("selenium")
chrome_driver.find_element(By.XPATH,value='/html/body/div[1]/header/div/div[2]/div[2]/div[1]/div/div/form/label/input[1]').send_keys(Keys.ENTER)