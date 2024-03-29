import os
import unicornhat
import time
import random

print('unicorn-hats')
unicornhat.set_layout(unicornhat.AUTO)
unicornhat.rotation(0)
unicornhat.brightness(0.3)
width, height = unicornhat.get_shape()

'''
  0,0,0,0,0,0,0,0
  0,1,1,0,0,1,1,0
  1,1,1,1,1,1,1,1
  1,1,1,1,1,1,1,1
  1,1,1,1,1,1,1,1
  0,1,1,1,1,1,1,0
  0,0,1,1,1,1,0,0
  0,0,0,1,1,0,0,0
'''


# show the zero
def show_zero():
    while True:
        # x 0
        unicornhat.set_pixel(0, 2, 100, 149, 237)
        unicornhat.set_pixel(0, 3, 100, 149, 237)
        unicornhat.set_pixel(0, 4, 100, 149, 237)
        unicornhat.set_pixel(0, 5, 100, 149, 237)
        # ----------------------------------
        # x 1
        unicornhat.set_pixel(1, 1, 100, 149, 237)
        unicornhat.set_pixel(1, 2, 100, 149, 237)
        unicornhat.set_pixel(1, 5, 100, 149, 237)
        unicornhat.set_pixel(1, 6, 100, 149, 237)
        # ----------------------------------
        # x 2
        unicornhat.set_pixel(2, 1, 100, 149, 237)
        unicornhat.set_pixel(2, 2, 100, 149, 237)
        unicornhat.set_pixel(2, 5, 100, 149, 237)
        unicornhat.set_pixel(2, 6, 100, 149, 237)
        # ----------------------------------
        # x 3
        unicornhat.set_pixel(3, 1, 100, 149, 237)
        unicornhat.set_pixel(3, 2, 100, 149, 237)
        unicornhat.set_pixel(3, 5, 100, 149, 237)
        unicornhat.set_pixel(3, 6, 100, 149, 237)
        # ----------------------------------
        # x 4
        unicornhat.set_pixel(4, 1, 100, 149, 237)
        unicornhat.set_pixel(4, 2, 100, 149, 237)
        unicornhat.set_pixel(4, 5, 100, 149, 237)
        unicornhat.set_pixel(4, 6, 100, 149, 237)
        # ----------------------------------
        # x 5
        unicornhat.set_pixel(5, 1, 100, 149, 237)
        unicornhat.set_pixel(5, 2, 100, 149, 237)
        unicornhat.set_pixel(5, 5, 100, 149, 237)
        unicornhat.set_pixel(5, 6, 100, 149, 237)
        # ----------------------------------
        # x 6
        unicornhat.set_pixel(6, 1, 100, 149, 237)
        unicornhat.set_pixel(6, 2, 100, 149, 237)
        unicornhat.set_pixel(6, 5, 100, 149, 237)
        unicornhat.set_pixel(6, 6, 100, 149, 237)
        # ----------------------------------
        # x 7
        unicornhat.set_pixel(7, 2, 100, 149, 237)
        unicornhat.set_pixel(7, 3, 100, 149, 237)
        unicornhat.set_pixel(7, 4, 100, 149, 237)
        unicornhat.set_pixel(7, 5, 100, 149, 237)
        # ----------------------------------
        unicornhat.show()
        time.sleep(0.5)
        unicornhat.clear()


# random all led
def show_random_all():
    while True:
        unicornhat.rotation(90)
        unicornhat.set_pixel(random.randint(0, 7), random.randint(0, 7), random.randint(0, 255), random.randint(0, 255),
                             random.randint(0, 255))
        unicornhat.show()
        time.sleep(0.4)
        for i in unicornhat.get_pixels():
            print(i)


