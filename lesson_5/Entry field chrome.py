from selenium import webdriver

# Пути к драйверам 
chrome_driver_path = "chromedriver"

# Создание экземпляров драйверов 
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")  # Открыть окно браузера в максимальном размере
chrome_driver = webdriver.Chrome(executable_path=chrome_driver_path, options=chrome_options)


# Открытие страницы 
url = "http://the-internet.herokuapp.com/inputs"
chrome_driver.get(url)

# Определение локатора поля ввода
input_locator = "input[type='number']"

# Ввод значения в поле 
chrome_input_field = chrome_driver.find_element_by_css_selector(input_locator)
chrome_input_field.send_keys("1000")

# Очистка поля ввода 
chrome_input_field.clear()

# Ввод нового значения 
chrome_input_field.send_keys("999")

# Закрытие браузера
chrome_driver.quit()
