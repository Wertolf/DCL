'''
This module stores sound constants,
including BGMs and sound effects.
'''

#constants
from .Paths import MATERIALS

#modules
import os
from pygame import mixer

#BGMs
HOMEBGM   = os.path.join(MATERIALS, r'Sounds\JustInTime.ogg')
STORYBGM  = os.path.join(MATERIALS, r'Sounds\32506.ogg')
GAMEBGM1  = os.path.join(MATERIALS, r'Sounds\EyeSpy.ogg')
GAMEBGM2  = os.path.join(MATERIALS, r'Sounds\LastResort.ogg')
ILLBGM    = os.path.join(MATERIALS, r'Sounds\LinesAreCrossed.ogg')
FATEBGM   = os.path.join(MATERIALS, r'Sounds\PikachuLogin.ogg')
TRADEBGM  = os.path.join(MATERIALS, r'Sounds\PikachuLogin.ogg')
DIEBGM    = os.path.join(MATERIALS, r'Sounds\WatchOverMe.ogg')
WINBGM1   = os.path.join(MATERIALS, r'Sounds\TimeMachine.ogg')
WINBGM2   = os.path.join(MATERIALS, r'Sounds\FatefulDecision.ogg')
ACKBGM    = os.path.join(MATERIALS, r'Sounds\FeelingGreat.ogg')

#effects
FOCUS = mixer.Sound(
    os.path.join(MATERIALS, r'Sounds\focus.wav')
    )
TYPE  = mixer.Sound(
    os.path.join(MATERIALS, r'Sounds\type.ogg')
    )
DIE   = mixer.Sound(
    os.path.join(MATERIALS, r'Sounds\die.wav')
    )
WIN   = mixer.Sound(
    os.path.join(MATERIALS, r'Sounds\win.ogg')
    )
SELL  = mixer.Sound(
    os.path.join(MATERIALS, r'Sounds\sell.wav')
    )
BUY   = mixer.Sound(
    os.path.join(MATERIALS, r'Sounds\buy.wav')
    )
VEND  = mixer.Sound(
    os.path.join(MATERIALS, r'Sounds\vend.wav')
    )
DOOR  = mixer.Sound(
    os.path.join(MATERIALS, r'Sounds\door.ogg')
    )
SHOT  = mixer.Sound(
    os.path.join(MATERIALS, r'Sounds\shot.ogg')
    )
ERROR = mixer.Sound(
    os.path.join(MATERIALS, r'Sounds\error.wav')
    )
