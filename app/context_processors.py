import os
from django.conf import settings
from django.utils import translation


# myapp/context_processors.py
def web_name(request):
    return {
        'baseurl': 'http://127.0.0.1:8000/',
        'web_name': 'LosariPost - Tegas, Cepat dan Berimbang',
        'webname': 'LosariPost',
        'address': 'Makassar',
        'telp': '0877 7579 5886',
        'fax': '(0411) 889464',
        'website': 'http://losaripost@admin.com',
        'email': 'losaripost@gmail.com',
        'instagram': '@losaripost',
        'created_by': 'hermantoXYZ',
    }

def versioned_static(request):
    """Context processor untuk versioning static files"""
    import time
    return {
        'STATIC_VERSION': int(time.time())
    }