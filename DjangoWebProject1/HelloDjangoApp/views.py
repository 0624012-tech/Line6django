import http 
from django.shortcuts import render
from django.http import HttpResponse 
from datetime import datetime 
from .models import teacher
from pypdf import PdfWriter, PdfReader
from reportlab.pdfgen import canvas #Generating PDfs

# Create your views here.
def index(request):

    teach = teacher.objects.all()
    return render(request,"HelloDjangoApp/index.html", {'content':teach})

def report (request):


    try: 
        merger = PdfWriter()
        input1 = PdfReader(generate_pdf())
        input2 = pdfreader(pdf_file, "rb")

        merger.append(input1)
        merger.append(input2)

        buffer = BytesIO()
        merger.write(buffer)
        buffer.seek(0)
        response = FileResponse(generate_pdf(), as_attachment = true, filename="Attachment.pdf")
        
    except FilNotFoundError:
        response = FileResponse(generate_pdf(), as_attachment = true, filename="noAttachment.pdf")
        return response
def generate_pdf ():

    buffer = BytesIO()
    p = canvas.Canvas(buffer)
   
    lines = [('Name:', 'Teaching Area:')]

    for teach in teachers:
        lines.append((teach.Name, teach.Area))

    tables = Table(lines)
    table.wrapOn(p, 300, 300)
    table.drawOn(p, 10, 650)

    p.showPage()
    p.save()

    buffer.seek(0)
    return buffer