import os

from flask import Flask

from Remote.Controller.RootController.RootController import root_app

base_path = "../wwwroot"

root_app.static_folder = os.path.abspath(os.path.join(base_path, "root/browser"))


app = Flask(__name__)


app.register_blueprint(root_app)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
