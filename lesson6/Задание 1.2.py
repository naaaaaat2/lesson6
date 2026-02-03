from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
try:
    driver.get("http://uitestingplayground.com/textinput")
    wait = WebDriverWait(driver, 10)

    # Вводим в поле "SkyPro"
    input_field = wait.until(
        EC.element_to_be_clickable((By.ID, "newButtonName"))
    )
    input_field.clear()
    input_field.send_keys("SkyPro")

    # Нажимаем на кнопку
    button = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn-primary"))
    )
    button.click()

    # Получаем текст кнопки и выводим
    button_text = button.text
    print(f'"{button_text}"')
finally:
    driver.quit()
