# -*- coding:utf-8 -*-
"""
作者:chenlong
日期：2022/1/28
"""

from PIL import Image, ImageGrab
import time
from pymouse import PyMouse
from pykeyboard import PyKeyboard


class ImageFind:
    def __init__(self):
        self.mouse = PyMouse()
        self.keyboard = PyKeyboard()
        pass

    def find_image(self):
        # 打开小图
        small = Image.open('./username.png')
        # load()读取到图像的坐标数据、以及颜色数据
        sdata = small.load()

        # print(sdata[50, 30])
        color_length = len(sdata[0, 0])

        # 对当前屏幕截图（大图）
        if color_length == 3:
            big = ImageGrab.grab()
        else:
            big = ImageGrab.grab().convert('RGBA')
        bdata = big.load()
        print(bdata[125, 345])

        # 遍历小图和大图的位置
        for x in range(big.width - small.width):
            for y in range(big.height - small.height):
                if self.check_match(small, bdata, sdata, x, y):
                    # print("找到了.坐标为：[%d, %d]" % (x, y))
                    center_x = int(x + small.width / 2)
                    center_y = int(y + small.height / 2)
                    return center_x, center_y
                else:
                    print("----------------还在寻找----------------")
        return -1, -1


    def check_match(self, small, bdata, sdata, x, y):
        for i in range(small.width):
            for j in range(small.height):
                if bdata[x + i, y + j] != sdata[i, j]:
                    return False
        return True


if __name__ == '__main__':
    time.sleep(3)
    finder = ImageFind()
    x, y = finder.find_image()
    print(x, y)
    finder.mouse.click(x, y)
    finder.keyboard.type_string("图像识别到的位置在此")
    pass