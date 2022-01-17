# from django.shortcuts import render
#
# from search.documents import AddressDocument
#
#
# def search(request):
#     q = request.GET.get('q')
#
#     if q:
#         addresses = AddressDocument.search().query("match", full_address=q)
#     else:
#         addresses = ''
#
#     return render(request, 'search/search.html', {'addresses': addresses})
