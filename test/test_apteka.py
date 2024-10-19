from conftest import *


class TestOnly:
    def test_footer(self, set_up):
        driver = set_up
        driver.get('https://only.digital/')
        try:
            driver.find_element(By.XPATH, '//footer')
            print("Element found")
        except NoSuchElementException:
            print("No element found")

    def test_footer_project(self, set_up):
        driver = set_up
        driver.get('https://only.digital/projects')
        try:
            driver.find_element(By.XPATH, '//footer')
            print("Element found")
        except NoSuchElementException:
            print("No element found")

    def test_footer_el1(self, set_up):
        driver = set_up
        driver.get('https://only.digital/')
        try:
            driver.find_element(By.XPATH, '//p[@class="sc-222969c7-1 eNylzl"]')
            print("Element found")
        except NoSuchElementException:
            print("No element found")

    def test_footer_el2(self, set_up):
        driver = set_up
        driver.get('https://only.digital/')
        el = driver.find_element(By.XPATH, '(//a[@rel="noreferrer"])[7]')
        assert '' == el.text

    def test_footer_el3(self, set_up):
        driver = set_up
        driver.get('https://only.digital/')
        el = driver.find_element(By.XPATH, "(//span[contains(text(), 'Awwwards')])[2]").text
        assert el == ''

    def test_footer_el4(self, set_up):
        driver = set_up
        driver.get('https://only.digital/')
        try:
            driver.find_element(By.XPATH, "(//span[contains(text(), 'Awwwards')])[2]")
            print("Element found")
        except NoSuchElementException:
            print("No element found")







