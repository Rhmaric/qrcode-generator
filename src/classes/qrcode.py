# -*- coding: utf-8 -*-

import qrcode

################################################################################
################################ QRcode Class ##################################
################################################################################

class QRCodeFactory:
    def __init__(self, prefix, dest, version, error_correction, box_size, border):
        self.prefix = prefix
        self.dest = dest
        self.version = version
        self.error_correction = error_correction
        self.box_size = box_size
        self.border = border

    def makeQRCode(self, data):
        qr = qrcode.QRCode(
            version=12,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=2,
            border=8
        )
        qr.add_data(f'{self.prefix}{data}')
        qr.make()
        img = qr.make_image()
        img.save(f'{self.dest}/{data}.png')