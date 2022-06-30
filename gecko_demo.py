import os
from time import sleep
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class GoogleLoginTestCase(unittest.TestCase):
    """This is a test-case class for GMAIL Inbox"""

    def setUp(self):
        # Create a new Firefox session
        geckodriver_path = '{}'.format(os.path.realpath('geckodriver'))
        self.browser = webdriver.Firefox(executable_path=geckodriver_path)
        # Get GMAIL Webpage
        self.browser.get('https://www.gmail.com')
        self.browser.implicitly_wait(10)

    def test_get_gmail_primary_inbox(self):
        """Test scenario for gmail inbox"""
        # Find username input and send some keys
        self.username = self.browser.find_element_by_id("identifierId")
        self.username.send_keys("") # Input Gmail username
        # Press enter
        self.username.send_keys(Keys.RETURN)
        # Find password input and send some keys
        self.password = self.browser.find_element_by_name("password")
        self.password.send_keys("") # Input Gmail password
        # Press enter
        self.password.send_keys(Keys.RETURN)
        # Find Primary section of emails
        self.primary_inbox = self.browser.find_element_by_partial_link_text('https://mail.google.com/mail/u/0/#inbox')
        if self.primary_inbox.get_attribute("tabindex") is not "0":
            self.primary_inbox.click()
        # Find the count od primary email
        self.count_primary_email = self.browser.find_element_by_xpath('//span[a[@href="https://mail.google.com/mail/u/0/#inbox"]]/following-sibling::div')
        # Print the count
        print(self.count_primary_email.get_attribute("innerHTML"))
        # Get the NTH email of the inbox
        self.nth_email_sender = self.browser.find_elements_by_class_name("zF")
        self.nth_email_subject = self.browser.find_elements_by_class_name("bqe")
        print('Sender: {}, Subject: {}'.format(self.nth_email_sender[0].get_attribute('name'), self.nth_email_subject[0].get_attribute("innerHTML")))

    def test_get_all_senders_and_subjects(self):
        """Test scenario for getting all sender and subjects from primary inbox"""
        self.email_senders = self.browser.find_elements_by_class_name("zF")
        self.email_subjects = self.browser.find_elements_by_class_name("bqe")
        for index, sender in enumerate(self.email_senders, start=0):
            print('Sender: {}, Subject: {}'.format(sender.get_attribute('name'), self.nth_email_subject[index].get_attribute("innerHTML")))

    def tearDown(self):
        self.browser.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)