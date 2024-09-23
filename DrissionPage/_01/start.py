from DrissionPage import ChromiumPage

def start() :
    # 使用系统默认 Chromium 内核浏览器
    # 也可通过：指定路径运行
    # path = r'D:\Chrome\Chrome.exe'  # 请改为你电脑内Chrome可执行文件路径
    # ChromiumOptions().set_browser_path(path).save()
    # 或者
    # path = r'D:\Chrome\Chrome.exe'  # 请改为你电脑内Chrome可执行文件路径
    # co = ChromiumOptions().set_browser_path(path)
    # page = ChromiumPage(co)
    # page.get('http://DrissionPage.cn')
    page = ChromiumPage()
    page.get('http://DrissionPage.cn')

if __name__ == '__main__':
    start()