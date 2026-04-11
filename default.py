import xbmcaddon
import xbmcgui

from resources.lib.led_controller import LEDController

addon = xbmcaddon.Addon()
dialog = xbmcgui.Dialog()


def get_setting_int(id, default):
    try:
        return int(addon.getSetting(id))
    except:
        return default


def main():
    # Read hardware settings
    num_leds = get_setting_int("num_leds", 5)
    bus = get_setting_int("spi_bus", 0)
    device = get_setting_int("spi_device", 0)

    # Read color settings
    red = get_setting_int("red", 255)
    green = get_setting_int("green", 255)
    blue = get_setting_int("blue", 255)
    brightness = get_setting_int("brightness", 50)

    color = (red, green, blue)

    # Apply LED color
    led = LEDController(num_leds=num_leds, bus=bus, device=device)
    led.set_color(color, brightness)

    dialog.notification(
        "WS2801 LED",
        f"Set to RGB({red},{green},{blue}) @ {brightness}%",
        xbmcgui.NOTIFICATION_INFO,
        3000
    )


if __name__ == "__main__":
    main()
