import time

import data
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


# no modificar
def retrieve_phone_code(driver) -> str:
    """Este código devuelve un número de confirmación de teléfono y lo devuelve como un string.
    Utilízalo cuando la aplicación espere el código de confirmación para pasarlo a tus pruebas.
    El código de confirmación del teléfono solo se puede obtener después de haberlo solicitado en la aplicación."""

    import json
    import time
    from selenium.common import WebDriverException
    code = None
    for i in range(10):
        try:
            logs = [log["message"] for log in driver.get_log('performance') if log.get("message")
                    and 'api/v1/number?number' in log.get("message")]
            for log in reversed(logs):
                message_data = json.loads(log)["message"]
                body = driver.execute_cdp_cmd('Network.getResponseBody',
                                              {'requestId': message_data["params"]["requestId"]})
                code = ''.join([x for x in body['body'] if x.isdigit()])
        except WebDriverException:
            time.sleep(1)
            continue
        if not code:
            raise Exception("No se encontró el código de confirmación del teléfono.\n"
                            "Utiliza 'retrieve_phone_code' solo después de haber solicitado el código en tu aplicación.")
        return code


class UrbanRoutesPage:
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')

    call_taxi_button = (By.CLASS_NAME, "button round")
    Comfort_button = (By.XPATH, "//*[@id='root'] /div /div[3] / div[3] / div[2] / div[1] / div[5] / div[2]")
    phone_number_button = (By.CLASS_NAME, "np-text")
    phone_input = (By.ID, "phone")
    phone_send = (By.XPATH, "//*[@id='rest'] / div / [div1] / [div2] / [div1] / form / div[2] / button")
    pay_method = (By.CLASS_NAME, "pp-text")
    add_card_button = (By.CLASS_NAME, "pp-title")
    add_card = (By.XPATH, "//*[text() = 'Agregar Tarjeta']")
    add_card_data = (By.ID, "number")
    cvv = (By.XPATH, "//*[@id='code']")


    def __init__(self, driver):
        self.driver = webdriver.Chrome()

    def set_from(self, address_from):
        self.driver.find_element(*self.from_field).send_keys(data.address_from)

    def set_to(self, address_to):
        self.driver.find_element(*self.to_field).send_keys(data.address_to)

    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')

    def set_route(self, address_from, address_to):
        self.set_from(address_from)
        self.set_to(address_to)



    def comfort_button_req(self):
        time.sleep(2)
        self.driver.find_element(*self.call_taxi_button).click()
        time.sleep(2)
        self.driver.find_element(*self.Comfort_button).click()

    def phone_number_req(self):
        self.driver.find_element(*self.phone_number_button).click()

    def phone_number_fill(self):
        self.driver.find_element(*self.phone_input).click()

    def phone_number_send(self):
        self.driver.find_element(*self.phone_send).click()


    def pay_method_req(self):
        self.driver.find_element(*self.pay_method).click()

    def add_card_req(self):
        self.driver.find_element(*self.add_card_button).click()

    def add_card_fill(self):
        self.driver.find_element(*self.add_card).click()

    def add_card_numbers(self):
        self.driver.find_element(*self.add_card_data).click()

    def cvv_add(self):
        self.driver.find_element(*self.add_card_data, *self.cvv).send_keys(data.card_number, data.card_code)




class TestUrbanRoutes:

    driver = None

    message_driver = (By.XPATH, "//*[@id='comment']")
    message_send = (By.CSS_SELECTOR, "Comment")
    request_button = (By.CLASS_NAME, "reqs-head")
    blanket_handkerchief = (By.CLASS_NAME, "r-sw-label")
    icecream = (By.CLASS_NAME, "r-counter-label")
    taxi_modal = (By.CLASS_NAME, "smart-button-main")


    @classmethod
    def setup_class(cls):
        # no lo modifiques, ya que necesitamos un registro adicional habilitado para recuperar el código de confirmación del teléfono
        from selenium.webdriver import DesiredCapabilities
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = webdriver.Chrome()


    def test_set_route(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        routes_page.set_route(address_from, address_to)
        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to



    @classmethod
    def teardown_class(cls):
        cls.driver.quit()



