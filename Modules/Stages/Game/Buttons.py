'''
This module stores button instances for __init__.py
it is not run until __init__.game is called.
'''

##imports
#classes
from ...Classes.Button import GameButton

#constants
from ...Locals.Colors  import RED
from ...Locals.Display import CENTERX
from ...Locals.Fonts   import BUTTON

#CAUTION: run-time data, it is not run until __init__.game is called
from ...Data.Running import loadTempPlayer
player = loadTempPlayer()

filename, size = BUTTON, 60

##action buttons
DRAW = GameButton(filename, size, text='抽卡')
EAT  = GameButton(filename, size, text='进食')
DRINK= GameButton(filename, size, text='喝水')
CALM = GameButton(filename, size, text='冷静')
CURE = GameButton(filename, size, text='治疗')
NEXT = GameButton(filename, size, text='下一天')
TRADE = GameButton(filename, size, text='交易')

DRAW .tip = '1张抽卡券的价格是10元。'
EAT  .tip = '使用1张食物卡，恢复10点体力。'
DRINK.tip = '使用1张水卡，恢复10点水分。'
CALM .tip = '使用1张镇静剂卡，恢复10点精神。'
CURE .tip = '使用相应的医疗类卡，治愈你的疾病。'
NEXT .tip = '睡觉。\n迎接下一天的到来。'
TRADE.tip = '牢房里有一台自动售货机。'

_TOP   = 680
_LEFT  =  80
_RIGHT = 880
DRAW.config(
    x=(None, CENTERX, None),
    y=(_TOP, None, None),
    )
EAT.config(
    x=(_LEFT, None, None),
    y=(_TOP+80, None, None),
    )
DRINK.config(
    x=(None, CENTERX, None),
    y=(_TOP+80, None, None),
    )
CALM.config(
    x=(None, None, _RIGHT),
    y=(_TOP+80, None, None),
    )
CURE.config(
    x=(_LEFT, None, None),
    y=(_TOP+160, None, None),
    )
NEXT.config(
    x=(None, CENTERX, None),
    y=(_TOP+160, None, None),
    )
TRADE.config(
    x=(None, None, _RIGHT),
    y=(_TOP+160, None, None),
    )

##attribute buttons
#text are not set yet, set in __init__.py

size  = 44
ATTR1 = GameButton(filename, size, text=player['attr1'])
ATTR2 = GameButton(filename, size, text=player['attr2'])
ATTR3 = GameButton(filename, size, text=player['attr3'])
ATTR4 = GameButton(filename, size, text=player['attr4'])
ATTR5 = GameButton(filename, size, text=player['attr5'])

TOP = 256
ATTR1.config(
    y=(TOP, None, None),
    x=(None, 120, None),
    )
ATTR2.config(
    y=(TOP, None, None),
    x=(None, 300, None),
    )
ATTR3.config(
    y=(TOP, None, None),
    x=(None, 480, None),
    )
ATTR4.config(
    y=(TOP, None, None),
    x=(None, 660, None),
    )
ATTR5.config(
    y=(TOP, None, None),
    x=(None, 840, None),
    )

buttonList  = [DRAW, EAT, DRINK, CALM, CURE, NEXT, TRADE]
disableList = []

buttonDict = dict(
    draw=DRAW, eat=EAT, drink=DRINK, calm=CALM, cure=CURE, next=NEXT, trade=TRADE,
    )

for i in range(1, 6):
    self = eval('ATTR%d' % i)
    key = 'attr%d' % i

    self.tip = '点击以查看详细信息。'
    self.config(highlight=RED)

    buttonList.append(self)
    buttonDict[key] = self
