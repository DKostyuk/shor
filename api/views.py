from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.views.decorators.csrf import csrf_exempt
from api.serializer import *
from products.models import Product
from rest_framework.response import Response
import json
from django.contrib import auth
from rest_framework import status


@api_view(["GET"])
def product_category(request):
    product_lines = ProductCategory.objects.filter(is_active=True).order_by('id')
    products = Product.objects.filter(is_active=True)
    p_images = ProductImage.objects.filter(is_active=True, is_main=True)
    list_product_lines = []
    all_products_list_dic = []
    for i in product_lines:
        list_product_lines.append(i.name)
        all_products_dic = {'line_id': i.id, 'p_line_name': i.name, 'product': []}
        for p in products:
            if p.category == i:
                for pi in p_images:
                    if pi.product == p:
                        all_products_dic['product'].append({'line_id': p.id, 'p_name': p.name,
                                                            'p_name_ua': p.name_pl,
                                                            'name_d': p.name_description, 'd': p.description,
                                                            'name_d_1': p.name_description_1, 'd_1': p.description_1,
                                                            'name_d_2': p.name_description_2, 'd_2': p.description_2,
                                                            'name_d_3': p.name_description_3, 'd_3': p.description_3,
                                                            'd_4': p.description_4, 'd_5': p.description_5,
                                                            'p_reg_number': p.product_ref_number,
                                                            'p_image': pi.image.url})
        all_products_list_dic.append(all_products_dic)

    serialized_data = json.dumps(all_products_list_dic)  # Serialize the dictionary to JSON
    serializer = ProductCategorySerializer(list_product_lines, many=True)
    # return Response(list_product_lines)
    return JsonResponse(serialized_data, safe=False)


@api_view(["GET"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def welcome(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    content = {"message": "Welcome to the BookStore!"}
    print(serializer.data)
    return Response(serializer.data)


@api_view(['POST'])
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    if request.POST:
        print('POST request received')
        user_email = request.POST.get('username', '').lower().replace(' ', '')
        print(user_email)
        password = request.POST.get('password', '')
        print(password)
        username = auth.authenticate(username=user_email, password=password)
        print('username:  ', username)
        user_old = User.objects.filter(username=user_email).first()
        if user_old and username is None:
            user_old.is_active = True
            user_old.save()
            auth.login(request, user_old)
            return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
        elif user_old is None:
            login_error = 'Email ' + str(user_email) + " не зарегистрирован. Пожалуйста, зарегистрируйтесь"
            return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
        else:  # only left one condition - that == username is not None
            user_data = {
                "username": username.username,
                "email": username.email,
                'text_q': 'URA'
                # Add other user data fields as needed
            }
            return Response(user_data, status=status.HTTP_200_OK)
    else:
        print('QWERTY  request received')
        # return render(request, 'landing/login.html', locals())

    # user = authenticate(username=username, password=password)
    # if user is not None:
    #     # User authenticated, return user data as JSON response
    #     user_data = {
    #         "username": user.username,
    #         "email": user.email,
    #         # Add other user data fields as needed
    #     }
    #     return Response(user_data)
    # else:
    #     # Authentication failed
    #     return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)



