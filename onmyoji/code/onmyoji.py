import atx
import time

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


def start_app(args):
    d.start_app(args)
    return


# def click_image(args):
#     d.click_image(args)  # d.click_image("button.png")
#     return


def click_image(args, args1, args2):
    # d.click_image(args, offset=(args1, args2))

    d.keep_screen()
    d.click_nowait(args, offset=(args1, args2))
    d.click_nowait(args, offset=(args1, args2))
    d.free_screen()
    return


def loge(args):
    print(args)
    return

def exists(args):
    if d.exists(args):
        return True
    else:
        return False


def current_app():
    return d.current_app()


d = atx.connect()

# 配置截图图片的手机分辨率
# d.resolution = (720, 1280)
# expect output: (1080, 1920) 实际获取到的值会把小的放在前面

# this is default (first check minicap and then check uiautomator)
# d.screenshot_method = atx.SCREENSHOT_METHOD_AUTO  # 默认
# d.screenshot_method = atx.SCREENSHOT_METHOD_UIAUTOMATOR  # 可选
# d.screenshot_method = atx.SCREENSHOT_METHOD_MINICAP # 可选

# d.image_match_method = atx.IMAGE_MATCH_METHOD_AUTO
# d.image_match_method = atx.IMAGE_MATCH_METHOD_TMPL  # 模版匹配, 默认
# d.image_match_method = atx.IMAGE_MATCH_METHOD_SIFT  # 特征点匹配, 可选

# d.image_match_threshold = 0.8  # 默认(模版匹配相似度)

# d.rotation = 0  # default auto detect, 这个配置一下比较好，自动识别有时候识别不出来
# 0: home key bottom(normal)
# 1: home key right
# 2: home key top
# 3: home key left

count = 30  # 循环运行5次组队御魂
while count > 0:
    count = count - 1
    while not exists("start_battle.png"):
        print("未找到图片start_battle，等待")
    click_image('start_battle.png', 0, 0)

    while exists("start_battle.png"):
        click_image("start_battle.png", 0, 0)

    while not exists("ready.png"):
        print("未找到图片ready，等待")
    click_image("ready.png", 0, 0)

    while not exists("victory.png"):
        print("未找到图片victory，等待")
    click_image("victory.png", 0, 0)

    while not exists("money_exp_plus.png"):
        print("未找到图片red_egg，等待")
    # click_image("money_exp_plus.png", 0, 0)

    # while not exists("red_egg.png"):
    #     print("未找到图片red_egg，等待")
    click_image("red_egg.png", 0, 0)

    while not exists("egg_open.png"):
        print("未找到图片egg_open，等待")
    click_image("egg_open.png", 0, 0)

    while not exists("invite_dialog.png"):
        print("未找到图片invite_dialog，等待")
    click_image("confirm.png", 0, 0)
