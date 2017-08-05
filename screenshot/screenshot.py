import atx
import time

d = atx.connect()
fileName = 'item/temp_' + str(time.time())+'.png'
d.screenshot(fileName)
