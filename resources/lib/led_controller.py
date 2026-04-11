import time

try:
    import spidev
    SPI_AVAILABLE = True
except ImportError:
    SPI_AVAILABLE = False


class LEDController:
    def __init__(self, num_leds=5, bus=0, device=0):
        self.num_leds = num_leds
        self.bus = bus
        self.device = device

        if SPI_AVAILABLE:
            self.spi = spidev.SpiDev()
            self.spi.open(bus, device)
            self.spi.max_speed_hz = 1000000
        else:
            self.spi = None

    def apply_brightness(self, color, brightness):
        factor = brightness / 100.0
        return tuple(int(c * factor) for c in color)

    def set_color(self, color, brightness=50):
        color = self.apply_brightness(color, brightness)

        data = []
        for _ in range(self.num_leds):
            data.extend([color[0], color[1], color[2]])

        if self.spi:
            self.spi.xfer2(data)
        else:
            with open(f"/dev/spidev{self.bus}.{self.device}", "wb") as spi:
                spi.write(bytearray(data))

        time.sleep(0.001)

    def close(self):
        if self.spi:
            self.spi.close()
