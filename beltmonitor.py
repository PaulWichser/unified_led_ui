#!/usr/bin/env python
from samplebase import SampleBase
import time
import board
import busio
import adafruit_character_lcd.character_lcd_rgb_i2c as character_lcd

sleeptime = 3        #seconds to sleep between states

#Initialize the lcd display
lcd_columns = 16
lcd_rows = 2
i2c = busio.I2C(board.SCL, board.SDA)
lcd = character_lcd.Character_LCD_RGB_I2C(i2c, lcd_columns, lcd_rows)
lcd.color = [100, 0, 0]


#Initialize LED matrix
width = 64                      #number of LEDs in a matrix row
height = 32                     #number of LEDs in a matrix column
color1 = [0,0,255]		#color in RGB values 0 to 255
color2 = [255,125,0]

ledelectrode10 = [0,18,3]		#locations of electrode leds 1-10, indexed at 0,0 [x,y,xspace]
ledelectrode20 = [36,18,3]
ledelectrode30 = [0,25,3]
ledelectrode40 = [36,25,3]
ledstatus = [24,1,16]			#status leds [x,y,length]
ledpower = [9,5]			#power led location [x,y]
ledbt = [54,5]				#bluetooth led location [x,y]
led41 = [6,30]
led42 = [21,30]
led43 = [42,30]
led44 = [57,30]

leds = {}
for i in range(1,11):
    leds["led%d" % i] = [ledelectrode10[0]+(i-1)*ledelectrode10[2],ledelectrode10[1],0,0,0]
for i in range(1,11):
    leds["led%d" % (i+10)] = [ledelectrode20[0]+(i-1)*ledelectrode20[2],ledelectrode20[1],0,0,0]
for i in range(1,11):
    leds["led%d" % (i+20)] = [ledelectrode30[0]+(i-1)*ledelectrode30[2],ledelectrode30[1],0,0,0]
for i in range(1,11):
    leds["led%d" % (i+30)] = [ledelectrode40[0]+(i-1)*ledelectrode40[2],ledelectrode40[1],0,0,0]
leds["led41"] = [led41[0],led41[1],0,0,0]
leds["led42"] = [led42[0],led42[1],0,0,0]
leds["led43"] = [led43[0],led43[1],0,0,0]
leds["led44"] = [led44[0],led44[1],0,0,0]
for i in range(ledstatus[2]):
    leds["ledstatus%d" % (i+1)] = [ledstatus[0]+i,ledstatus[1],0,0,0]
leds["ledpower"] = [ledpower[0],ledpower[1],0,0,0]
leds["ledbt"] = [ledbt[0],ledbt[1],0,0,0]
print(leds)

