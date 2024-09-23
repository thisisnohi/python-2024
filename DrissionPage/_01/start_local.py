from DrissionPage._pages.chromium_page import ChromiumPage
from DrissionPage._pages.session_page import SessionPage


def login():
    # 创建页面对象
    page = SessionPage()
    # 跳转到登录页面
    page.get('http://127.0.0.1/zh/java/JDK9-17.html#_1-%E6%A8%A1%E5%9D%97%E5%8C%96')
    print('page is open')
    # tag=a  a标签
    links = page.eles('tag=a')
    links = page.eles('css:ul.sidebar-item-children a.sidebar-item')
    print('links', links)
    print('links', len(links))
    for link in links:
        print(link.text, link.link)

    # page.close()

if __name__ == '__main__':
    login()