## 用户端 Web自动化测试实战

**知识点梳理**
![img.png](img/img.png)
**手工测试与自动化测试场景对比**
![img.png](img.png)
![img_1.png](img_1.png)

**什么时候可以做 Web 自动化测试**

* 业务流程不频繁改动
* UI 元素不频繁改动
* 需要频繁回归的场景
* 核心场景等

![img_2.png](img_2.png)

**Web 自动化测试相关技术**
* Selenium：支持多语言，行业内最火最主流
* Pytest：最好用最全面的单元测试框架
* Allure：测试报告

**Selenium的简介**
* 用于web浏览器测试的工具
* 支持的浏览器包括IE，Firefox，Safari，Chrome，Edge等
* 使用简单，可使用Java，Python等多种语言编写用例脚本
* 主要由三个工具构成：WebDriver、IDE、Grid

**Selenium架构图**
![img_6.png](img_6.png)

**SeleniumIDE用例录制**

**使用场景**
* 刚开始入门UI自动化测试
* 团队代码基础较差
* 技术成长之后学习价值不高

**常用功能**

1. 新建、保存、打开
2. 开始和停止录制
3. 运行8中的所有的实例
4. 运行单个实例
5. 调试模式
6. 调整案例的运行速度
7. 要录制的网址
8. 实例列表
9. 动作、目标、值
10. 对单条命令的解释
11. 运行日志

![img_3.png](img_3.png)
其他常用功能
* 用例管理
![img_7.png](img_7.png)
* 保存和回放

**脚本优化**
```python
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestDemo01():
  def setup_method(self, method):
    # 实例化chromedriver
    self.driver = webdriver.Chrome()
    # 添加全局隐式等待
    self.driver.implicitly_wait(5)
  
  def teardown_method(self, method):
    # 关闭driver
    self.driver.quit()
  
  def test_demo01(self):
    # 访问网站
    self.driver.get("https://www.baidu.com/")
    # 设置窗口
    self.driver.set_window_size(1330, 718)
    # 点击输入框
    self.driver.find_element(By.ID, "kw").click()
    # 输入框输入信息
    self.driver.find_element(By.ID, "kw").send_keys("霍格沃兹测试开发")
    # 点击搜索按钮
    self.driver.find_element(By.ID, "su").click()
    # 等待界面加载
    time.sleep(5)
    # 元素定位后获取文本信息
    res = self.driver.find_element(By.XPATH,"//*[@id='1']/h3/a").get_attribute("text")
    # 打印文本信息
    print(res)
    # 添加断言
    assert "霍格沃兹测试开发" in res
    # 查看界面展示
    time.sleep(5)
```

**实战二目标**
* 编写测试人网站的 Web 自动化测试用例。
  1. 掌握浏览器的控制方法
  2. 熟悉定位元素方法与交互操作
  3. 学会元素等待方式

**相关知识点**
![img_4.png](img_4.png)

