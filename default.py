import xbmc
import xbmcgui
import xbmcaddon

from resources.lib.led_controller import LEDController

addon = xbmcaddon.Addon()
dialog = xbmcgui.Dialog()

def ask_color():
    colors = [
        ("Red", (255, 0, 0)),
        ("Green", (0, 255, 0)),
        ("Blue", (0, 0, 255)),
        ("White", (255, 255, 255)),
        ("Yellow", (255, 255, 0)),
        ("Purple", (255, 0, 255)),
        ("Cyan", (0, 255, 255)),
        ("Off", (0, 0, 0))
    ]

    names = [c[0] for c in colors]
    choice = dialog.select("Choose Color", names)

    if choice == -1:
        return None

    return colors[choice][1]


def ask_brightness():
    brightness = dialog.numeric(0, "Brightness (0-100)", "100")
    try:
        val = int(brightness)
        return max(0, min(100, val))
    except:
        return 100


def main():
    color = ask_color()
    if color is None:
        return

    brightness = ask_brightness()

    led = LEDController(num_leds=30)
    led.set_color(color, brightness)

    dialog.ok("WS2801 LED", "Color applied successfully!")


if __name__ == "__main__":
    main()
