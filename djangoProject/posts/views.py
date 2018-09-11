# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import pdb
import os
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from app import get_string,src_path
from django.http import HttpResponse
# Create your views here.

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
def index(request):
    target = os.path.join(APP_ROOT, 'static\\')
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage(location=target)
        print(target)
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        print(uploaded_file_url)
        img_src =  uploaded_file_url
        print(img_src)
        text_from_img = get_string(uploaded_file_url)
        #print(text_from_img)
        return render(request, 'index.html', {
            'text_from_img': text_from_img,'image_src':img_src
        })
    return render(request,'index.html')