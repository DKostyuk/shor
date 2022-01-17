# from django_elasticsearch_dsl import Document, Index
# from blog.models import Post
# from addresses.models import Address

# addresses = Index('addresses')
#
#
# @addresses.doc_type
# class AddressDocument(Document, 'Django'):
#     class Meta:
#         model = Address
#
#         fields = [
#             'name',
#             'full_address',
#             'display_address',
#             'url',
#             'description',
        # ]