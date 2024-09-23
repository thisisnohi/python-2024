# 导入
from DrissionPage import ChromiumPage

# 创建对象
page = ChromiumPage()
# 访问网页
page.get("https://www.baidu.com")
# 输入文本
page('#kw').input("DrissionPage")
# 点击按钮
page('#su').click()
# 等待页面跳转
page.wait.load_start()
# 获取所有结果
links = page.eles('tag:h3')
print('links size:', len(links))
# 打印
for link in links:
    print(link.text)