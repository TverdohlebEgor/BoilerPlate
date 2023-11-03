from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from time import sleep

class Boilerplate_selenium(object):
    def __init__(self,browser="Firefox",debug = True):
        browser_options = []
        if not debug:
            browser_options = Options()
            browser_options.add_argument("--headless")
            browser_options.add_argument("--disable-gpu")

        try:
            if(browser == "Firefox"):self.browser = webdriver.Firefox(options=browser_options)
            elif(browser == "Chrome"):self.browser = webdriver.Chrome(options=browser_options)
            elif(browser == "Edge"):self.browser = webdriver.Edge()
            elif(browser == "Safari"):self.browser = webdriver.Safari(options=browser_options)
        except:
            raise Exception("Browser not found")

    def simple_connect(self,url="http://google.com",timeout = 10):
        self.browser.get(url)
        sleep(timeout)

    def smart_connect(self,url="http://google.com",timeout = 20):
        self.browser.get(url)
        try:
            wait = WebDriverWait(self.browser,timeout)
        except:
            raise Exception("Timeout the page has not been loaded in time")
        wait.until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
        sleep(3)

    def close_connection(self):
        if(self.browser):
            self.browser.close()

    def simple_button_click(self,XPATH):
        button = self.browser.find_element(By.XPATH,XPATH)
        button.click()
        del button
        sleep(1)

    def get_label_text(self,XPATH):
        return self.browser.find_element(By.XPATH,XPATH).text
    
    def get_labels_text(self,XPATH):
        return [label.text for label in  self.browser.find_elements(By.XPATH,XPATH)]

    def get_title_page(self):
        return self.browser.title

    def simple_input(self,input,XPATH):
        self.browser.find_element(By.XPATH,XPATH).send_keys(input)
        sleep(1)
    
    def get_attribute(self,attribute,XPATH):
        return self.browser.find_element(By.XPATH,XPATH).get_attribute(attribute)
        sleep(1)

    def get_attributes(self,attribute,XPATH):
        return [obj.get_attribute(attribute) for obj in self.browser.find_elements(By.XPATH,XPATH)]

    def stupid_scroll_to_bottom(self,max_scrools=30):
        for _ in range(max_scrools):
            self.browser.find_element(By.TAG_NAME,'body').send_keys(Keys.END)
            sleep(1)  # Adjust the sleep duration to control scrolling speed

    def smart_scroll_to_bottom(self):
        lastHeight = self.browser.execute_script("return document.body.scrollHeight")
        while True:
           self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
           sleep(0.5)
           newHeight = self.browser.execute_script("return document.body.scrollHeight")
           if newHeight == lastHeight:
              break
           lastHeight = newHeight

if __name__ == "__main__":
    test = Boilerplate_selenium()
    test.smart_connect("https://www.amazon.it/promotion/psp/A36ZVRQO3N3ABW?ref_=nav_cs_DiscoBar_amazonbasket")
    #test.simple_button_click("/html/body/c-wiz/div/div/div/div[2]/div[1]/div[4]/div[1]/form[1]/div/div/button")
    test.smart_scroll_to_bottom()
    test.close_connection()