# show heart
'''
  0,0,0,0,0,0,0,0
  0,1,1,0,0,1,1,0
  1,1,1,1,1,1,1,1
  1,1,1,1,1,1,1,1
  1,1,1,1,1,1,1,1
  0,1,1,1,1,1,1,0
  0,0,1,1,1,1,0,0
  0,0,0,1,1,0,0,0  
'''
'''
  0,0,0,0,0,0,0,0,
  0,0,0,0,0,0,0,0,
  0,0,1,0,0,1,0,0,  2=5
  0,1,1,1,1,1,1,0,  1-6
  0,1,1,1,1,1,1,0,  1-6
  0,0,1,1,1,1,0,0,  2-5
  0,0,0,1,1,0,0,0,  3-4
  0,0,0,0,0,0,0,0,


'''


# show heart
def show_heart():
    unicornhat.rotation(270)
    while True:
        unicornhat.set_pixel(1, 1, 255, 165, 0)
        unicornhat.set_pixel(1, 2, 255, 165, 0)
        unicornhat.set_pixel(1, 5, 255, 165, 0)
        unicornhat.set_pixel(1, 6, 255, 165, 0)
        for i in range(8):
            unicornhat.set_pixel(2, i, 255, 165, 0)
            unicornhat.set_pixel(3, i,255, 165, 0)
            unicornhat.set_pixel(4, i, 255, 165, 0)
        for x in range(1, 7):
            unicornhat.set_pixel(5, x, 255, 165, 0)
        for z in range(2, 6):
            unicornhat.set_pixel(6, z, 255, 165, 0)
        for c in range(3, 5):
            unicornhat.set_pixel(7, c, 255, 165, 0)
        unicornhat.show()
        time.sleep(0.4)
        # -------------------------
        unicornhat.clear()
        unicornhat.set_pixel(2, 2, 255, 165, 0)
        unicornhat.set_pixel(2, 5, 255, 165, 0)
        for i1 in range(1, 7):
            unicornhat.set_pixel(3, i1, 255, 165, 0)
        for x1 in range(1, 7):
            unicornhat.set_pixel(4, x1, 255, 165, 0)
        for z1 in range(2, 6):
            unicornhat.set_pixel(5, z1, 255, 165, 0)
        for c1 in range(3, 5):
            unicornhat.set_pixel(6, c1,255, 165, 0)
        unicornhat.show()
        time.sleep(0.3)
        # -------------------------
        unicornhat.clear()


# show blink heart
def rainbow_pink_heart():
    # hotpink 255,105,180
    # deep pink 255,20,147
    # pink 255,192,203
    # light pink 255,182,193
    unicornhat.rotation(180)
    while True:
        unicornhat.set_pixel(1, 1, 255, random.randint(20, 203), random.randint(147, 200))
        unicornhat.set_pixel(1, 2, 255, random.randint(20, 203), random.randint(147, 200))
        unicornhat.set_pixel(1, 5, 255, random.randint(20, 203), random.randint(147, 200))
        unicornhat.set_pixel(1, 6, 255, random.randint(20, 203), random.randint(147, 200))
        for i in range(8):
            unicornhat.set_pixel(2, i, 255, random.randint(20, 203), random.randint(147, 200))
            unicornhat.set_pixel(3, i, 255, random.randint(20, 203), random.randint(147, 200))
            unicornhat.set_pixel(4, i, 255, random.randint(20, 203), random.randint(147, 200))
        for x in range(1, 7):
            unicornhat.set_pixel(5, x, 255, random.randint(20, 203), random.randint(147, 200))
        for z in range(2, 6):
            unicornhat.set_pixel(6, z, 255, random.randint(20, 203), random.randint(147, 200))
        for c in range(3, 5):
            unicornhat.set_pixel(7, c, 255, random.randint(20, 203), random.randint(147, 200))
        unicornhat.show()
        time.sleep(0.3)
        unicornhat.clear()


# a album blink
def blink_album():
    while True:
        for x in range(8):
            for y in range(8):
                unicornhat.set_pixel(x, y, 255, 0, 0)
        unicornhat.show()
        time.sleep(1)
        for x in range(8):
            for y in range(8):
                unicornhat.set_pixel(x, y, 0, 0, 255)
        unicornhat.show()
        time.sleep(1)


# show_zero()
# show_random_all()
# blink_album()
# show_heart()
# rainbow_pink_heart()
if __name__ == '__main__':
    show_heart()

