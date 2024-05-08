from django.shortcuts import render
from .models import *
from django.http import JsonResponse

# Create your views here.
def get_Hotel(request):
    try:
        Hotel_objs=Hotel.objects.all()
        
        if request.GET.get('sort_by'):
            sort_by_value=request.GET.get('sort_by')
            if sort_by_value == 'asc':
                Hotel_objs = Hotel_objs.order_by('Hotel_price')
            elif sort_by_value == "dsc":
                Hotel_objs=Hotel_objs.order_by('-Hotel_price')

        if request.GET.get('amount'):
            amount = request.GET.get('amount')
            Hotel_objs = Hotel_objs.filter(Hotel_price_lte = amount)

            if request.GET.get('amenities'):
                amenities = request.GET.get('amenities')
                amenities = str(amenities).split(',')
                am = []
                for amenities in amenities:
                    am.append(int(amenity))

                    Hotel_objs = Hotel_objs.filter(amenities__in = am).distinct()


        payload = []
        for Hotel_obj in Hotel_objs:
            payload.append({
                'Hotel_name': Hotel_obj.Hotel_name,
                'Hotel_price': Hotel_obj.Hotel_price,
                'Hotel_description':Hotel_obj.Hotel_description,
                'banner_image':str(Hotel_obj.banner_image),
            })

            return JsonResponse(payload,safe=False)
        
    except Exception as e:
        print(e)

    return JsonResponse({'message':'something went wrong'})
