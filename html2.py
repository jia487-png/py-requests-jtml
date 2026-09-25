from requests_html import HTMLSession    # 导入HTMLSession类
session = HTMLSession()          # 创建HTML会话对象
data = {'user':'admin','password':123456}    # 模拟表单登录的数据
r = session.post('http://httpbin.org/post',data=data)   # 发送post请求
if r.status_code == 200:                                # 判断请求是否成功
    print(r.text)                                        # 以文本形式打印返回结果
