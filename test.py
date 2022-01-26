from products.models import *


def join_products():
    print('----start----')
    products_all = Product.objects.get.all()
    print(products_all)
    return 'test-success'


s = join_products()
print(s)
