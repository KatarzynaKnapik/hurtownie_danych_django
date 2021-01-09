from django.shortcuts import render
from django.http import HttpResponse
from xhtml2pdf import pisa 
from . import pdf_creator 

def index(request):
    context = {
        'title': 'Hurtownie danych - 2020/2021 - Scrapy',
        'authors_list': 'Knapik Katarzyna, Kwolek Krzystof, Lippa Andrzej'
    }
    return render(request, 'base.html', context)



def generate_PDF(request):
    pdf = pdf_creator.generate_PDF()

    response = HttpResponse(pdf, 'application/pdf')
    response['Content-Disposition'] = 'attachment; filename="{}"'.format('Raport.pdf')

    return response
    
