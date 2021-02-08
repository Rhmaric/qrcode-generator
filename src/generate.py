# -*- coding: utf-8 -*-
# see https://note.nkmk.me/en/python-pillow-qrcode/ for more information

################################################################################
############################## QRcode Generator ################################
################################################################################

import qrcode
import csv
import sys, getopt
from classes.qrcode import QRCodeFactory

def generate(csvPath, qrCodeDest, qrCodePrefix, iconPath='assets/icons'):
    # TODO : add feature iconPath
    factory = QRCodeFactory(
        qrCodePrefix,
        qrCodeDest,
        version=12,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=2,
        border=8
    )

    with open(csvPath, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        for ids in reader:
            for id in ids:
                if id:
                    factory.makeQRCode(data=id)

def getArgs(argv):
    csvPath = ''
    qrCodeDest = 'assets/qrcode'
    qrCodePrefix = ''
    
    try:
        opts, args = getopt.getopt(argv, "hp:d:f:",["path=","dest=", "prefix="])
    except getopt.GetoptError:
        print('generate.py -p <csvFilePath> -d <qrCodeDestination> -f <qrCodePrefix>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('generate.py -p <csvFilePath> -d <qrCodeDestination> -f <qrCodePrefix>')
            sys.exit()
        elif opt in ("-p", "--path"):
            csvPath = str(arg)
        elif opt in ("-d", "--dest"):
            qrCodeDest = str(arg)
        elif opt in ("-f", "--prefix"):
            qrCodePrefix = str(arg)

    return [csvPath, qrCodeDest, qrCodePrefix]


if __name__ == '__main__':
    csvPath, qrCodeDest, qrCodePrefix = getArgs(sys.argv[1:])
    generate(csvPath, qrCodeDest, qrCodePrefix)
