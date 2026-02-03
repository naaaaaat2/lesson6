from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()
try:
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/loading-images.html"
    )
    wait = WebDriverWait(driver, 10)

    # Ждем полной загрузки всех изображений
    wait.until(lambda driver: driver.execute_script(
        "return Array.from(document.images).every(img => img.complete && "
        "img.naturalWidth > 0);"
    ))

    images = driver.find_elements(By.TAG_NAME, "img")

    if len(images) >= 3:
        src_value = images[2].get_attribute("src")
        print(src_value)
    else:
        print("Меня довели, картинок меньше трех.")
finally:
    driver.quit()
