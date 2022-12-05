import flask
from flask import request
import functions as open_api
from html_template import html_template, html2json


app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return html_template()


@app.route('/api/getPdf', methods=['GET'])
def html_to_pdf():
    # return open_api.convert_to_pdf(request)
    return open_api.convert_to_pdf(html2json())


app.run()