### web 浏览器控制
![img_5.png](img_5.png)
**get方法打开浏览器**
```python
from selenium import webdriver
import time

def window_start():
    # 实例化chromedriver
    driver = webdriver.Chrome()
    # 打开网站
    driver.get('http://www.ceshiren.com')
    # 等待一秒
    time.sleep(1)

if __name__ == '__main__':
    window_start()
```
**refresh方法刷新页面**
```python
from selenium import webdriver
import time

def window_refresh():
    # 实例化chromedriver
    driver = webdriver.Chrome()
    # 打开网站
    driver.get('http://www.ceshiren.com')
    # 等待一秒
    time.sleep(1)
    # 刷新网页
    driver.refresh()
    # 等待一秒
    time.sleep(1)

if __name__ == '__main__':
    window_refresh()
```
**用back方法回退到上一个界面**
```python
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

def window_back():
    # 实例化chromedriver
    driver = webdriver.Chrome()
    # 打开网站
    driver.get('http://www.ceshiren.com')
    # 等待一秒
    time.sleep(1)
    driver.find_element(By.XPATH,"//*[@id='ember35']").click()
    # 等待一秒
    time.sleep(1)
    # 返回上一个界面
    driver.back()
    # 等待一秒
    time.sleep(1)

if __name__ == '__main__':
    window_back()
```
**maximize_window方法使窗口最大化**
```python
def max_window():
    # 实例化chromedriver
    driver = webdriver.Chrome()
    # 打开网站
    driver.get('http://www.ceshiren.com')
    # 等待一秒
    time.sleep(1)
    # 屏幕最大化
    driver.maximize_window()
    # 等待一秒
    time.sleep(1)

if __name__ == '__main__':
    max_window()
```
**minimize_window方法使窗口最小化**
```python
from selenium import webdriver
import time

def min_window():
    # 实例化chromedriver
    driver = webdriver.Chrome()
    # 打开网站
    driver.get('http://www.ceshiren.com')
    # 等待一秒
    time.sleep(1)
    # 屏幕最小化
    driver.minimize_window()
    # 等待一秒
    time.sleep(1)

if __name__ == '__main__':
    min_window()
```
### 常见控件定位方法
![img_8.png](img_8.png)
**HTML铺垫**
* 标签：`<a>`
* 属性：href
* 类属性: class
```angular2html
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>测试人论坛</title>
</head>
<body>
<a href="https://ceshiren.com/" class="link">链接</a>
</body>
</html>
```
格式： 
```angular2html
driver.find_element_by_定位方式(定位元素)
driver.find_element(By.定位方式, 定位元素) 
```
示例，两种方式作用一模一样
官方建议使用下面的方式
```angular2html
driver.find_element_by_id("su")
driver.find_element(By.ID, "su") 
```
**通过 id 定位**

`driver.find_element(By.ID, "ID属性对应的值")`
```python
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

def id_position_method():

    # 实例化chromedriver
    driver = webdriver.Chrome()
    # 打开网站
    driver.get('http://www.ceshiren.com')
    # 等待一秒
    time.sleep(1)
    # 点击“精华帖”
    driver.find_element(By.ID,"ember35").click()
    # 等待两秒
    time.sleep(2)

if __name__ == '__main__':
    id_position_method()
```
**name 定位**

`driver.find_element(By.NAME, "Name属性对应的值")`
```python
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

def name_position_method():

    # 实例化chromedriver
    driver = webdriver.Chrome()
    # 打开网站
    driver.get('http://www.baidu.com')
    # 等待一秒
    time.sleep(1)
    # 点击更多
    driver.find_element(By.NAME,"tj_briicon").click()
    # 等待两秒
    time.sleep(2)

if __name__ == '__main__':
    name_position_method()
```
**css selector 定位**
` driver.find_element(By.CSS_SELECTOR, "css表达式")`
![img_9.png](img_9.png)
**xpath 定位**
`driver.find_element(By.XPATH, "xpath表达式")`
![img_10.png](img_10.png)
**link 定位**
`driver.find_element(By.LINK_TEXT,"文本信息")`

### 强制等待与隐式等待
**为什么要添加等待**

避免页面未渲染完成后操作，导致的报错
```python
from selenium import webdriver
from selenium.webdriver.common.by import By

def wait_sleep():
    """
    如果直接执行，不添加任何等待，可能会报错
    """
    driver = webdriver.Chrome()
    driver.get("https://vip.ceshiren.com/")
    # 不加等待，可能会因为网速等原因产生报错
    driver.find_element(By.XPATH, "//*[text()='个人中心']")

if __name__ == '__main__':
    wait_sleep()
```
**直接等待**
* 解决方案：在报错的元素操作之前添加等待
* 原理：强制等待，线程休眠一定时间
* 演练环境：https://vip.ceshiren.com/
* time.sleep(3)
```python
from selenium import webdriver
from selenium.webdriver.common.by import By

def wait_sleep():
    """
    如果直接执行，不添加任何等待，可能会报错
    """
    driver = webdriver.Chrome()
    driver.get("https://vip.ceshiren.com/")
    # 添加等待，让页面渲染完成
    time.sleep(3)
    driver.find_element(By.XPATH, "//*[text()='个人中心']")

if __name__ == '__main__':
    wait_sleep()
```
**隐式等待**
* 问题：难以确定元素加载的具体等待时间。
* 解决方案：针对于寻找元素的这个动作，使用隐式等待添加配置。
* 演练环境：https://vip.ceshiren.com/
* 原理：设置一个等待时间，轮询查找（默认0.5秒）元素是否出现，如果没出现就抛出异常

