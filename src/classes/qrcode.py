# -*- coding: utf-8 -*-

import qrcode
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

################################################################################
################################ QRcode Class ##################################
################################################################################

class QRCodeFactory:
    def __init__(self, prefix, dest, addLabel, version, error_correction, box_size, border):
        # QRcode attributes
        self.prefix = prefix
        self.dest = dest
        self.addLabel = addLabel
        self.version = version
        self.error_correction = error_correction
        self.box_size = box_size
        self.border = border
        
        # Text Label attributes
        self.labelSize = 25
        self.labelFontFamily = "fonts/Arial.ttf" # see fonts folder for available fonts
        self.labelFont = ImageFont.truetype(self.labelFontFamily, self.labelSize)
        self.labelColor = (0, 0, 0)

    def makeQRCode(self, data):
        # Create QRCode image
        qr = qrcode.QRCode(
            version=self.version,
            error_correction=self.error_correction,
            box_size=self.box_size,
            border=self.border
        )
        qr.add_data(f'{self.prefix}{data}')
        qr.make()
        img = qr.make_image().convert('RGB')
        # Add bottom-centered text label
        draw = ImageDraw.Draw(img)
        W, H = img.size
        w, h = draw.textsize(data)
        draw.text(((W-w)/2, H-5*h/2), data, self.labelColor, font=self.labelFont)
        # Save image
        img.save(f'{self.dest}/{data}.png')