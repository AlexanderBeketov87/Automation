from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

chrome_driver_path = "chromedriver"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")  # Открыть окно браузера в максимал
chrome_driver = webdriver.Chrome(executable_path=chrome_driver_path, options=chrome_options)

# Открытие страницы 
url = "http://uitestingplayground.com/classattr"
chrome_driver.get(url)

# Определение локатора кнопки с CSS-классом
button_locator = (By.CSS_SELECTOR, ".button-blue")

# Функция для клика на кнопку
def click_button(driver):
    button = driver.find_element(*button_locator)
    button.click()

# Проведение кликов три раза 
for _ in range(3):
    click_button(chrome_driver)
    time.sleep(1)  # Пауза для визуальной проверки

# Закрытие браузера
chrome_driver.quit()