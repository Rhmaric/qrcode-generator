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

Deactivate : 
`$ deactivate`

### Install Pip requirements

`$ pip install -r requirements.txt`

Freeze pip dependencies : 
`$ pip freeze > requirements.txt`

## Generate QRcode script
---

### Usage
Run `$ python generate.py` 

### Command line arguments

- Help command
Run `$ generate.py -h` for information