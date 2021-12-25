from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
chrome_driver = webdriver.Chrome(executable_path=r"c:\users\daniel.malka\downloads\chromedriver_win32\chromedriver.exe")
chrome_driver.get("https://translate.google.com/")
by_class = chrome_driver.find_element_by_class_name('er8xn')
by_xpath = chrome_driver.find_element(By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[1]/span/span/div/textarea')
by_css = chrome_driver.find_element(By.CSS_SELECTOR, '#yDmH0d > c-wiz > div > div.WFnNle > c-wiz > div.OlSOob > c-wiz > div.ccvoYb > div.AxqVh > div.OPPzxe > c-wiz.rm1UF.UnxENd > span > span > div > textarea')
print(by_class)
print(by_xpath)
print(by_css)