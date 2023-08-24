import pickle
import selenium.webdriver

driver = selenium.webdriver.Firefox()
driver.get("https://bard.google.com/")
pickle.dump( driver.get_cookies() , open("cookies.pkl","wb"))