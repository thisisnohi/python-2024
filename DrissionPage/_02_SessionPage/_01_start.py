# 导入
from DrissionPage import SessionPage
# 创建页面对象
page = SessionPage()
# 访问网页
page.get('https://gitee.com/explore/all')
# 在页面中查找元素
items = page.eles('tag:h3')
# 遍历元素: 最后一个元素为搜索帮助，排除
for item in items[:-1]:
    # 获取当前<h3>元素下的<a>元素
    lnk = item('tag:a')
    # 打印<a>元素文本和href属性
    print(lnk.text, lnk.link)

