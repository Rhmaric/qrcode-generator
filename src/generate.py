# -*- coding: utf-8 -*-
# see https://note.nkmk.me/en/python-pillow-qrcode/ for more information

################################################################################
############################## QRcode Generator ################################
################################################################################

import qrcode
import csv
import argparse
from classes.qrcode import QRCodeFactory

def generate(csvPath, qrCodeDest, qrCodePrefix, iconPath='assets/icons'):
    # TODO : add feature iconPath
    factory = QRCodeFactory(
        qrCodePrefix,
        qrCodeDest,
        version=7,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4
    )

    with open(csvPath, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        for ids in reader:
            for id in ids:
                if id:
                    factory.makeQRCode(data=id)

def parseArgs():
    parser = argparse.ArgumentParser(description='Command to generate unique QRcodes from a csv file')
    parser.add_argument('csvPath', type=str, default='', help='path to the csv file')
    parser.add_argument('-d', '--dest', dest='qrCodeDest', type=str, default='assets/qrcode',
        help='path where all the generated QRcodes will be stored')
    parser.add_argument('-p', '--prefix', dest='qrCodePrefix', type=str, default='',
        help='prefix that will be added to each qrCode data')
    args = parser.parse_args()
    
    return [args.csvPath, args.qrCodeDest, args.qrCodePrefix]


if __name__ == '__main__':
    # Parse command line arguments
    csvPath, qrCodeDest, qrCodePrefix = parseArgs()
    # Generate QRCodes
    generate(csvPath, qrCodeDest, qrCodePrefix)
