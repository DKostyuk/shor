from django.shortcuts import render
from addresses.models import *


# def cosmetolog(request, cosmetolog_id):
#     cosmetolog = Cosmetolog.objects.get(id=cosmetolog_id)
#
#     session_key = request.session.session_key
#     if not session_key:
#         request.session.cycle_key()
#
#     print (request.session.session_key)
#
#     return render(request, 'cosmetologs/cosmetolog.html', locals())
#
#
# def service(request, service_product_id):
#     service_product = ServiceProduct.objects.get(id=service_product_id)
#
#     session_key = request.session.session_key
#     if not session_key:
#         request.session.cycle_key()
#
#     print (request.session.session_key)
#
#     return render(request, 'cosmetologs/service.html', locals())
