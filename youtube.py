from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
chrome_driver = webdriver.Chrome(executable_path=r"c:\users\daniel.malka\downloads\chromedriver_win32\chromedriver.exe")
chrome_driver.get("https://www.youtube.com/")
chrome_driver.find_element_by_name('search_query').send_keys("Matrix Awakens")
chrome_driver.find_element(By.CLASS_NAME,value='style-scope ytd-searchbox').send_keys(Keys.ENTER)