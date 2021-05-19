import json
import random
from typing import Text

from django.http     import JsonResponse
from django.views    import View

from products.models import Product

class ProductView(View):
    def get(self,request):
        product_id = request.GET.get('id', None)
        if not product_id:     
            return JsonResponse({'MESSAGE':'NOT_FOUND_ID'}, status=400)   
        if int(product_id) > Product.objects.count():
            return JsonResponse({'MESSAGE':'NOT_FOUND_PRODUCT'}, status=400)   
        
        product    = Product.objects.get(id=product_id)
        productdetail = {
            'images'           : [product_images.url for product_images in product.productimage_set.all()],
            'menu'             : product.category.menu.name,
            'category'         : product.category.name,
            'name'             : product.name,
            'cost'             : product.cost,
            'clicks'           : product.clicks,
            'description'      : product.description_iamge_url,
            'size'             : [product_size.name for product_size in product.size_set.all()]
        }
        return JsonResponse({'productdetail':productdetail}, status=200)
