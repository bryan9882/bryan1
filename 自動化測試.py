

from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
import time
# from selenium.webdriver.common.action_chains import ActionChains

options = webdriver.ChromeOptions()

# options.add_argument('window-size=375x667') #设置浏览器分辨率
options.add_argument('--disable-gpu') #规避Google bug
options.add_argument(     
    '--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
        AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36') #设定最新ua
PATH = "C:/Users/bryan/OneDrive/桌面/chromedriver-win64/chromedriver.exe"

driver = webdriver.Chrome(executable_path=PATH,options=options)

driver.set_window_size(375, 667)
driver.get("https://www.cathaybk.com.tw/cathaybk/")

time.sleep(0.5)

# driver.save_screenshot("screenshot-Cathay.png")

menu = driver.find_elements_by_xpath("/html/body/div[1]/header/div/div[1]")[0].click()
product_intro = driver.find_elements_by_xpath("/html/body/div[1]/header/div/div[3]/div/div[2]/div[1]/div/div[1]/div[1]")[0].click()
credit_card = driver.find_element_by_xpath("/html/body/div[1]/header/div/div[3]/div/div[2]/div[1]/div/div[1]/div[2]/div/div[1]/div[1]/div").click()
titles = driver.find_elements_by_xpath("/html/body/div[1]/header/div/div[3]/div/div[2]/div[1]/div/div[1]/div[2]/div/div[1]/div[2]/a")


print(len(titles))
for title in  titles:
   print(title.text)
   



# actions = ActionChains(driver)
# actions.click(menu)
# actions.performs()

# driver.quit()











# print(driver.title)
# #search = driver.find_element_by_name("query")
# #search.send_keys("比特幣") #搜尋欄打字
# #search.send_keys(Keys.RETURN) #搜尋欄搜尋
# titles = driver.find_elements_by_class_name("atm_cs_1urozh") #找到目標的Class_name
# for title in titles:
#     print(title.text)   
# link = driver.find.element_by_link_text("2023洛杉磯冠軍賽🏆有獎應援活動徵起來✨")    
# link.click()
# time.sleep(5)
# driver.quit()