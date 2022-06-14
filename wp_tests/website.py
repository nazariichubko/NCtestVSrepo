import os
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import NCtestVSrepo.wp_tests.constants as constant
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class TestWebsite(webdriver.Chrome):
    def __init__(self, driver_path=r"c:\Users\nazar\git\NCtestVSrepo\NCtestVSrepo\Local_website", teardown=False):
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ['PATH'] += self.driver_path
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        super(TestWebsite, self).__init__(options=options)
        self.implicitly_wait(constant.w)
        self.maximize_window()

    # Open a webpage

    def navigate_to_homepage(self):
        self.get("http://localhost/wp-test/")

    # Open a custom page
    def navigate_to_custom_page(self):
        self.get("http://localhost/wp-test/site/")

    # Define form fields variables.
    def fill_contact_form(self):
        first_name = self.find_element(By.ID, 'field_dp46a_first')
        last_name = self.find_element(By.ID, 'field_dp46a_last')
        email = self.find_element(By.ID, 'field_j3yjg')
        phone = self.find_element(By.ID, 'field_qbnam')
        #      text_field = driver.find_element(By.ID, 'field_uot6f_label')

        # send values to form fields

        first_name.send_keys("Testonww1")
        last_name.send_keys("Testerqq1")
        email.send_keys("nchubko.forte1@gmail1.com")
        phone.send_keys("097234543002")

    # text_field.send_keys("example text to sent into database")

    # Click Submit button
    def submit_form(self):
        submit_btn = self.find_element(By.CLASS_NAME, 'frm_button_submit')
        submit_btn.click()
# Check if success message is present on the page
    def check_contact_form_submission_success_message(self):
        WebDriverWait(self, 30).until(
            EC.text_to_be_present_in_element(
                (By.ID, 'frm_form_2_container'),  # Element filtaration
                    'Your responses were successfully submitted. Thank you!'  # Expected text
                )
            )
        return print("Success.")
# navigate to wordpress login page
    def navigate_to_login_page(self):
        self.get("http://localhost/wp-test/wp-login.php")
# Enter test user credentials at the login page
    def enter_credentials(self, username, password):
        self.find_element(By.ID, "user_login").send_keys(username)
        self.find_element(By.ID, "user_pass").send_keys(password)
        self.find_element(By.ID, "wp-submit").click()

#========================================================================
# navigate to user's registration page
    def navigate_to_registration_page(self):
        self.get("http://localhost/wp-test/register/")
# submit registration form
    def fill_registration_form(self):
        self.find_element(By.ID,"user_firstname").send_keys(constant.testuser1_username)
        self.find_element(By.ID, "user_lastname").send_keys(constant.testuser1_lastname)
        self.find_element(By.ID, "user_email").send_keys(constant.testuser1_email)
        self.find_element(By.ID, "user_password").send_keys(constant.testuser1_password)
        self.find_element(By.ID, "privacy").click()
        self.find_element(By.XPATH, "//input[@name = 'submit_registration' and @value = 'Register']").click()

# check if user has been successfully registered.
    def verify_user_registration_is_successfull(self):
        WebDriverWait(self, 30).until(
            EC.text_to_be_present_in_element(
                (By.XPATH, "//div[@class = 'wpum-message success']"),  # Element filtaration
                'Registration complete. We have sent you a confirmation email with your details.'  # Expected text
            )
        )
        return print("Success.")

# Navigate to Registration page
    def navigate_to_users_login_page(self):
        self.get("http://localhost/wp-test/log-in/")
        assert True

# Enter registration data and submit form
    def enter_registered_user_credentials(self):
        self.find_element(By.ID,"username").send_keys(constant.testuser1_email)
        self.find_element(By.ID, "password").send_keys(constant.testuser1_password)
        self.find_element(By.XPATH, "//input[@type = 'submit' and @value = 'Login']").click()

# Verify user logged in to the website.
    def verify_user_is_logged_in_successfully(self):
        WebDriverWait(self, 30).until(
            EC.text_to_be_present_in_element(
                (By.XPATH, "//a[@class = 'ab-item' and @aria-haspopup = 'true']/span[@class = 'display-name']"),  # Element filtaration
                constant.testuser1_email  # Expected text
            )
        )
        return print("Success.")

# Logout form user's account
    def log_out_from_account(self):
        users_menu = self.find_element(By.CSS_SELECTOR, 'a[href = "http://localhost/wp-test/wp-admin/profile.php"]')
        logout_button  = self.find_element(By.XPATH, "//li[@id  = 'wp-admin-bar-logout']/a[@class = 'ab-item']")
        ActionChains(self).move_to_element(users_menu).click(logout_button).perform()
        logout_button.click()


