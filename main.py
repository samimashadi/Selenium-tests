
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from chromedriver_py import binary_path

driver = webdriver.Chrome(executable_path=binary_path)


url = 'https://www.python.org/'
driver.get(url)

search = driver.find_element_by_name("q")
search.send_keys("pycon")
search.send_keys(Keys.RETURN)







