import time
from decimal import *

INCREASE_FLAG = 1
DECREASE_FLAG = 2

INCREASE_DECREASE_KEY = "increase_decrease_flag"
MONEY_KET = "money"

UNIT_WAN = 1
UNIT_YI = 10000 * UNIT_WAN

# 板块交易
class BkTrade(object):
    def __init__(self, bk="", up_down_percent=0.00, money=0, increase_decrease_flag=INCREASE_FLAG):
        self.bk = bk
        self.up_down_percent = up_down_percent  # 涨跌幅度
        self.money = money
        self.increase_decrease_flag = increase_decrease_flag  # 净额曾减
        self.time = int(time.time())
        self.unit = "万"


def bk_trade_to_dict(bk: BkTrade) -> dict:
    return {
        'bk': bk.bk,
        'up_down_percent': bk.up_down_percent,
        'money': bk.money,
        'increase_decrease_flag': bk.increase_decrease_flag,
        'time': bk.time,
        'unit': bk.unit,
    }


def parse_up_down_percent(up_down_percent: str) -> float:
    without_percent = up_down_percent.replace("%", "")
    return float(without_percent)


def parse_money(money_str: str) -> dict:
    unit = 0

    ret = {
        INCREASE_DECREASE_KEY: INCREASE_FLAG,
        MONEY_KET: 0,
    }

    if money_str.find("-") > 0:
        ret[INCREASE_DECREASE_KEY] = DECREASE_FLAG
        money_str = money_str.replace("-", "")

    if money_str.find("万") > 0:
        money_str = money_str.replace("万", "")
        unit = UNIT_WAN
    else:
        money_str = money_str.replace("亿", "")
        unit = UNIT_YI

    money_decimal = Decimal(money_str)
    money_decimal = money_decimal * Decimal(unit)

    ret[MONEY_KET] = int(money_decimal)

    return ret
