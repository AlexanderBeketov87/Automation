from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Пути к драйверам браузера
firefox_driver_path = "geckodriver"


firefox_options = webdriver.FirefoxOptions()
firefox_options.add_argument("--start-maximized")
firefox_driver = webdriver.Firefox(executable_path=firefox_driver_path, options=firefox_options)

# Открытие страницы 
url = "http://the-internet.herokuapp.com/entry_ad"
firefox_driver.get(url)

# Определение локатора кнопки Close
close_button_locator = (By.CLASS_NAME, "modal-footer")

# Функция для закрытия модального окна
def close_modal(driver):
    try:
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(close_button_locator)).click()
    except Exception as e:
        print(f"An error occurred: {e}")

# Закрытие модального окна 
close_modal(firefox_driver)

# Закрытие браузера
firefox_driver.quit()
