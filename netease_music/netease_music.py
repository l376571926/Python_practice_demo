# coding: utf-8 
import atx
import time

d = atx.connect()
x = d.start_app('com.netease.cloudmusic', "com.netease.cloudmusic.activity.LoadingActivity")
print(x)

# d.swipe(200, 500, 200, 200)
# d.screenshot('temp.png')

time.sleep(1)

while not d.exists("menu.png"):
    print("未找到图片menu，等待")
d.screenshot('temp1.png')  # 截图
d.click_image("menu.png")  # 点击图片

time.sleep(1)  # 等待1秒钟打开界面

while not d.exists("setting.png"):  # 不断查找是否存在某个图片
    print("未找到图片setting，等待")  # 没查找到就打印日志
d.screenshot('temp2.png')
d.click_image("setting.png")
