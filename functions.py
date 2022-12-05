import pdfkit
from io import BytesIO
from flask import send_file


def convert_to_pdf(request):
    keys = list(request.keys())
    html = request[keys[0]]
    config = pdfkit.configuration(wkhtmltopdf=r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe")
    the_file = BytesIO(pdfkit.from_string(html, configuration=config))
    the_file.seek(0)
    filename = str(f"download.pdf")
    return send_file(the_file, as_attachment=True, attachment_filename=filename)
