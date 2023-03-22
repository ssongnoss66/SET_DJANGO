from django.shortcuts import render
import random

# Create your views here.
def berners_lee(request):
    return render(request, 'berners_lee/berners_lee.html')

def index(request):
    context = {
        'name': 'SsongnosS'
    }
    return render(request, 'berners_lee/index.html', context)


def dinner(request):
    foods = ['pizza', 'hamburger', 'bibimbap', 'bulgogi']
    picked = random.choice(foods)
    context = {
        'foods': foods,
        'picked': picked,
    }
    return render(request, 'berners_lee/dinner.html', context)

def search(request):
    return render(request, 'berners_lee/search.html')

def throw(request):
    return render(request, 'berners_lee/throw.html')

def catch(request):
    print(request)                      # <WSGIRequest: GET '/catch/?message=DJANGO'>
    print(type(request))                # <class 'django.core.handlers.wsgi.WSGIRequest'>
    print(dir(request))                 # ['COOKIES', 'FILES', 'GET', 'META', 'POST', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_current_scheme_host', '_encoding', '_get_full_path', '_get_post', '_get_raw_host', '_get_scheme', '_initialize_handlers', '_load_post_and_files', '_mark_post_parse_error', '_messages', '_read_started', '_set_content_type_params', '_set_post', '_stream', '_upload_handlers', 'accepted_types', 'accepts', 'body', 'build_absolute_uri', 'close', 'content_params', 'content_type', 'csrf_processing_done', 'encoding', 'environ', 'get_full_path', 'get_full_path_info', 'get_host', 'get_port', 'get_raw_uri', 'get_signed_cookie', 'headers', 'is_ajax', 'is_secure', 'method', 'parse_file_upload', 'path', 'path_info', 'read', 'readline', 'readlines', 'resolver_match', 'scheme', 'session', 'upload_handlers', 'user']
    print(request.GET)                  # <QueryDict: {'message': ['DJANGO']}>
    print(request.GET.get('message'))   # DJANGO
    data = request.GET.get('message')
    context = {
        'data': data,
    }
    return render(request, 'berners_lee/catch.html', context)