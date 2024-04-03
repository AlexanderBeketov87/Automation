from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Пути к драйверам браузера
chrome_driver_path = "chromedriver"

# Создание экземпляров драйверов 
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")  # Открыть окно браузера в максимальном размере
chrome_driver = webdriver.Chrome(executable_path=chrome_driver_path, options=chrome_options)


# Открытие страницы 
url = "http://the-internet.herokuapp.com/entry_ad"
chrome_driver.get(url)

# Определение локатора кнопки Close
close_button_locator = (By.CLASS_NAME, "modal-footer")

# Функция для закрытия модального окна
def close_modal(driver):
    try:
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(close_button_locator)).click()
    except Exception as e:
        print(f"An error occurred: {e}")

# Закрытие модального окна 
close_modal(chrome_driver)

# Закрытие браузера
chrome_driver.quit()

