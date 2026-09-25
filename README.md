# py-requests-jtml
requests-jtml的使用

#pip install request-html

##运行时出现以下错误：
Traceback (most recent call last):
File "d:\claudecodelx\py-requests-jtml\html1.py", line 2, in <module>
from requests_html import HTMLSession    # 导入 HTMLSession 类
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
File "C:\ProgramData\anaconda3\Lib\site-packages\requests_html.py", line 14, in <module>
from lxml.html.clean import Cleaner
File "C:\ProgramData\anaconda3\Lib\site-packages\lxml\html\clean.py", line 18, in <module>
raise ImportError(
...<2 lines>...
) from None
ImportError: lxml.html.clean module is now a separate project lxml_html_clean.
Install lxml[html_clean] or lxml_html_clean directly.

# 报错原因

`requests-html` 依赖的 `lxml.html.clean` 在新版 lxml 里被拆分出去了，单独变成了 `lxml_html_clean`，直接导入就报这个错。
提示原话：`Install lxml[html_clean] or lxml_html_clean directly.`

## 解决方法（Anaconda 环境，打开 Anaconda Prompt 执行）

### 方案 1（推荐，安装带 html_clean 的 lxml）
pip install lxml[html_clean]


### 方案 2（单独装拆分出来的包）
pip install lxml_html_clean

### 方案 3 如果上面不行，直接重装 requests_html 整套
pip uninstall lxml requests-html -y
pip install lxml[html_clean] requests-html


# HTML1
~~~~
from requests_html import HTMLSession    # 导入HTMLSession类

session = HTMLSession()          # 创建HTML会话对象
url = 'http://news.youth.cn/'    # 定义请求地址
r =session.get(url)              # 发送网络请求
print(r.html)                    # 打印网络请求的url地址

~~~~

# 输出结果
<HTML url='http://news.youth.cn/'>

# html2
from requests_html import HTMLSession    # 导入HTMLSession类
session = HTMLSession()          # 创建HTML会话对象
data = {'user':'admin','password':123456}    # 模拟表单登录的数据
r = session.post('http://httpbin.org/post',data=data)   # 发送post请求
if r.status_code == 200:                                # 判断请求是否成功
    print(r.text)                                        # 以文本形式打印返回结果

# 输出结果
{
  "args": {}, 
  "data": "", 
  "files": {}, 
  "form": {
    "password": "123456", 
    "user": "admin"
  }, 
  "headers": {
    "Accept": "*/*", 
    "Accept-Encoding": "gzip, deflate, br", 
    "Content-Length": "26", 
    "Content-Type": "application/x-www-form-urlencoded", 
    "Host": "httpbin.org", 
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/603.3.8 (KHTML, like Gecko) Version/10.1.2 Safari/603.3.8", 
    "X-Amzn-Trace-Id": "Root=1-6ab5e2b5-10195d17583e75907b7d16f7"
  }, 
  "json": null, 
  "origin": "111.60.88.247", 
  "url": "http://httpbin.org/post"
}