from flask import jsonify
from .routes import graphql_routes, rest_routes
from .bootstrap import app
from .constants import HOST, PORT, DEBUG

@app.route('/')
def welcome():
    return jsonify('Welcome')

@app.errorhandler(404)
def page_not_found(error):
    return { 'result': 'not_found' }, 404

@app.errorhandler(Exception)
def exception_occur(error):
    return { 'result': error.args[0] if len(error.args) else error.args}, 500

graphql_routes()
rest_routes()

def run_server():
    app.run(host=HOST, port=PORT, debug=DEBUG)
