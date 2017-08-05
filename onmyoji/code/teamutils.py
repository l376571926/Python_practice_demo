# import atx
# U10AFCPF22EFQ
# from uiautomator import Device as d
# from atx.drivers.mixin import DeviceMixin as m
# from atx.drivers.android import AndroidDevice as k

# dj = atx.connect()
# k.start_app("com.aoemo.keyboard")
# while m.exists("3.png"):
#     print("找到3.png")

# if m.exists("3.png"):
#     m.click_image("3.png");

# d.screen.on()
# d.swipe(100, 500, 100, 1000)
# x = d.info
# print(x)

# while not m.exists("3.png"):
#     print("未找到")

from uiautomator import Device
from atx.drivers.mixin import DeviceMixin

myDevice = Device('U10AFCPF22EFQ')
# myDevice.screen.on()

mixin = DeviceMixin
mixin.exists("3.png")

# myDevice.screen.off()
# ddd = d.info
# print(ddd)
