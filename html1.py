
from requests_html import HTMLSession    # 导入HTMLSession类

session = HTMLSession()          # 创建HTML会话对象
url = 'http://news.youth.cn/'    # 定义请求地址
r =session.get(url)              # 发送网络请求
print(r.html)                    # 打印网络请求的url地址
