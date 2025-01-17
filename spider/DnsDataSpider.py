# coding=utf-8

from core.public import *
from spider import BaseSpider

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


# 自己写js没成功，这里用了selenium 所以需要配合google浏览器的驱动了
class DnsDataSpider(BaseSpider):
    def __init__(self, domain):
        super().__init__()
        self.source = 'DnsBuffer'
        self.domain = domain

    # 写文件
    def write_file(self, web_lists, target, page):
        workbook = openpyxl.load_workbook(abs_path + str(target) + ".xlsx")
        worksheet = workbook.worksheets[page]  # 打开的是证书的sheet
        index = 0
        while index < len(web_lists):
            web = list()
            web.append(web_lists[index]['ssl'])
            web.append(web_lists[index]['submain'])
            worksheet.append(web)
            index += 1
        workbook.save(abs_path + str(target) + ".xlsx")
        workbook.close()

    # 解析数据，这里用(递归)的方式进行查询
    def get_json_data(self, browser):
        temp = 0
        browser.implicitly_wait(60)  # 隐式等待
        try:
            # print(temp)
            WebDriverWait(browser, 40, 0.5).until(
                EC.presence_of_element_located((By.TAG_NAME, "pre")))  # 显式等待 0.5s会进行轮询操作
            json_data = json.loads(browser.find_element_by_tag_name('pre').text)
            if json_data:
                return json_data
            else:
                temp += 1
                self.get_json_data(browser)
        finally:
            browser.close()

    # 爬取
    def spider(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-certificate-errors')
        # options.add_argument('--headless')
        browser = webdriver.Chrome(options=options)
        browser.get('https://dns.bufferover.run/dns?q=.' + self.domain)

        # json_data = {"FDNS_A": "", "RDNS": ""}

        json_data = self.get_json_data(browser)
        print(json_data)

        # print(json_data)
        browser.quit()

        try:
            for i in json_data['FDNS_A']:
                if i == '':
                    continue
                else:
                    self.resList.extend(i.split(','))
        except:
            pass

        try:
            for j in json_data['RNDS']:
                if j == '':
                    continue
                else:
                    self.resList.extend(j.split(','))
        except:
            pass

    def main(self):
        logging.info("DnsDataSpider Start")
        self.spider()
        # self.write_file(self.dnsdatalist, self.target, 2)
        return self.resList


if __name__ == '__main__':
    DnsDataSpider('nbcc.cn').main()
