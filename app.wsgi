activate_this = '/home/ubuntu/string2words/venv/bin/activate_this.py'
with open(activate_this) as f:
   exec(f.read(), dict(__file__=activate_this))

import sys
import logging

logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/html/string2words/")

from app import app as application
