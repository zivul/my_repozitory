from conftest import *

class TestResult:
    def test_apt(self, set_up):
        driver = set_up
        driver.get('https://apteka-altay.ru/')
        el = driver.find_element(By.XPATH, '//*[text()="Товары по назначению"]').text
        assert el == 'Товары по назначению'


    def test_apt_2(self, set_up):
        driver = set_up
        driver.get('https://apteka-altay.ru/zhivica')
        el2 = driver.find_elements(By.CLASS_NAME, 'product-thumb')
        assert len(el2) == 15