class ledmatrix(SampleBase):
    def __init__(self, *args, **kwargs):
        super(ledmatrix, self).__init__(*args, **kwargs)

    def run(self):
        # sub_blocks = 16
        width = self.matrix.width
        height = self.matrix.height
        # x_step = max(1, width / sub_blocks)
        # y_step = max(1, height / sub_blocks)
        # count = 0


        while True:
            #State1: Power blue, loading animation
            for x in range(self.matrix.width):
                for y in range(self.matrix.height):
                    self.matrix.SetPixel(x,y,0,0,0)
            for key, value in leds.items():
                leds[key] = [value[0],value[1],0,0,0]
            leds["ledpower"] = [ledpower[0],ledpower[1],color1[0],color1[1],color1[2]]
            power=leds.get("ledpower")
            self.matrix.SetPixel(power[0],power[1],power[2],power[3],power[4])
            lcd.message = "                "
            start = time.time()
            while (time.time() - start) < sleeptime:
                lcd.message = "      *   "
                time.sleep(0.5)
                lcd.message = "      **  "
                time.sleep(0.5)
                lcd.message = "      *** "
                time.sleep(0.5)
                lcd.message = "      ****"
                time.sleep(0.5)

            #State2: Status LEDs amber, "Connect CABLE"
            for i in range(ledstatus[2]):
                self.matrix.SetPixel(ledstatus[0]+i,ledstatus[1],color2[0],color2[1],color2[2])
            lcd.message = "                "
            lcd.message = "Connect CABLE"
            time.sleep(sleeptime)

            #State3: Status LEDs blink blue, "INITIALIZING ..."
            lcd.message = "                "
            lcd.message = "INITIALIZING ..."
            start = time.time()
            while (time.time() - start) < 2:
                for i in range(ledstatus[2]):
                    self.matrix.SetPixel(ledstatus[0]+i,ledstatus[1],color1[0],color1[1],color1[2])
                time.sleep(0.8)
                for i in range(ledstatus[2]):
                    self.matrix.SetPixel(ledstatus[0]+i,ledstatus[1],0,0,0)
                time.sleep(0.2)


            #State4: 2 LEDs amber, "Ready To Test"
            for x in range(self.matrix.width):
                for y in range(self.matrix.height):
                    self.matrix.SetPixel(x,y,0,0,0)
            for key, value in leds.items():
                leds[key] = [value[0],value[1],color1[0],color1[1],color1[2]]
            leds["led12"]=(leds["led12"][0],leds["led12"][1],color2[0],color2[1],color2[2])
            leds["led25"]=(leds["led25"][0],leds["led25"][1],color2[0],color2[1],color2[2])
            for key, value in leds.items():
                self.matrix.SetPixel(value[0],value[1],value[2],value[3],value[4])
            lcd.message = "                "
            lcd.message = "Ready To Test"
            time.sleep(5)

            #State5: Status and 15 LEDs blink amber, "Issues Found"
            lcd.message = "                "
            lcd.message = "Issues Found"
            start = time.time()
            while (time.time() - start) < 5:
                for i in range(ledstatus[2]):
                    self.matrix.SetPixel(ledstatus[0]+i,ledstatus[1],color2[0],color2[1],color2[2])
                self.matrix.SetPixel(leds["led3"][0],leds["led3"][1],color2[0],color2[1],color2[2])
                self.matrix.SetPixel(leds["led4"][0],leds["led4"][1],color2[0],color2[1],color2[2])
                self.matrix.SetPixel(leds["led5"][0],leds["led5"][1],color2[0],color2[1],color2[2])
                self.matrix.SetPixel(leds["led6"][0],leds["led6"][1],color2[0],color2[1],color2[2])
                self.matrix.SetPixel(leds["led7"][0],leds["led7"][1],color2[0],color2[1],color2[2])
                self.matrix.SetPixel(leds["led8"][0],leds["led8"][1],color2[0],color2[1],color2[2])
                self.matrix.SetPixel(leds["led12"][0],leds["led12"][1],color2[0],color2[1],color2[2])
                self.matrix.SetPixel(leds["led13"][0],leds["led13"][1],color2[0],color2[1],color2[2])
                self.matrix.SetPixel(leds["led14"][0],leds["led14"][1],color2[0],color2[1],color2[2])
                self.matrix.SetPixel(leds["led15"][0],leds["led15"][1],color2[0],color2[1],color2[2])
                self.matrix.SetPixel(leds["led16"][0],leds["led16"][1],color2[0],color2[1],color2[2])
                self.matrix.SetPixel(leds["led24"][0],leds["led24"][1],color2[0],color2[1],color2[2])
                self.matrix.SetPixel(leds["led25"][0],leds["led25"][1],color2[0],color2[1],color2[2])
                self.matrix.SetPixel(leds["led33"][0],leds["led33"][1],color2[0],color2[1],color2[2])
                self.matrix.SetPixel(leds["led34"][0],leds["led34"][1],color2[0],color2[1],color2[2])
                time.sleep(0.8)
                for i in range(ledstatus[2]):
                    self.matrix.SetPixel(ledstatus[0]+i,ledstatus[1],0,0,0)
                self.matrix.SetPixel(leds["led3"][0],leds["led3"][1],0,0,0)
                self.matrix.SetPixel(leds["led4"][0],leds["led4"][1],0,0,0)
                self.matrix.SetPixel(leds["led5"][0],leds["led5"][1],0,0,0)
                self.matrix.SetPixel(leds["led6"][0],leds["led6"][1],0,0,0)
                self.matrix.SetPixel(leds["led7"][0],leds["led7"][1],0,0,0)
                self.matrix.SetPixel(leds["led8"][0],leds["led8"][1],0,0,0)
                self.matrix.SetPixel(leds["led12"][0],leds["led12"][1],0,0,0)
                self.matrix.SetPixel(leds["led13"][0],leds["led13"][1],0,0,0)
                self.matrix.SetPixel(leds["led14"][0],leds["led14"][1],0,0,0)
                self.matrix.SetPixel(leds["led15"][0],leds["led15"][1],0,0,0)
                self.matrix.SetPixel(leds["led16"][0],leds["led16"][1],0,0,0)
                self.matrix.SetPixel(leds["led24"][0],leds["led24"][1],0,0,0)
                self.matrix.SetPixel(leds["led25"][0],leds["led25"][1],0,0,0)
                self.matrix.SetPixel(leds["led33"][0],leds["led33"][1],0,0,0)
                self.matrix.SetPixel(leds["led34"][0],leds["led34"][1],0,0,0)
                time.sleep(0.2)

# Main function
if __name__ == "__main__":
    ledmatrix = ledmatrix()
    if (not ledmatrix.process()):
        ledmatrix.print_help()
