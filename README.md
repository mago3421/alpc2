# string2words Install and Usage Guide
### To install, use a virtual environment
`sudo apt-get install virtualenv -u`
`virtualenv venv --python=$(which python3)`
### Activate the virtual environment
`source venv/bin/activate`
### Then, install the package
`pip install string2words`
### Install Flask and the other requirements
`pip install -r requirements`
### To use, activate a python shell with the virtual environment activated
`python`
### Then, you may use the encode and decode functions
`encode('marc')`
`decode(267653579)`

