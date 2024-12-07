# -*- coding: gb18030 -*-

def url (pages):
    from time import sleep
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    import csv

    # ���������ѡ��
    option = webdriver.EdgeOptions()
    option.add_experimental_option("detach", True)
    driver = webdriver.Edge(options=option)
 
    # Ŀ��url
    key = '����'#�ؼ���
    url = f"https://s.wanfangdata.com.cn/conference?q={key}&s=20&p={pages}"#������ַ(conference)
    driver.get(url=url)

    #��1-20������
    for num in range(1,21):
        #xpath��λ
        sleep(3)
        element = driver.find_element(By.XPATH,f"/html/body/div[5]/div/div[3]/div[2]/div/div[4]/div[2]/div[1]/div/div[{num}]/div[1]/div[2]/span[3]")
        exurl = element.get_attribute('innerHTML')
        url = exurl.replace('conference_','')
        with open("url.csv","a",newline="") as file:
                writer = csv.writer(file)
                writer.writerow([url])

    #�ر������
    driver.close()

    #1-5ҳ
for pages in range(1,6):
    url(pages)

print("over!")
