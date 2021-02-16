# qrcode-generator
very small python script to generate qrcode images

## Installation
---

### Technical Requirements

- Your Python's version must be greater than 2.7.10 or (3.9.1 if your are using Python3). 
Run `$ python --version` to check your Python's version

- Make sure `virtualenv` is installed - see [installation guide](https://virtualenv.pypa.io/en/latest/installation.html)

- Make sure a Python virtual env exists for your project. 
Run `$ virtualenv env` to create one

### Activate Python VirtualEnv

`$ source env/bin/activate`

Deactivate: 
`$ deactivate`

### Install Pip requirements

`$ pip install -r requirements.txt`

Freeze pip dependencies: 
`$ pip freeze > requirements.txt`

## Generate QRcode script
---

### Usage
Run `$ python src/generate.py <csvFilePath> -d <qrCodeDestination> -p <qrCodePrefix> -l <addQrCodeLabel>` 

### Command line arguments

- **csvFilePath**: [path] this is the path to your csv file. This csv file must contain unique ids in a single row.

- **qrCodeDestination** (option `-d` or `--dest`): [path] this is the path where all the generated QRcodes will be stored

- **qrCodePrefix** (option `-p` or `--prefix`): [string] you can provide a prefix (e.g an url) that will be added to each qrCode encryted data

- **addQrCodeLabel** (option `-l` or `--label`): [boolean] you can add a label on each QRCode image. This feature is disabled by default. Label will be added to the bottom center of each qrCode image 

- Help command
Run `$ python src/generate.py -h` for information