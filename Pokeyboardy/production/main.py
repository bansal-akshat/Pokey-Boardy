import board
import busio
import displayio

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.matrix import DiodeOrientation
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.rgb import RGB, AnimationModes
from kmk.extensions.display import Display, TextEntry
from kmk.extensions.display.ssd1306 import SSD1306

keyboard = KMKKeyboard()

keyboard.col_pins = (board.GP26, board.GP27, board.GP28)
keyboard.row_pins = (board.GP3, board.GP4)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

encoder_handler = EncoderHandler()
encoder_handler.pins = ((board.GP2, board.GP1, None),)
encoder_handler.map = ((KC.VOLU, KC.VOLD),)
keyboard.modules.append(encoder_handler)

rgb = RGB(
    pixel_pin=board.GP29,
    num_pixels=2,
    animation_mode=AnimationModes.SWIRL,
    hue_default=60,
    sat_default=80,
    val_default=60,
    animation_speed=1.5,
)
keyboard.extensions.append(rgb)

# 0.91in 128x32 ssd1306 oled over i2c on gp6 sda gp7 scl
displayio.release_displays()
i2c_bus = busio.I2C(board.GP7, board.GP6)
driver = SSD1306(i2c=i2c_bus, device_address=0x3C)
display = Display(
    entries=[
        TextEntry(text='Pokeyboardy', x=0, y=0),
        TextEntry(text='enc: volume', x=0, y=2, x_anchor='L', y_anchor='T'),
    ],
    width=128,
    height=32,
    driver=driver,
)
keyboard.extensions.append(display)

keyboard.keymap = [
    [
        KC.LCTL(KC.C), KC.LCTL(KC.V), KC.MUTE,
        KC.LCTL(KC.X), KC.LCTL(KC.Z), KC.LSFT(KC.LCTL(KC.Z)),
    ]
]

if __name__ == '__main__':
    keyboard.go()
