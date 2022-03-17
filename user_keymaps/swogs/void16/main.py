print("Starting VOID16 macropad")

import board
import busio

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.matrix import DiodeOrientation
from kmk.modules.encoder import EncoderHandler
from kmk.modules.layers import Layers
from kmk.extensions.media_keys import MediaKeys


keyboard = KMKKeyboard()

layers = Layers()
encoder1 = EncoderHandler()
encoder1.pins = (( board.D3, board.D4, None, True),)
keyboard.modules = [layers, encoder1 ]

keyboard.extensions.append( MediaKeys() )

keyboard.col_pins = (board.D10, board.MOSI, board.MISO, board.SCK, )
keyboard.row_pins = (board.A3, board.A2, board.A1, board.A0, )   
keyboard.diode_orientation = DiodeOrientation.COL2ROW

# SDA = board.A3
# SCL = board.A2
# i2c = busio.I2C(SDA, SCL)
# encoder_handler.i2c = ((i2c, None, False),)

keyboard.keymap = [
    [
        KC.AUDIO_MUTE, KC.MPRV, KC.MPLY, KC.MNXT,
        KC.E, KC.F, KC.G, KC.H,
        KC.I, KC.J, KC.K, KC.L,
        KC.M, KC.N, KC.O, KC.P,
    ]
]

encoder1.map = (
    ((KC.VOLD, KC.VOLU),),
)

if __name__ == '__main__':
    keyboard.go()
