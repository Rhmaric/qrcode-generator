# qrcode-generator
very small python script to generate qrcode images

## Installation
---

### Technical Requirements

- Your Python's version must be greater than 2.7.10 or (3.9.1 if your are using Python3)
run `$ python --version` to check your Python's version

- Make sure `virtualenv` is installed - see [installation guide](https://virtualenv.pypa.io/en/latest/installation.html)

- Make sure a Python virtual env exists for your project
`$ virtualenv env`

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
Run `$ python src/generate.py -p <csvFilePath> -d <qrCodeDestination> -f <qrCodePrefix>` 

### Command line arguments

- **csvFilePath** (option `-p` or `--path`): this is the path to your csv file. This csv file must contain unique ids in a single row.

- **qrCodeDestination** (option `-d` or `--dest`): this is the path where all the generated QRcodes will be stored

- **qrCodePrefix** (option `-f` or `--prefix`): [optional] you can provide a prefix (e.g an url) that will be added to the qrCode encryted data 

- Help command
Run `$ python src/generate.py -h` for information