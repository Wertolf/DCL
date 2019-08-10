'''
This module stores font path constants,
variable names are placed in alphabetical order.
'''

#constants
from .Paths import MATERIALS

#modules
import os

#original fonts
AMARANTH= os.path.join(MATERIALS, 'Fonts\Amaranth-Bold.ttf')
ARVO    = os.path.join(MATERIALS, 'Fonts\Arvo-Bold.ttf')
BRUX    = os.path.join(MATERIALS, 'Fonts\BRUX.otf')
COURIER = os.path.join(MATERIALS, 'Fonts\courbd.ttf')
SOUL02  = os.path.join(MATERIALS, 'Fonts\Soul02.ttf')
SOUL20  = os.path.join(MATERIALS, 'Fonts\Soul20.ttf')
SOUL27  = os.path.join(MATERIALS, 'Fonts\Soul27.ttf')
SOUL35  = os.path.join(MATERIALS, 'Fonts\Soul35.ttf')
SOUL43  = os.path.join(MATERIALS, 'Fonts\Soul43.ttf')
SOUL54  = os.path.join(MATERIALS, 'Fonts\Soul54.ttf')
XINGKAI = os.path.join(MATERIALS, 'Fonts\XINGKAI.TTF')
LISHU   = os.path.join(MATERIALS, 'Fonts\LISHU.TTF')
XINWEI  = os.path.join(MATERIALS, 'Fonts\XINWEI.TTF')

#particular fonts
ATTRIBUTE   = SOUL27 #avoiding name conflict with list ATTRS
BARS        = SOUL35
BUTTON      = SOUL27
COPYRIGHT   = ARVO
FATE        = SOUL43
INSTRUCTION = SOUL02
INVENTORY   = SOUL27
LOADING     = AMARANTH
LOGO        = BRUX
MARGIN      = ARVO
NEXTDAY     = SOUL02
NOTICE      = SOUL54
REASON      = SOUL54
SETTING     = SOUL43
STORY       = SOUL43
TIP         = SOUL43
TITLE       = SOUL20
USERNAME    = ARVO
