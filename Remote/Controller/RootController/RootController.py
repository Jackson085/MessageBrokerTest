from flask import Blueprint, jsonify

from Commons.Constants import AppVersion

root_app = Blueprint('RootController', __name__)


@root_app.route('/version', methods=['GET'])
def version():
    version_dto = AppVersion.Version
    return jsonify(version_dto.__dict__)


@root_app.route('/', methods=['GET'])
def root():
    return root_app.send_static_file('index.html')


@root_app.route('/<path:filename>')
def serve_static(filename):
    return root_app.send_static_file(filename)
