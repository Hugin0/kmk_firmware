import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.layers import Layers
from kmk.extensions.media_keys import MediaKeys
from kmk.modules.modtap import ModTap
from kmk.modules.capsword import CapsWord
from kmk.modules.tapdance import TapDance

keyboard = KMKKeyboard()

layers = Layers()
media = MediaKeys()

modtap = ModTap()
modtap.tap_time = 220

caps_word = CapsWord()
caps_word.keys_ignored.append(KC.UNDS)
caps_word.keys_ignored.append(KC.MINUS)
caps_word.keys_ignored.append(KC.COMMA)

tapdance = TapDance()
tapdance.tap_time = 750

keyboard.modules = [layers, modtap, tapdance, caps_word, ]
keyboard.extensions = [media, ]

keyboard.row_pins = (board.D9, board.D8, board.D7, board.D6, )
keyboard.col_pins = (
    board.D2,
    board.D3,
    board.D4,
    board.D5,
    board.A0,
    board.A1,
    board.A2,
    board.A3,
    board.D10,
    board.MOSI,
    board.MISO,
    board.SCK,
)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

# Cleaner key names
_______ = KC.TRNS
XXXXXXX = KC.NO

LOWER = KC.MO(1)
RAISE = KC.MO(2)
KB_SYS = KC.MO(3)

# my home row modtap short names for easier readability in the keymap
SH_ENT = KC.MT(KC.ENT, KC.RSFT)
TAP_CW = KC.TD(KC.LSFT, KC.CW)

MT_LALT = KC.MT(KC.S, KC.LALT, prefer_hold=False, tap_interrupted=True)
MT_LCTRL = KC.MT(KC.D, KC.LCTRL, prefer_hold=False, tap_interrupted=True)

MT_RALT = KC.MT(KC.L, KC.RALT, prefer_hold=False, tap_interrupted=True)
MT_RCTRL = KC.MT(KC.K, KC.RCTRL, prefer_hold=False, tap_interrupted=True)

keyboard.keymap = [
    [  #QWERTY
        KC.TAB,  KC.Q,    KC.W,    KC.E,     KC.R,    KC.T,    KC.Y,    KC.U,    KC.I,     KC.O,    KC.P,    KC.BSPC,
        KC.ESC,  KC.A,    MT_LALT, MT_LCTRL, KC.F,    KC.G,    KC.H,    KC.J,    MT_RCTRL, MT_RALT, KC.SCLN, KC.QUOT,
        KC.LSFT, KC.Z,    KC.X,    KC.C,     KC.V,    KC.B,    KC.N,    KC.M,    KC.COMM,  KC.DOT,  KC.SLSH, SH_ENT ,
        KC.LGUI, KC.LCTL, KC.LALT, XXXXXXX,  LOWER,   KC.SPC,  KC.LSFT,  RAISE,   KC.LEFT,  KC.DOWN, KC.UP,   KC.RGHT,
    ],
    [  #LOWER
        KC.GRV , _______, KC.UP  , _______,  _______, _______, _______, KC.N7  , KC.N8  ,  KC.N9  , _______, _______,
        KB_SYS , KC.LEFT, KC.DOWN, KC.RGHT,  _______, _______, KC.N0  , KC.N4  , KC.N5  ,  KC.N6  , _______, KC.PIPE,
        _______, _______, _______, _______,  _______, _______, _______, KC.N1  , KC.N2  ,  KC.N3  , _______, _______,
        _______, _______, _______, _______,  _______, _______, _______, _______, _______,  _______, _______, _______,

    ],
    [  #RAISE
        KC.TILD, KC.EXLM, KC.AT,   KC.HASH, KC.DLR,  KC.PERC, KC.CIRC, KC.AMPR, KC.ASTR, KC.LPRN, KC.RPRN, KC.DEL,
        _______, _______, _______, _______, _______, KC.MINS, KC.EQL , _______, _______, KC.LBRC, KC.RBRC, KC.BSLS,
        _______, _______, _______, _______, _______, KC.UNDS, KC.PLUS, _______, _______, KC.LCBR, KC.RCBR, _______,
        _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______,

    ],
    [  #KB_SYS
        _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, KC.RESET,
        _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______,
        _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______,
        _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______,
    ],
]



if __name__ == '__main__':
    print("Starting VOID40 keyboard")
    keyboard.go()
