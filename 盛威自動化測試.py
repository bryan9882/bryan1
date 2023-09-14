from selenium import webdriver
import time

options = webdriver.ChromeOptions()
pic = "C:/Users/bryan/OneDrive/桌面/圖片/"#存圖片路徑
PATH = "C:/Users/bryan/OneDrive/桌面/chromedriver-win64/chromedriver.exe"#設定Driver路徑
driver = webdriver.Chrome(executable_path=PATH,options=options)

driver.set_window_size(375, 667)#啟動時是手機的size
driver.get("https://www.cathaybk.com.tw/cathaybk/")#開啟的網站

time.sleep(0.5)#等待加載

driver.save_screenshot(pic+"screenshot-Cathay.png")#截圖

menu = driver.find_elements_by_xpath("/html/body/div[1]/header/div/div[1]")[0].click()
product_intro = driver.find_elements_by_xpath("/html/body/div[1]/header/div/div[3]/div/div[2]/div[1]/div/div[1]/div[1]")[0].click()
credit_card = driver.find_element_by_xpath("/html/body/div[1]/header/div/div[3]/div/div[2]/div[1]/div/div[1]/div[2]/div/div[1]/div[1]/div").click()
titles = driver.find_elements_by_xpath("/html/body/div[1]/header/div/div[3]/div/div[2]/div[1]/div/div[1]/div[2]/div/div[1]/div[2]/a")
time.sleep(0.5)#等待加載                                     
driver.save_screenshot(pic+"screenshot-CreditCard.png")#截圖

print(f"有{len(titles)}個項目在信用卡列表")

card_intro = driver.find_element_by_xpath('//*[@id="lnk_Link"]').click()
   
card_count=0
for i in range(1,40):
    aria_label = driver.find_elements_by_class_name("swiper-pagination-bullet")[i*-1].get_attribute("aria-label")#取aria label
    driver.find_elements_by_class_name("swiper-pagination-bullet")[i*-1].click()
    time.sleep(0.5)
    driver.save_screenshot(pic+f"screenshot-CreditCard{i}.png")
    card_count +=1
    if aria_label == "Go to slide 1" :
        print(f"總共有{card_count}張卡被停發了")
        break
