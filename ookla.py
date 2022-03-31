from selenium.webdriver.common.by import By
import time


class Ookla:
    def __init__(self, driver):
        self.driver = driver

    def test_speed(self):
        self.driver.get("https://www.speedtest.net/")
        time.sleep(1)

        self.driver.find_element(By.ID, '_evidon-banner-acceptbutton').click()
        time.sleep(1)

        self.driver.execute_script("window.scrollTo(0, 400)")
        time.sleep(1)

        self.driver.find_element(By.CSS_SELECTOR, ".start-button a").click()

        time.sleep(40)

        down_speed = float(self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text)
        print(down_speed)
        # down_speed = 420
        return down_speed
