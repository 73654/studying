from selenium.webdriver.common.by import By
from webtest_project.web_po.ceshiren_line.package.BaseDriver import BaseDriver


class SearchPackage(BaseDriver):
    def test_search_search(self, keyword_text):
        self.find_and_input(By.XPATH, '//*[@placeholder = "搜索"]', keyword_text)

        # self.driver.find_element(By.CLASS_NAME,
        #                          'full-page-search.search.no-blur.search-query.ember-text-field.ember-view').send_keys(
        #     keyword_text)
        # 点击搜索按钮
        self.find_and_click(By.CLASS_NAME, "d-button-label")
        # self.driver.find_element(By.CLASS_NAME, "d-button-label").click()
        return self

    def get_search_result(self):
        eles = self.finds(By.CLASS_NAME, 'topic-title')
        # eles = self.driver.find_elements(By.CLASS_NAME, 'topic-title')
        names = [e.text for e in eles]
        return names

    def get_search_result_fail(self):
        ele2 = self.get_text(By.CLASS_NAME, "fps-invalid")
        # ele2 = self.driver.find_element(By.CLASS_NAME, "fps-invalid").text
        return ele2

    def get_search_reasult_fail2(self):
        ele3 = self.get_text(By.XPATH, '//*[@class="ember-view"]/div[2]/h3')
        # ele3 = self.driver.find_element(By.XPATH,
        #                                 '/html/body/section/div/div[2]/div[2]/div[2]/div[3]/div/div/div[2]/h3').text
        return ele3
