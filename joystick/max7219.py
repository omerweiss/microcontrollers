from machine import Pin, SPI

class MAX7219:
    def __init__(self, spi, cs_pin):
        self.spi = spi
        self.cs = Pin(cs_pin, Pin.OUT)
        self.init_display()

    def init_display(self):
        self.write_byte(0x09, 0xFF)  # Decode mode: BCD for all digits
        self.write_byte(0x0A, 0x0F)  # Intensity: 15 (max)
        self.write_byte(0x0B, 0x07)  # Scan limit: 8 digits
        self.write_byte(0x0C, 0x01)  # Display on
        self.clear()

    def write_byte(self, address, data):
        self.cs.value(0)
        self.spi.write(bytearray([address, data]))
        self.cs.value(1)

    def clear(self):
        for i in range(1, 5):
            self.write_byte(i, 0)

    def display_number(self, num):
        # Ensure num is an integer
        if not isinstance(num, int):
            raise ValueError("Input must be an integer")
        if num < 0 or num > 9999:
            raise ValueError("Number out of range (0-9999)")

        # Convert to 4-digit list with manual padding
        digits = [int(d) for d in f"{num:04d}"]
        for i, digit in enumerate(digits):
            self.write_byte(i + 1, digit)