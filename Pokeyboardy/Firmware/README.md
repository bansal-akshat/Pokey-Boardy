# Firmware

Pokeyboardy runs [KMK](https://github.com/KMKfw/kmk_firmware) on [CircuitPython](https://circuitpython.org/).

## Flashing

1. Put the XIAO RP2040 into bootloader mode and flash [CircuitPython](https://circuitpython.org/board/seeeduino_xiao_rp2040/) if it isn't already installed
2. Copy the `KMK` directory and its dependencies (`kmk_firmware`) onto the CIRCUITPY drive
3. Copy `KMK/main.py` to the root of the CIRCUITPY drive
4. It boots automatically — keys, encoder, RGB and OLED all work out of the box

## Layout

| Key (matrix order) | Action |
|--------------------|--------|
| 1 | Ctrl+C |
| 2 | Ctrl+V |
| 3 | Mute |
| 4 | Ctrl+X |
| 5 | Ctrl+Z |
| 6 (empty slot) | Ctrl+Shift+Z |
| Encoder | Volume up / down |

RGB runs a soft swirl by default; OLED shows the board name and encoder hint.
