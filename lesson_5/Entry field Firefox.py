from selenium import webdriver

# Пути к драйверам 
firefox_driver_path = "geckodriver"

# Создание экземпляров 
firefox_options = webdriver.FirefoxOptions()
firefox_options.add_argument("--start-maximized")
firefox_driver = webdriver.Firefox(executable_path=firefox_driver_path, options=firefox_options)

# Открытие страницы 
url = "http://the-internet.herokuapp.com/inputs"
firefox_driver.get(url)

# Определение локатора поля ввода
input_locator = "input[type='number']"

# Ввод значения в поле 
firefox_input_field = firefox_driver.find_element_by_css_selector(input_locator)
firefox_input_field.send_keys("1000")

# Очистка поля ввода в обоих браузерах
firefox_input_field.clear()

# Ввод нового значения в обоих браузерах
firefox_input_field.send_keys("999")

# Закрытие браузера
firefox_driver.quit()
