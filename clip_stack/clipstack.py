import atx.drivers.android
import atx.drivers.mixin
import string
import time
import sys

# 获取被测应用的package_name
# python -m atx apkparse app-debug.apk
"""
{
    "version": {
        "code": "57",
        "name": "1.5.0"
    },
    "main_activity": "com.catchingnow.tinyclipboardmanager.ActivityMain",
    "package_name": "com.catchingnow.tinyclipboardmanager"
}
"""

package_name = 'com.catchingnow.tinyclipboardmanager'
d = None


def init():
    d = atx.connect()
    return


def start_app(args):
    init()
    d.start_app(args)
    return


def click_image(args):
    d.click_image(args)  # d.click_image("button.png")
    return


def loge(args):
    print(args)
    return


def wait(args):
    d.wait(args)  # 等待一个按钮出现
    return


def exists(args):
    if d.exists(args):
        return True
    else:
        return False


def current_app():
    return d.current_app()


init()

# 字符串用单双引号都可以
start_app(package_name)
print(current_app())  # AppInfo(package='com.catchingnow.tinyclipboardmanager', activity='.ActivityMain', pid=19027)

# time.sleep(2)
# print(x)
star_btn = '13.png'
right_btn = 'right_btn.png'

a = 10  # 重复点击右上角的过滤按钮
while a > 0:
    if exists(star_btn):
        loge("点左边")
        click_image(star_btn)
    else:
        loge("点右边")
        click_image(right_btn)
    time.sleep(2)
    a = a - 1
