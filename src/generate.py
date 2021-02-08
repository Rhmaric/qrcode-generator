# -*- coding: utf-8 -*-

################################################################################
############################## QRcode Generator ################################
################################################################################

import qrcode
import csv
from classes.qrcode import QRCodeFactory

def generate(csvPath, qrCodeDest =  'assets/qrcode', qrCodePrefix =  '', iconPath = 'assets/icons'):
    # TODO : add feature iconPath
    factory = QRCodeFactory(
        qrCodePrefix,
        qrCodeDest,
        version=12,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=2,
        border=8
    )

    with open(csvPath, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        for ids in reader:
            for id in ids:
                if id:
                    factory.makeQRCode(data=id)

if __name__ == '__main__':
    generate('/Users/romaric/Desktop/id.csv',  qrCodePrefix = 'https://atipik-solutions.com/api/v1/')
