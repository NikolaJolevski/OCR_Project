# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import pdb
import os
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from app import get_string,src_path
from django.views.decorators.csrf import  csrf_exempt
from django.http import JsonResponse
from django.http import HttpResponse
# Create your views here.
lang_list = [
    {
        "id": "eng",
        "name": "English"
    },
    {
        "id": "bos",
        "name": "Bosnian"
    },
    {
        "id": "bul",
        "name": "Bulgarian"
    },
    {
        "id": "ces",
        "name": "Czech"
    },
    {
        "id": "deu",
        "name": "German"
    },
    {
        "id": "fra",
        "name": "French"
    },
    {
        "id": "hrv",
        "name": "Croatian"
    },
    {
        "id": "eng",
        "name": "English"
    },
    {
        "id": "ita",
        "name": "Italian"
    },
    {
        "id": "mkd",
        "name": "Macedonian"
    },
    {
        "id": "rus",
        "name": "Russian"
    },
    {
        "id": "slv",
        "name": "Slovenian"
    },
    {
        "id": "srp",
        "name": "Serbian"
    },
    {
        "id": "tur",
        "name": "Turkish"
    }
]
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
def index(request):
    target = os.path.join(APP_ROOT, 'static\\')

    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage(location=target)
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        img_src =  uploaded_file_url
        lang = request.POST['lang']
        text_from_img = get_string(uploaded_file_url, lang)
        #print(text_from_img)
        return render(request, 'index.html', {
            'text_from_img': text_from_img,'image_src':img_src, 'lang_list': lang_list
        })
    elif request.method == 'POST':
        return render(request, 'index.html', {
            'error_msg': "Please choose your image", 'lang_list': lang_list
        })
    return render(request,'index.html', {
        'lang_list': lang_list
    })

@csrf_exempt
def webcam(request):

    target = os.path.join(APP_ROOT, 'static\\')

    if request.method == 'POST':
        myfile = request.FILES['webcam']
        fs = FileSystemStorage(location=target)
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        img_src = '/static/' + uploaded_file_url
        text_from_img = get_string(uploaded_file_url, "eng")
        data = {
            'text_from_img' : text_from_img,
            'image_src' : img_src
        }
        return JsonResponse(data,safe=False)

    return render(request,'webcam.html')
