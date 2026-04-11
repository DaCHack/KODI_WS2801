import spidev
import time

class LEDController:
    def __init__(self, num_leds=30, bus=0, device=0):
        self.num_leds = num_leds
        self.spi = spidev.SpiDev()
        self.spi.open(bus, device)
        self.spi.max_speed_hz = 1000000

    def apply_brightness(self, color, brightness):
        factor = brightness / 100.0
        return tuple(int(c * factor) for c in color)

    def set_color(self, color, brightness=100):
        color = self.apply_brightness(color, brightness)

        data = []
        for _ in range(self.num_leds):
            # WS2801 expects RGB
            data.extend([color[0], color[1], color[2]])

        self.spi.xfer2(data)

        # latch
        time.sleep(0.001)

    def close(self):
        self.spi.close()
