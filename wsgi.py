import os
from testbot import application

if __name__ == '__main__':
    application.debug = True
    port = int(os.environ.get("PORT", 5000))
    application.run(host='0.0.0.0', port=port)