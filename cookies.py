from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
chrome_driver = webdriver.Chrome(executable_path=r"c:\users\daniel.malka\downloads\chromedriver_win32\chromedriver.exe")
chrome_driver.get("https://ksp.co.il/web/")
chrome_driver.delete_all_cookies()
chrome_cookies = chrome_driver.get_cookies()
print(chrome_cookies)