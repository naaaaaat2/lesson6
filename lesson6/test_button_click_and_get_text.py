from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()  # или другой драйвер
try:
    driver.get("http://uitestingplayground.com/ajax")
    wait = WebDriverWait(driver, 10)

    # Нажимаем на синюю кнопку
    button = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn-primary"))
    )
    button.click()

    # Ждем появления зеленой плашки и получаем её текст
    success_msg = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "div#content span"))
    ).text

    # Выводим сообщение в консоль
    print("Data loaded with AJAX get request.")
finally:
    driver.quit()
