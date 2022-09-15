# -*- coding: utf-8 -*-

"""
配置类
@author : kemomi
@time : 2022/9/15 12:35
"""
import os

# 以下参数根据自己的需要进行修改：
SYS_CONFIG = {
    # 获取到的header中t值,必须修改为自己的
    "header_t": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2OTQzNDg4MDcsIm5iZiI6MTY2MzI0NjYwNywiaWF0IjoxNjYzMjQ0ODA3LCJqdGkiOiJDTTpjYXRfbWF0Y2g6bHQxMjM0NTYiLCJvcGVuX2lkIjoiIiwidWlkIjoxMTEzNTc0MDUsImRlYnVnIjoiIiwibGFuZyI6IiJ9.uRBnG5jXiDjAa9Eek7lhRayuUUIwMe_yiMFP04KLk8o",
    # 获取到的header中的user-agent值
    "header_user_agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148",
    # 设定的完成耗时，单位s，默认-1随机表示随机生成1s~1h之内的随机数，设置为正数则为固定
    "cost_time": 10,
    # 需要通关的次数，默认1
    "cycle_count": 10000000000
}


def get(key: str):
    value = os.getenv(key)
    if value is None:
        if key in SYS_CONFIG:
            value = SYS_CONFIG[key]
    return value
