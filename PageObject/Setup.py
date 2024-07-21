from selenium.webdriver.common.by import By


class SetupFilter:

    def __init__(self, driver):
        self.driver = driver

    login = (By.ID, "loginHref")
    username = (By.ID, "login")
    password = (By.ID, "password")
    click_button = (By.ID, "go")
    Sampling_info = (By.XPATH, "//span[contains(text(),'Sampling')]")
    sampling_setup = (By.XPATH, "//div[.='Sampling Setup']")
    Quarter = (By.NAME, "QUARTER")
    Quarter_dropdown = (By.ID, "id12")
    Year = (By.NAME, "SAMPLING_YEAR")
    Year_dropdown = (By.ID, "id13")
    Round1 = (By.ID, "id17")
    Round2 = (By.ID, "id18")
    Round3 = (By.ID, "id19")
    HRR_Round1 = (By.ID, "id20")
    HRR_Round2 = (By.ID, "id21")
    HRR_Round3 = (By.ID, "id22")
    Enable_Grade_E = (By.NAME, "ENABLE_GRADE_E")
    Enable_Grade_E_dropdown = (By.ID, "id23")
    Grade_E_Round1 = (By.ID, "id24")
    Grade_E_Round2 = (By.ID, "id25")
    Grade_E_Round3 = (By.ID, "id26")
    Sampling_start_date =(By.NAME, "SAMPLING_DATE_COUNT")
    Persistency_Ratio = (By.ID, "id28")
    DistRep_Status = (By.ID, "search_name")
    Transaction_Type = (By.ID, "search_name")
    Benefit_Status =(By.ID, "id32")

    def loginPage(self):
        return self.driver.find_element(*SetupFilter.login)
        # self.driver.find_element(By.ID, "loginHref").click()

    def Username(self):
        return self.driver.find_element(*SetupFilter.username)

    def Password(self):
        return self.driver.find_element(*SetupFilter.password)

    def go(self):
        return self.driver.find_element(*SetupFilter.click_button)

    def Sampling_infocenter(self):
        return self.driver.find_element(*SetupFilter.Sampling_info)

    def sampling_setup_fun(self):
        return self.driver.find_element(*SetupFilter.sampling_setup)

    def quarter(self):
        return self.driver.find_element(*SetupFilter.Quarter)

    def quarter_drop(self):
        return self.driver.find_element(*SetupFilter.Quarter_dropdown)

    def year(self):
        return self.driver.find_element(*SetupFilter.Year)

    def year_dropdown(self):
        return self.driver.find_element(*SetupFilter.Year_dropdown)

    def round1(self):
        return self.driver.find_element(*SetupFilter.Round1)

    def round2(self):
        return self.driver.find_element(*SetupFilter.Round2)

    def round3(self):
        return self.driver.find_element(*SetupFilter.Round3)

    def hrr_round1(self):
        return self.driver.find_element(*SetupFilter.HRR_Round1)

    def hrr_round2(self):
        return self.driver.find_element(*SetupFilter.HRR_Round2)

    def hrr_round3(self):
        return self.driver.find_element(*SetupFilter.HRR_Round3)

    def Enable_Grade_E_fun(self):
        return self.driver.find_element(*SetupFilter.Enable_Grade_E)

    def Enable_Grade_E_dropdown_fun(self):
        return self.driver.find_element(*SetupFilter.Enable_Grade_E_dropdown)

    def Grade_E_Round1_fun(self):
        return self.driver.find_element(*SetupFilter.Grade_E_Round1)

    def Grade_E_Round2_fun(self):
        return self.driver.find_element(*SetupFilter.Grade_E_Round2)

    def Grade_E_Round3_fun(self):
        return self.driver.find_element(*SetupFilter.Grade_E_Round3)

    def Sampling_start_date_fun(self):
        return self.driver.find_element(*SetupFilter.Sampling_start_date)

    def Persistency_Ratio_fun(self):
        return  self.driver.find_element(*SetupFilter.Persistency_Ratio)

    def DistRep_Status_fun(self):
        return self.driver.find_element(*SetupFilter.DistRep_Status)

    def Transaction_Type_fun(self):
        return self.driver.find_element(*SetupFilter.Transaction_Type)

    def Benefit_Status_fun(self):
        return self.driver.find_element(*SetupFilter.Benefit_Status)