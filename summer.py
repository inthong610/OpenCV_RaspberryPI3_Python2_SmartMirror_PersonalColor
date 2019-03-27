# 여름 쿨

# 참조 : https://picamera.readthedocs.io/en/release-1.10/recipes1.html#overlaying-images-on-the-preview
#       <overlaying images on the preview2.py>, <over_laying_text_on_the_output2.py>

import picamera
import time
import itertools
from PIL import Image
from time import sleep

with picamera.PiCamera() as camera:
    camera.resolution = (640, 1000)
    camera.framerate = 24
    camera.start_preview()
    camera.annotate_text = 'Summer Cool '
    time.sleep(1)

    # Load the arbitrarily sized image
    img = Image.open('summer1.png')
    # Create an image padded to the required size with
    # mode 'RGB'
    pad = Image.new('RGB', (
        ((img.size[0] + 31) // 32) * 32,
        ((img.size[1] + 15) // 16) * 16,
        ))
    # Paste the original image into the padded one
    pad.paste(img, (0, 0))

    # Add the overlay with the padded image as the source,
    # but the original image's dimensions
    o = camera.add_overlay(pad.tostring(), size=img.size)
    # By default, the overlay is in layer 0, beneath the
    # preview (which defaults to layer 2). Here we make
    # the new overlay semi-transparent, then move it above
    # the preview
    o.alpha = 128
    o.layer = 3


    time.sleep(2)


     # Load the arbitrarily sized image
    img = Image.open('summer2.png')
    # Create an image padded to the required size with
    # mode 'RGB'
    pad = Image.new('RGB', (
        ((img.size[0] + 31) // 32) * 32,
        ((img.size[1] + 15) // 16) * 16,
        ))

    # Paste the original image into the padded one
    pad.paste(img, (0, 0))

    # Add the overlay with the padded image as the source,
    # but the original image's dimensions
    o = camera.add_overlay(pad.tostring(), size=img.size)
    # By default, the overlay is in layer 0, beneath the
    # preview (which defaults to layer 2). Here we make
    # the new overlay semi-transparent, then move it above
    # the preview
    o.alpha = 128
    o.layer = 3

    time.sleep(2)


     # Load the arbitrarily sized image
    img = Image.open('summer3.png')
    # Create an image padded to the required size with
    # mode 'RGB'
    pad = Image.new('RGB', (
        ((img.size[0] + 31) // 32) * 32,
        ((img.size[1] + 15) // 16) * 16,
        ))

    # Paste the original image into the padded one
    pad.paste(img, (0, 0))

    # Add the overlay with the padded image as the source,
    # but the original image's dimensions
    o = camera.add_overlay(pad.tostring(), size=img.size)
    # By default, the overlay is in layer 0, beneath the
    # preview (which defaults to layer 2). Here we make
    # the new overlay semi-transparent, then move it above
    # the preview
    o.alpha = 128
    o.layer = 3

    time.sleep(2)


     # Load the arbitrarily sized image
    img = Image.open('summer4.png')
    # Create an image padded to the required size with
    # mode 'RGB'
    pad = Image.new('RGB', (
        ((img.size[0] + 31) // 32) * 32,
        ((img.size[1] + 15) // 16) * 16,
        ))

    # Paste the original image into the padded one
    pad.paste(img, (0, 0))

    # Add the overlay with the padded image as the source,
    # but the original image's dimensions
    o = camera.add_overlay(pad.tostring(), size=img.size)
    # By default, the overlay is in layer 0, beneath the
    # preview (which defaults to layer 2). Here we make
    # the new overlay semi-transparent, then move it above
    # the preview
    o.alpha = 128
    o.layer = 3

    time.sleep(2)


     # Load the arbitrarily sized image
    img = Image.open('summer5.png')
    # Create an image padded to the required size with
    # mode 'RGB'
    pad = Image.new('RGB', (
        ((img.size[0] + 31) // 32) * 32,
        ((img.size[1] + 15) // 16) * 16,
        ))

    # Paste the original image into the padded one
    pad.paste(img, (0, 0))

    # Add the overlay with the padded image as the source,
    # but the original image's dimensions
    o = camera.add_overlay(pad.tostring(), size=img.size)
    # By default, the overlay is in layer 0, beneath the
    # preview (which defaults to layer 2). Here we make
    # the new overlay semi-transparent, then move it above
    # the preview
    o.alpha = 128
    o.layer = 3

    time.sleep(3)
