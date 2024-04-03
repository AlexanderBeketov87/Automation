from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

firefox_driver_path = "geckodriver"

firefox_options = webdriver.FirefoxOptions()
firefox_options.add_argument("--start-maximized")
firefox_driver = webdriver.Firefox(executable_path=firefox_driver_path, options=firefox_options)

# Открытие страницы 
url = "http://uitestingplayground.com/classattr"
firefox_driver.get(url)

# Определение локатора кнопки с CSS-классом
button_locator = (By.CSS_SELECTOR, ".button-blue")

# Функция для клика на кнопку
def click_button(driver):
    button = driver.find_element(*button_locator)
    button.click()

# Проведение кликов три раза 
for _ in range(3):
    click_button(firefox_driver)
    time.sleep(1)  

# Закрытие браузера
firefox_driver.quit()
