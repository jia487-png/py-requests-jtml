from requests_html import HTMLSession,UserAgent    # 导入HTMLSession类

session = HTMLSession()          # 创建HTML会话对象
ua = UserAgent().random          # 创建随机请求头
r = session.get('http://httpbin.org/get',headers = {'user-agent': ua})
if r.status_code == 200:         # 判断请求是否成功
    print(r.text)                # 以文本形式打印返回结果