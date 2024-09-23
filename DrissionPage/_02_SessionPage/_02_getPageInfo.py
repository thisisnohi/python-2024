from DrissionPage import SessionPage

page = SessionPage()
page.get('http://www.baidu.com')
# 获取页面标题
print(page.title)
# 获取页面html
print(page.html)

for i in page.cookies(as_dict=False, all_domains=True):
    print(i)

# 打印连接状态
r = page.response
print(r.status_code)


page = SessionPage()
page.get('https://gitee.com/explore')

# 获取推荐目录下所有 a 元素
li_eles = page('tag:ul@text():全部推荐项目').eles('t:a')

# 遍历列表
for i in li_eles:
    # 获取并打印标签名、文本、href 属性
    print(i.tag, i.text, i.attribute('href'))