from selenium.webdriver.common.by import By


class SignIn:

    def __init__(self, driver):
        self.driver = driver

    userfield = (By.ID, "email")
    pwdfield = (By.ID, "passwd")
    submit = (By.ID, "SubmitLogin")
    homepagebutton = (By.XPATH, "//div/a/img[@alt='My Store']")

    def user_field(self):
        return self.driver.find_element(*SignIn.userfield)

    def pwd_field(self):
        return self.driver.find_element(*SignIn.pwdfield)

    def sub_mit(self):
        return self.driver.find_element(*SignIn.submit)

    def homepage_button(self):
        return self.driver.find_element(*SignIn.homepagebutton)