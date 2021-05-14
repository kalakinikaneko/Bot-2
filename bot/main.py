from selenium import webdriver

PATH = "/Users/kalakinikaneko/Desktop/chromedriver"
driver = webdriver.Chrome(PATH)
driver.get("https://youtube.com")