import json
from django.views.decorators.csrf import csrf_exempt
import models
from django.http import HttpResponse


@csrf_exempt
def index(request):
    return HttpResponse("Hello, world. You're at the index.")


@csrf_exempt
def insert(request):
    if not request.POST:
        return HttpResponse('please use post method', content_type="application/json")
    user_info = models.User()
    if user_info.find(user_name=request.POST.get('user_name')):
        return HttpResponse('please use another use name', content_type="application/json")
    data =dict(request.POST)
    user_info.insert(**data)
    return HttpResponse('True', content_type="application/json")


@csrf_exempt
def login(request):
    if not request.POST:
        return HttpResponse('please use post method', content_type="application/json")
    user_info = models.User()
    if not (request.POST.get('user_name') and request.POST.get('pass_word')):
        return HttpResponse('please provide user_name and  pass_word', content_type="application/json")
    if user_info.find(user_name=request.POST.get('user_name'),pass_word=request.POST.get('pass_word')):
        return HttpResponse('True', content_type="application/json")
    return HttpResponse('False', content_type="application/json")

@csrf_exempt
def search(request):
    if not request.GET:
        return HttpResponse('please use GET method', content_type="application/json")
    user_info = models.User()
    print request.GET
    data =dict(request.GET)
    find_elements=user_info.findall(**data)
    if find_elements:
        return HttpResponse(find_elements, content_type="application/json")
    return HttpResponse('Nothing Found', content_type="application/json")

@csrf_exempt
def show_files(request):
    if not request.POST:
        return HttpResponse('please use POST method', content_type="application/json")
    file_info = models.Showfiles()
    print request.GET
    path =request.POST.get('path')
    if not path:
        return HttpResponse('please use path variable while post', content_type="application/json")
    find_elements=file_info.find(path=path)
    if find_elements:
        return HttpResponse(find_elements, content_type="application/json")

@csrf_exempt
def mongostatus(request):
    mongo_info = models.Services()
    status =mongo_info.mongo_status()
    return HttpResponse(status, content_type="application/json")

