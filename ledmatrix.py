#!/usr/bin/env python
from samplebase import SampleBase
import time

color1 = [0,0,255]		#color in RGB values 0 to 255
color2 = [255,125,000]

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
class ledmatrix(SampleBase):
    def __init__(self, *args, **kwargs):
        super(ledmatrix, self).__init__(*args, **kwargs)

    def run(self):
        # sub_blocks = 16
        width = self.matrix.width
        height = self.matrix.height
        for i in range(1,11): 
            leds["led%d" % i] = [ledelectrode10[0]+(i-1)*ledelectrode10[2],ledelectrode10[1],color1[0],color1[1],color1[2]]
        for i in range(1,11):
            leds["led%d" % (i+10)] = [ledelectrode20[0]+(i-1)*ledelectrode20[2],ledelectrode20[1],color1[0],color1[1],color1[2]]
        for i in range(1,11):
            leds["led%d" % (i+20)] = [ledelectrode30[0]+(i-1)*ledelectrode30[2],ledelectrode30[1],color2[0],color2[1],color2[2]]
        for i in range(1,11):
            leds["led%d" % (i+30)] = [ledelectrode40[0]+(i-1)*ledelectrode40[2],ledelectrode40[1],color2[0],color2[1],color2[2]]
        leds["led41"] = [led41[0],led41[1],color1[0],color1[1],color1[2]]
        leds["led42"] = [led42[0],led42[1],color1[0],color1[1],color1[2]]
        leds["led43"] = [led43[0],led43[1],color1[0],color1[1],color1[2]]
        leds["led44"] = [led44[0],led44[1],color1[0],color1[1],color1[2]]
        for i in range(ledstatus[2]):
            leds["ledstatus%d" % (i+1)] = [ledstatus[0]+i,ledstatus[1],color1[0],color1[1],color1[2]]
        leds["ledpower"] = [ledpower[0],ledpower[1],color1[0],color1[1],color1[2]]
        leds["ledbt"] = [ledbt[0],ledbt[1],color1[0],color1[1],color1[2]]
        print(leds)
        # x_step = max(1, width / sub_blocks)
        # y_step = max(1, height / sub_blocks)
        # count = 0


        while True:
            for key, value in leds.items():
                self.matrix.SetPixel(value[0],value[1],value[2],value[3],value[4])
            # for y in range(0, height):
            #     for x in range(0, width):
            #self.matrix.SetPixel(led41[0],led41[1],color1[0],color1[1],color1[2])
            #self.matrix.SetPixel(led42[0],led42[1],color2[0],color2[1],color2[2])
            #         c = sub_blocks * int(y / y_step) + int(x / x_step)
            #         if count % 4 == 0:
            #             self.matrix.SetPixel(x, y, c, c, c)
            #         elif count % 4 == 1:
            #             self.matrix.SetPixel(x, y, c, 0, 0)
            #         elif count % 4 == 2:
            #             self.matrix.SetPixel(x, y, 0, c, 0)
            #         elif count % 4 == 3:
            #             self.matrix.SetPixel(x, y, 0, 0, c)
            #
            # count += 1
            # time.sleep(2)


# Main function
if __name__ == "__main__":
    ledmatrix = ledmatrix()
    if (not ledmatrix.process()):
        ledmatrix.print_help()
