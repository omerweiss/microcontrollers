from machine import Pin

# 74HC595
# 16: VCC
# 15, 1~7: Q0~Q7
# 14: DS   --- Pico GPIO 18
# 13: OE   --- Pico GPIO 19
# 12: STCP --- Pico GPIO 20
# 11: SHCP --- Pico GPIO 21
# 9: Q7S
# 8: GND

class Chip74HC595(object):
    def __init__(self, ds: int=18, stcp: int=20, shcp: int=21, oe: int=19):
        self._ds = Pin(ds, Pin.OUT, value=0)
        self._shcp = Pin(shcp, Pin.OUT, value=0)
        self._stcp = Pin(stcp, Pin.OUT, value=0)
        self._oe = Pin(oe, Pin.OUT, value=0)
        self.enable()

    def shiftOut(self,direction,data): 
        self._shcp.on() 
        self._stcp.on()
        if direction: 
            for i in range(8):
                bit = data << i
                bit = bit & 0x80 
                if bit == 0x80:
                    self._ds.on()
                else:
                    self._ds.off()
                self._shift_bit()
            self._send_data()
        if not direction: 
            for i in range(8):
                bit = data >> i
                bit = bit & 0x01
                if bit == 0x01:
                    self._ds.on()
                else:
                    self._ds.off()
                self._shift_bit()
            self._send_data()

    def clear(self):
        for i in range(8):
            self._ds.off()
            self._shift_bit()
        self._send_data()
        self.enable()

    def _shift_bit(self):
        self._shcp.off()
        self._shcp.on()

    def _send_data(self):
        self._stcp.off()
        self._stcp.on()
        
    def disable(self):
        self._oe.on()

    def enable(self):
        self._oe.off()