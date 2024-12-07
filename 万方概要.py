# -*- coding: gb18030 -*-
def gy(url):

    from time import sleep
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.relative_locator import locate_with
    import csv

    # ���������ѡ��
    option = webdriver.EdgeOptions()
    option.add_experimental_option("detach", True)
    driver = webdriver.Edge(options=option)
 
    # Ŀ��url
    url = f"https://d.wanfangdata.com.cn/conference/{url}"#����
    driver.get(url=url)
    sleep(3)

    try:
        #��λ�����
        element = driver.find_element(By.CLASS_NAME,("btn"))
        element.click()
    except:

        #��λ�ı�
        element1 = driver.find_element(By.XPATH,'//*[@class="summary list"]//span[2]/span/span[1]')
    else:
        element1 = driver.find_element(By.XPATH,'//*[@class="summary list"]//span[2]/span/span[1]')
    #д��
    with open("gy.csv","a",newline="") as file:
            writer = csv.writer(file)
            writer.writerow([element1.get_attribute('innerHTML')])

    driver.close()

import csv

with open("url.csv","r") as file:
                csv_reader = csv.reader(file)
                for a in csv_reader:
                    gy(a[0])#�����б�

print("over!")