from django.db import models

# Create your models here.
class amenities (models.Model):
    amenity = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self) -> str:
        return self.amenity

class Hotel (models.Model):
    Hotel_name = models.CharField(max_length=100)
    Hotel_price = models.IntegerField()
    Hotel_description = models.TextField()
    amenities = models.ManyToManyField(amenities)
    banner_image = models.ImageField(upload_to='Hotels')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.Hotel_name
    
    def get_emenities(self):
        payload = []

        for amenity in self.amenities.all():
            payload.append({'id':amenity.id, 'amenity':amenity.amenity})
            return payload


class HotelImage(models.Model):
    Hotel = models.ForeignKey(Hotel, on_delete= models.CASCADE)
    Image = models.ImageField(upload_to='Hotels')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self) -> str:
        return self.Hotel.Hotel_name
