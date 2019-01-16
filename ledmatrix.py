#!/usr/bin/env python
from samplebase import SampleBase
import time

colorR=0
colorG=0
colorB=255
x=9
y=5

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
            # for y in range(0, height):
            #     for x in range(0, width):
                    self.matrix.SetPixel(x,y,colorR,colorG,colorB)
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