```python
#设置一个等待时间，轮询查找（默认0.5秒）元素是否出现，如果没出现就抛出异常
driver.implicitly_wait(3)
```
隐式等待无法解决的问题
* 元素可以找到，使用点击等操作，出现报错
* 原因：
  * 页面元素加载是异步加载过程，通常html会先加载完成，js、css其后
  * 元素存在与否是由HTML决定，元素的交互是由css或者js决定
  * 隐式等待只关注元素能不能找到，不关注元素能否点击或者进行其他的交互
* 解决方案：使用显式等待

**显式等待基本使用(初级)**
* 示例： WebDriverWait(driver实例, 最长等待时间, 轮询时间).until(结束条件)
* 原理：在最长等待时间内，轮询，是否满足结束条件
* 演练环境： https://vip.ceshiren.com/#/ui_study
* 注意：在初级时期，先关注使用
```python
def wait_until():
    driver = webdriver.Chrome()
    driver.get("https://vip.ceshiren.com/#/ui_study")
    WebDriverWait(driver, 10).until(
        expected_conditions.element_to_be_clickable(
            (By.CSS_SELECTOR, '#success_btn')))
    driver.find_element(By.CSS_SELECTOR, "#success_btn").click()
```
**总结**
![img_11.png](img_11.png)

### 常见控件交互方法
**点击，输入，清空**
* 点击百度搜索框
* 输入”霍格沃兹测试开发”
* 清空搜索框中信息
* 演练地址： https://www.baidu.com/
```python
# 点击百度搜索框
driver.find_element(By.ID,"kw").click()
# 输入"霍格沃兹测试开发"
driver.find_element(By.ID,"kw").send_keys("霍格沃兹测试开发")
# 清空搜索框中信息
driver.find_element(By.ID,"kw").clear()
```
**获取元素属性信息**
* 原因：
  * 定位到元素后，获取元素的文本信息，属性信息等
* 目的：
  * 根据这些信息进行断言或者调试
* 演练地址： https://vip.ceshiren.com/#/ui_study

**获取元素属性信息的方法**
* 获取元素文本
* 获取元素的属性（html的属性值）
```python
# 获取元素文本
driver.find_element(By.ID, "id").text
# 获取这个元素的name属性的值
driver.find_element(By.ID, "id").get_attribute("name")
```
**课堂练习**
* 通过对应 API 实现对页面元素的操控。
  * 点击
  * 输入
  * 获取元素文本

实战思路
![img_12.png](img_12.png)
```python
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestSearch:

    def setup_class(self):
        # 打开浏览器
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)

    def teardown_class(self):
        self.driver.quit()

    def test_search(self):
        # 打开网页
        self.driver.get("https://ceshiren.com/")
        # 点击搜索
        self.driver.find_element(By.ID, "search-button").click()
        # 输入搜索的内容
        self.driver.find_element(By.ID, "search-term").send_keys("霍格沃兹测试开发")
        self.driver.find_element(By.CLASS_NAME, "keyword").click()
        # 查看搜索结果
        elements = self.driver.find_elements(By.CLASS_NAME, "first-line")
        # 完成断言
        names = [ele.text for ele in elements]
        assert '关于霍格沃兹测试开发学社' in names
```