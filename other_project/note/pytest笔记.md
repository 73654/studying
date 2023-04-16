## pytest测试框架
**知识点梳理**
![image.png](https://note.youdao.com/yws/res/2867/WEBRESOURCE437ece77859f498a8aa2a2e683191396)
**实战思路**
![image.png](https://note.youdao.com/yws/res/2868/WEBRESOURCEc70e11a268184769a2bb75891052cab5)
**Pytest 是什么？**

- pytest 能够支持简单的单元测试和复杂的功能测试；
- pytest 可以结合 Requests 实现接口测试； 结合 Selenium、Appium 实现自动化功能测试；
- 使用 pytest 结合 Allure 集成到 Jenkins 中可以实现持续集成。
- pytest 支持 315 种以上的插件；

**为什么要选择 Pytest**
- 丰富的第三方插件
  - 报告
  - 多线程
  - 顺序控制
![image.png](https://note.youdao.com/yws/res/2869/WEBRESOURCE599d97effca34f1cb9025191f244f907)
- 简单灵活
```
# content of test_sample.py
def inc(x):
    return x + 1


def test_answer():
    assert inc(3) == 5
```
- 兼容 unittest
- 定制化插件开发
![image.png](https://note.youdao.com/yws/res/2870/WEBRESOURCE49296f8b530540afaaec8d9eaacd5bc4)

**pytest命名规则**
- 文件:test_开头 或者 _test 结尾
- 类:Test 开头
- 方法/函数:test_开头
- 注意：测试类中不可以添加__init__构造函数	

#### pytest 用例结构
- 三部分构成
  - 用例名称
  - 用例步骤
  - 用例断言

用例示例:
```python
def test_XXX(self):
    # 测试步骤1
    # 测试步骤2
    # 断言  实际结果 对比 预期结果
    assert ActualResult == ExpectedResult
```
类级别的用例示例:

```python
class TestXXX:
    def setup(self):
        # 资源准备
        pass

    def teardown(self):
        # 资源销毁
        pass

    def test_XXX(self):
        # 测试步骤1
        # 测试步骤2
        # 断言  实际结果 对比 预期结果
        assert ActualResult == ExpectedResult
```
#### pytest 用例断言
**概念**
断言(assert)，是一种在程序中的一阶逻辑(如：一个结果为真或假的逻辑判断式)，目的为了表示与验证软件开发者预期的结果。当程序执行到断言的位置时，对应的断言应该为真。若断言不为真时，程序会中止执行，并给出错误信息。
**断言的用法**
- 断言写法
  - assert <表达式>
  - assert <表达式>,<描述>

```
assert <bool expression>;       
assert <bool expression> : <message>;
```
示例 1:

```python
def test_a():
    assert True

def test_b():
    a = 1
    b = 1
    c = 2
    assert a + b == c, f"{a}+{b}=={c}, 结果为真"
```
示例2:

```python
def test_c():
    a = 1
    b = 1
    c = 2
    assert 'abc' in "abcd"

import sys
def test_plat():
    assert ('linux' in sys.platform), "该代码只能在 Linux 下执行"
```
**Pytest 测试框架结构（setup/teardown）**

`setup_module/teardown_module`	全局模块级

`setup_class/teardown_class`	类级，只在类中前后运行一次

`setup_function/teardown_function`	函数级，在类外

`setup_method/teardown_method`	方法级，类中的每个方法执行前后

`setup/teardown`	在类中，运行在调用方法的前后（重点）

### pytest 参数化用例

**参数化**
- 通过参数的方式传递数据，从而实现数据和脚本分离。
- 并且可以实现用例的重复生成与执行。

**参数化应用场景**
- 测试登录场景
  - 测试登录成功，登录失败(账号错误，密码错误)
  - 创建多种账号: 中⽂文账号，英⽂文账号
- 普通测试用例方法
  - Copy 多份代码 or 读⼊入参数?
  - 一次性执⾏多个输⼊入参数

```
def test_param_login_ok():
    # 登录成功
    username = "right"
    password = "right"
    login(username,password)

def test_param_login_fail():
    # 登录失败
    username = "wrong"
    password = "wrong"
    login(username,password)
```
**参数化实现方案**
- pytest 参数化实现方法
- 装饰器：@pytest.mark.parametrize

```
@pytest.mark.parametrize("username,password",[["right","right"], ["wrong","wrong"]])
def test_param(username,password):
    login(username,password)
```
#### 参数化测试函数使用
**参数化：单参数情况**
- 单参数，可以将数据放在列表中

```
search_list = ['appium','selenium','pytest']

@pytest.mark.parametrize('name',search_list)
def test_search(name):
    assert name in search_list
```
**参数化：多参数情况**
- 将数据放在列表嵌套元组中
- 将数据放在列表嵌套列表中

```
# 数据放在元组中
@pytest.mark.parametrize("test_input,expected",[
    ("3+5",8),("2+5",7),("7+5",12)
])
def test_mark_more(test_input,expected):
    assert eval(test_input) == expected
# 数据放在列表中
@pytest.mark.parametrize("test_input,expected",[
    ["3+5",8],["2+5",7],["7+5",12]
])
def test_mark_more(test_input,expected):
    assert eval(test_input) == expected
```
**参数化：用例重命名-添加 ids 参数**
- 通过ids参数，将别名放在列表中

```
@pytest.mark.parametrize("test_input,expected",[
    ("3+5",8),("2+5",7),("7+5",12)
],ids=['add_3+5=8','add_2+5=7','add_3+5=12'])
def test_mark_more(test_input,expected):
    assert eval(test_input) == expected
```
**参数化：用例重命名-添加 ids 参数（中文）**

```
@pytest.mark.parametrize("test_input,expected",[
    ("3+5",8),("2+5",7),("7+5",12)
],ids=["3和5相加","2和5相加","7和5相加"])
def test_mark_more(test_input,expected):
    assert eval(test_input) == expected
```

```
# 创建conftest.py 文件 ，将下面内容添加进去，运行脚本
def pytest_collection_modifyitems(items):
    """
    测试用例收集完成时，将收集到的用例名name和用例标识nodeid的中文信息显示在控制台上
    """
    for i in items:
        i.name=i.name.encode("utf-8").decode("unicode_escape")
        i._nodeid=i.nodeid.encode("utf-8").decode("unicode_escape")
```
**参数化：笛卡尔积**
- 两组数据
  - a=[1,2,3]
  - b=[a,b,c]
- 对应有几种组合形势 ？
  - (1,a),(1,b),(1,c)
  - (2,a),(2,b),(2,c)
  - (3,a),(3,b),(3,c)

```
@pytest.mark.parametrize("b",["a","b","c"])
@pytest.mark.parametrize("a",[1,2,3])
def test_param1(a,b):
    print(f"笛卡积形式的参数化中 a={a} , b={b}")
```

#### pytest 运行用例
**运行多条用例**
- 运行 某个/多个 用例包
- 运行 某个/多个 用例模块
- 运行 某个/多个 用例类
- 运行 某个/多个 用例方法

**运行多条用例方式**
- 执行包下所有的用例：`pytest/py.test [包名]`
- 执行单独一个 pytest 模块：`pytest 文件名.py`
- 运行某个模块里面某个类：`pytest 文件名.py::类名`
- 运行某个模块里面某个类里面的方法：`pytest 文件名.py::类名::方法名`

**运行结果分析**
- 常用的：fail/error/pass
- 特殊的结果：warning/deselect

#### 常用命令行参数

```
 --help 
-x   用例一旦失败(fail/error)，就立刻停止执行
--maxfail=num 用例达到
-m  标记用例
-k  执行包含某个关键字的测试用例
-v 打印详细日志
-s 打印输出日志（一般-vs一块儿使用）
--collect-only（测试平台，pytest 自动导入功能 ）
```
#### Pytest 标记测试用例
**Mark：标记测试用例**

* 场景:只执行符合要求的某一部分用例 可以把一个web项目划分多个模块，然后指定模块名称执行。
* 解决: 在测试用例方法上加 @pytest.mark.标签名
* 执行: -m 执行自定义标记的相关用例
  * pytest -s test_mark_zi_09.py -m=webtest
  * pytest -s test_mark_zi_09.py -m apptest
  * pytest -s test_mark_zi_09.py -m "not ios"

**pytest 浮点数计算精度**
`pytest.appeox()`

##### pytest.ini 配置
**pytest.ini 是什么**
* pytest.ini 是 pytest 的配置文件
* 可以修改  pytest  的默认行为
* 不能使用任何中文符号，包括汉字、空格、引号、冒号等等

**pytest.ini**
* 修改用例的命名规则
* 配置日志格式，比代码配置更方便
* 添加标签，防止运行过程报警告错误
* 指定执行目录
* 排除搜索目录

**pytest 配置- 改变运行规则**
```angular2html
;执行check_开头和 test_开头的所有的文件，后面一定要加*
python_files = check_* test_*
;执行所有的以Test和Check开头的类
python_classes = Test*  Check*
;执行所有以test_和check_开头的方法
python_functions= test_* check_*
```
**pytest 配置- 添加默认参数**
```angular2html
addopts = -v -s --alluredir=./results
```
**pytest 配置- 指定/忽略执行目录**
```angular2html
;设置执行的路径
;testpaths = bilibili baidu
;忽略某些文件夹/目录
norecursedirs = result logs datas test_demo*
```
**pytest 配置- 日志**

pytest.ini 文件配置日志级别，保存地址等内容。
* 注意： windows系统 需要把中文 注释去掉。
```angular2html
[pytest]
;日志开关 true false
log_cli = true
;日志级别
log_cli_level = info
;打印详细日志，相当于命令行加 -vs
addopts = --capture=no
;日志格式
log_cli_format = %(asctime)s [%(levelname)s] %(message)s (%(filename)s:%(lineno)s)
;日志时间格式
log_cli_date_format = %Y-%m-%d %H:%M:%S
;日志文件位置
log_file = ./log/test.log
;日志文件等级
log_file_level = info
;日志文件格式
log_file_format = %(asctime)s [%(levelname)s] %(message)s (%(filename)s:%(lineno)s)
;日志文件日期格式
log_file_date_format = %Y-%m-%d %H:%M:%S
```

#### pytest 设置跳过、预期失败

**Mark：跳过(Skip)及预期失败(xFail)**
* 这是 pytest 的内置标签，可以处理一些特殊的测试用例，不能成功的测试用例
* skip - 始终跳过该测试用例
* skipif - 遇到特定情况跳过该测试用例
* xfail - 遇到特定情况,产生一个“期望失败”输出

**Skip 使用场景**
* 调试时不想运行这个用例
* 标记无法在某些平台上运行的测试功能
* 在某些版本中执行，其他版本中跳过
* 比如：当前的外部资源不可用时跳过
  * 如果测试数据是从数据库中取到的，
  * 连接数据库的功能如果返回结果未成功就跳过，因为执行也都报错
* 解决 1：添加装饰器
  * @pytest.mark.skip
  * @pytest.mark.skipif
* 解决 2：代码中添加跳过代码
  * pytest.skip(reason)

**xfail 使用场景**

* 与 skip 类似 ，预期结果为 fail ，标记用例为 fail
* 用法：添加装饰器@pytest.mark.xfail

### 常用第三方库 yaml

**YAML**
* 一种数据序列化格式
* 用于人类的可读性和与脚本语言的交互
* 一种被认为可以超越 XML、JSON 的配置文件

**YAML 基本语法规则**
* 大小写敏感
* 使用缩进表示层级关系
* 缩进时不允许使用 Tab 键，只允许使用空格
* 缩进的空格数目不重要，只要相同层级的元素左侧对齐即可
* `# `表示注释，从这个字符一直到行尾，都会被解析器忽略

**YAML 支持的数据结构**
* 对象：键值对的集合，用冒号 “:” 表示
* 数组：一组按次序排列的值，前加 “-”
* 纯量：单个的、不可再分的值
  * 字符串
  * 布尔值
  * 整数
  * 浮点数
  * Null
  * 时间
  * 日期
```angular2html
# 编程语言
languages:
  - PHP
  - Java
  - Python 
book:
  Python入门: # 书籍名称
    price: 55.5
    author: Lily
    available: True
    repertory: 20
    date: 2018-02-17
  Java入门:
    price: 60
    author: Lily
    available: False
    repertory: Null
    date: 2018-05-11
```

#### PyYAML
* Python 的 YAML 解析器和生成器
* 官网：https://pypi.org/project/PyYAML/
* 安装：pip install pyyaml

**创建 yaml 文件**

```python

from other_project import pyyaml

data = {
    "client": {"default-character-set": "utf8"},
    "mysql": {"user": 'root', "password": 123},
    "custom": {
        "user1": {"user": "张三", "pwd": 666},
        "user2": {"user": "李四", "pwd": 999},
    }
}
# 直接 dump 可以把对象转为 YAML 文档
with open('./my.pyyaml', 'w', encoding='utf-8') as f:
    pyyaml.dump(data, f, allow_unicode=True)
```
**读取 yaml 文件**

```python

from other_project import pyyaml

file_path = './my.pyyaml'

with open(file_path, 'r', encoding='utf-8') as f:
    data = pyyaml.safe_load(f)
print(data)
```

#### Pytest 结合数据驱动 YAML

**数据驱动**
* 什么是数据驱动？
  * 数据驱动就是数据的改变从而驱动自动化测试的执行，最终引起测试结果的改变。简单来说，就是参数化的应用。数据量小的测试用例可以使用代码的参数化来实现数据驱动，数据量大的情况下建议大家使用一种结构化的文件(例如 yaml，json 等)来对数据进行存储，然后在测试用例中读取这些数据。
* 应用：
  * App、Web、接口自动化测试
  * 测试步骤的数据驱动
  * 测试数据的数据驱动
  * 配置的数据驱动

**yaml 文件使用**
* 查看 yaml 文件
  * pycharm
  * txt 记事本
* 读取 yaml 文件
  * 安装：pip install pyyaml
  * 方法：yaml.safe_load(f)
  * 方法：yaml.safe_dump(f)
```python
import yaml
file_path = './my.yaml'
with open(file_path, 'r', encoding='utf-8') as f:
    data = yaml.safe_load(f)
```

**工程目录结构**

* data 目录：存放 yaml 数据文件
* func 目录：存放被测函数文件
* testcase 目录：存放测试用例文件
```angular2html
# 工程目录结构
.
├── data
│   └── data.yaml
├── func
│   ├── __init__.py
│   └── operation.py
└── testcase
    ├── __init__.py
    └── test_add.py
```

**测试准备**
* 被测对象：operation.py
* 测试用例：test_add.py
* 测试数据：data.yaml
```angular2html
# operation.py 文件内容
def my_add(x, y):
    result = x + y
    return result
# test_add.py 文件内容
class TestWithYAML:
  @pytest.mark.parametrize('x,y,expected', [[1, 1, 2]])
  def test_add(self, x, y, expected):
    assert my_add(int(x), int(y)) == int(expected)
# data.yaml 文件内容
-
  - 1
  - 1
  - 2
-
  - 3
  - 6
  - 9
-
  - 100
  - 200
  - 300
```

**Pytest 数据驱动结合 yaml 文件**
```angular2html
# 读取yaml文件
def get_yaml():
    """
    获取json数据
    :return: 返回数据的结构：[[1, 1, 2], [3, 6, 9], [100, 200, 300]]
    """
    with open('../datas/data.yaml', 'r') as f:
        data = yaml.safe_load(f)
        return data
```