from selenium.webdriver.common.by import By


class FooterSection:

    def __init__(self, driver):
        self.driver = driver

    footermenu = (By.CSS_SELECTOR, "section[class*='footer'] h4")
    footercateg = (By.XPATH, "//*[contains(@class, 'footer')]/h4[text()='Categories']/parent::section/div/div/ul/li/a")
    footerinfo = (By.XPATH, "//*[contains(@class, 'footer')]/h4[text()='Information']/parent::section/ul/li")
    footeracc = (By.XPATH, "//*[contains(@class, 'footer')]/h4/a/parent::h4/parent::section/div/ul/li")
    women = (By.XPATH, "//*[contains(@class, 'footer')]/h4[text()='Categories']/parent::section/div/div/ul/li/a")
    specials = (By.XPATH, "//*[contains(@class, 'footer')]/h4[text()='Information']/parent::section/ul/li/a[@title='Specials']")
    newproducts = (By.XPATH, "//*[contains(@class, 'footer')]/h4[text()='Information']/parent::section/ul/li/a[@title='New products']")
    bestsellers = (By.XPATH, "//*[contains(@class, 'footer')]/h4[text()='Information']/parent::section/ul/li/a[@title='Best sellers']")
    ourstores = (By.XPATH, "//*[contains(@class, 'footer')]/h4[text()='Information']/parent::section/ul/li/a[@title='Our stores']")
    contactus = (By.XPATH, "//*[contains(@class, 'footer')]/h4[text()='Information']/parent::section/ul/li/a[@title='Contact us']")
    termsconditions = (By.XPATH, "//*[contains(@class, 'footer')]/h4[text()='Information']/parent::section/ul/li/a[@title='Terms and conditions of use']")
    aboutus = (By.XPATH, "//*[contains(@class, 'footer')]/h4[text()='Information']/parent::section/ul/li/a[@title='About us']")
    sitemap = (By.XPATH, "//*[contains(@class, 'footer')]/h4[text()='Information']/parent::section/ul/li/a[@title='Sitemap']")
    myorders = (By.XPATH, "//*[contains(@class, 'footer')]/h4/a/parent::h4/parent::section/div/ul/li/a[@title='My orders']")
    creditslips = (By.XPATH, "//*[contains(@class, 'footer')]/h4/a/parent::h4/parent::section/div/ul/li/a[@title='My credit slips']")
    myaddress = (By.XPATH, "//*[contains(@class, 'footer')]/h4/a/parent::h4/parent::section/div/ul/li/a[@title='My addresses']")
    personalinfo = (By.XPATH, "//*[contains(@class, 'footer')]/h4/a/parent::h4/parent::section/div/ul/li/a[@title='Manage my personal information']")
    signout = (By.XPATH, "//*[contains(@class, 'footer')]/h4/a/parent::h4/parent::section/div/ul/li/a[@title='Sign out']")

    def footer_menu(self):
        return self.driver.find_elements(*FooterSection.footermenu)

    def footer_category(self):
        return self.driver.find_element(*FooterSection.footercateg)

    def footer_info(self):
        return self.driver.find_elements(*FooterSection.footerinfo)

    def footer_acc(self):
        return self.driver.find_elements(*FooterSection.footeracc)

    def wo_men(self):
        return self.driver.find_element(*FooterSection.women)

    def spec_ial(self):
        return self.driver.find_element(*FooterSection.specials)

    def new_products(self):
        return self.driver.find_element(*FooterSection.newproducts)

    def best_sellers(self):
        return self.driver.find_element(*FooterSection.bestsellers)

    def our_stores(self):
        return self.driver.find_element(*FooterSection.ourstores)

    def contact_us(self):
        return self.driver.find_element(*FooterSection.contactus)

    def terms_conditions(self):
        return self.driver.find_element(*FooterSection.termsconditions)

    def about_us(self):
        return self.driver.find_element(*FooterSection.aboutus)

    def site_map(self):
        return self.driver.find_element(*FooterSection.sitemap)

    def my_orders(self):
        return self.driver.find_element(*FooterSection.myorders)

    def credit_slip(self):
        return self.driver.find_element(*FooterSection.creditslips)

    def my_address(self):
        return self.driver.find_element(*FooterSection.myaddress)

    def personal_info(self):
        return self.driver.find_element(*FooterSection.personalinfo)

    def sign_out(self):
        return self.driver.find_element(*FooterSection.signout)