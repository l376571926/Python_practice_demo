# --------------------------------------------------------
# 妖气封印 自动上车脚本
import atx
import time
import random

d = atx.connect('U10AFCPF22EFQ')  # U10AFCPF22EFQ 指定连接一台手机
# d.start_app('com.netease.cloudmusic')

while True:
    x = random.choice(range(214, 280))
    y = random.choice(range(600, 684))
    d.click(x, y)  # 214,581 319,684    组队
    time.sleep(2)

    x = random.choice(range(154, 354))
    y = random.choice(range(560, 609))
    d.click(x, y)  # 妖气封印

    count = 0
    flag = True
    while flag:
        x = random.choice(range(409, 572))
        y = random.choice(range(601, 646))
        d.click(x, y)  # 刷新

        x = random.choice(range(1004, 1093))
        y = random.choice(range(201, 238))
        d.click(x, y)  # 第一个
        # d.click(1062, 312)  # 第二个
        # d.click(1062, 412)  # 第三个
        # d.click(1062, 512)  # 第四个
        count = count + 1
        if count % 10 == 0:
            if d.exists("item/team_detail.png"):  # 等队友
                flag = False
            elif d.exists("item/setuphero.png"):  # 准备
                flag = False
            else:
                print("还没上车--->" + str(count))
    print("成功上车--->" + str(count))

    count = 0
    while not d.exists("item/setuphero.png"):
        count = count + 1
        print("还没到准备页面---->" + str(count))

    x = random.choice(range(1079, 1217))
    y = random.choice(range(482, 613))
    d.click(x, y)

    count = 0
    while not d.exists("item/victory.png"):
        count = count + 1
        time.sleep(5)
        print("还没到胜利---->" + str(count))

    x = random.choice(range(0, 1280))
    y = random.choice(range(50, 163))
    d.click(x, y)
    time.sleep(2)

    x = random.choice(range(0, 1280))
    y = random.choice(range(50, 163))
    d.click(x, y)
    time.sleep(2)

    x = random.choice(range(0, 1280))
    y = random.choice(range(50, 163))
    d.click(x, y)
    time.sleep(10)

    print("打完了")
    # --------------------------------------------------------
