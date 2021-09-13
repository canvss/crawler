# -*- coding: utf-8 -*-
"""
------------------------------
# @Date     :2021/9/10 18:25
# @Author   :epover
# @Email    :endliss@sina.cn
------------------------------
"""
# and 必须同时为true，前面代码为flase，后面代码不执行
a = 10
a > 20 and print("error")
a > 5 and print('correct')

# or 只需满足一条，前面为true后面代码不执行
a >20 or print('or is error')
a > 5 or print('or is correct')