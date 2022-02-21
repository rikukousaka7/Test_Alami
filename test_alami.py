import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
import time

class TestAlami(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()

    def test_searchBox(self): 

        driver = self.driver 

        driver.get("https://www.elevenia.co.id/")
        time.sleep(2)
        driver.find_element_by_xpath("/html/body/header/div[2]/div/div[2]/form/div/input").click()
		driver.find_element_by_xpath("/html/body/header/div[2]/div/div[2]/form/div/input").send_keys("komputer")
        driver.find_element_by_xpath("/html/body/header/div[2]/div/div[2]/form/div/button").click()
        time.sleep(3)
		
	def test_chooseProduct(self): 

        driver = self.driver 
		
		time.sleep(2)
        driver.find_element_by_xpath("/html/body/section/section/article[2]/div[1]/div[1]/div[1]/ul/li[2]/a").click()
		driver.find_element_by_xpath("/html/body/section/section/article[2]/div[1]/div[2]/ul/ul[1]/li[1]/div/a[2]").click()
		time.sleep(3)
		
	def test_addCart(self): 

        driver = self.driver 
		
		time.sleep(2)
        driver.find_element_by_xpath("/html/body/section/section/form[1]/div[1]/div[3]/div[3]/div/ul[2]/li/div/div/button[2]").click()
		driver.find_element_by_xpath("/html/body/section/section/form[1]/div[1]/div[3]/div[3]/div/ul[2]/li/div/div/button[2]").click()
		driver.find_element_by_xpath("/html/body/section/section/form[1]/div[1]/div[4]/div[1]/div[1]/div/div/div[2]/select").click()
		driver.find_element_by_xpath("/html/body/section/section/form[1]/div[1]/div[4]/div[1]/div[1]/div/div/div[2]/select/option[2]").click()
		driver.find_element_by_xpath("/html/body/section/section/form[1]/div[1]/div[3]/div[6]/a[1]").click()
		
		time.sleep(3)
		
		yes = driver.find_elements_by_xpath("/html/body/section/section/form[1]/div[1]/div[3]/div[6]/div[2]/div[2]/a[1]")
		cart = driver.find_elements_by_xpath("/html/body/header/div[1]/div/div/div[2]/ul/li[4]/a")
		if yes.is_displayed():
			yes.click()
		else
			cart.click()
		
	def test_Cart(self): 

        driver = self.driver 
		
		time.sleep(2)
        driver.find_element_by_xpath("/html/body/div[2]/section[1]/article/form/table/tbody/tr/td[6]/a[1]").click()
		driver.find_element_by_xpath("/html/body/section/form/article/p[3]/a[2]").click()
		driver.find_element_by_xpath("/html/body/div[2]/section[1]/article/form/table/tbody/tr/td[7]/a[2]").click()
		driver.find_element_by_xpath("/html/body/div[2]/section[1]/div[2]/div/section/article/p/span[2]/a").click()
		
		time.sleep(3)


    def tearDown(self): 
        self.driver.close() 

if __name__ == "__main__": 
    unittest.main() 