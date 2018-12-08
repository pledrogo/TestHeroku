from flask import Flask
import os
import json

application = Flask(__name__)


@application.route('/Z3AELDdzzE09KLk210jNbcDuY8jnd0823x42163s53&d23hJMzaAsq02/')
def hello_world():

    return os.environ.get('TEST_TOKEN','na')
