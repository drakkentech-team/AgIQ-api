from flask import *
from flask import send_file
import os
import io
from pyhtml2pdf import converter
import time

app = Flask(__name__)  
  

@app.route('/')  
def main():  
    return ""
  

@app.route('/api', methods=['GET'])
def html_to_pdf():  
    url = None
    delay = 5
    width = 15
    height = 16
    landscape = False
    filename = 'download'

    if request.args.get('src'):
        url = request.args.get('src')
    if request.args.get('d'):
        delay = request.args.get('d')
    if request.args.get("w"):
        width = request.args.get("w")
    if request.args.get("h"):
        height = request.args.get("h")
    if request.args.get("o"):
        landscape = True if request.args.get("o") == 'l' else False
    if request.args.get("n"):
        filename = request.args.get("n")

    time.sleep(int(delay))
    
    if url:
        the_file = converter.convert(url, 'html.pdf', print_options={"paperWidth": int(width), "paperHeight": int(height), "landscape": landscape, "displayHeaderFooter":False})
        file_path = 'html.pdf'
        return_data = io.BytesIO()
        with open(file_path, 'rb') as fo:
            return_data.write(fo.read())
        # (after writing, cursor will be at last byte, so move it to start)
        return_data.seek(0)
        os.remove(file_path)
        return send_file(return_data, mimetype='application/pdf',download_name= filename + '.pdf')
    else:
        return print("Error, please try again")
  

if __name__ == '__main__':  
    app.run(debug=True)