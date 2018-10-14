#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Mr.yang
# Created Time : 2018/9/14 星期五 19:56:52
# File Name: water.py
# Description:
"""

class WaterHandle():
    totalWater = 0

    def change(self, water, time, cap, bottle):
        if time == 0:
            cap = water
            bottle = water
            self.totalWater += water;
        else:
            cap += water
            bottle += water

        water = 0
        water += cap // 5
        cap =cap % 5
        water += bottle // 3  #地板除去小数
        bottle = bottle % 3
        print("次数", time, "你可以换水:", water, "余下瓶子:", bottle, ",余下盖子:", cap)

        time += 1
        if (water > 0):
            self.totalWater += water
            self.change(water, time, cap, bottle)
        else:
            print("换不了了，游戏结束!")

    def game(self):
        a = input("你有多少钱:")
        self.change(int(int(a)/3), 0, 0, 0)
        print("你喝了 ", self.totalWater, "瓶水!")


water = WaterHandle()
water.game()
