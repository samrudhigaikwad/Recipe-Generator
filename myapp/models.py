from django.db import models

from django.db import models

from django.db import models
from django.contrib.auth.models import User


# User Role Model
class UserProfile(models.Model):
    ROLE_CHOICES = [
        ('user', 'User'),
        ('chef', 'Chef'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

    def str(self):
        return self.user.username

#recipe model
class Recipe(models.Model):
    CATEGORY_CHOICES = [
        ('Breakfast', 'Breakfast'),
        ('Lunch', 'Lunch'),
        ('Dinner', 'Dinner'),
        ('Dessert', 'Dessert'),
        ('Snacks', 'Snacks'),
    ]

    SUBCATEGORY_CHOICES = [
        ('Veg', 'Veg'),
        ('Non-Veg', 'Non-Veg'),
    ]

    title = models.CharField(max_length=255)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    subcategory = models.CharField(max_length=50, choices=SUBCATEGORY_CHOICES, blank=True, null=True)
    short_description = models.CharField(max_length=300, blank=True, null=True)
    ingredients = models.TextField()
    instructions = models.TextField()
    image = models.ImageField(upload_to='recipe_images/', blank=True, null=True)

    def __str__(self):
        return self.title

# Categories Model
class Category(models.Model):
    CATEGORY_CHOICES = [
        ('breakfast', 'Breakfast'),
        ('lunch', 'Lunch'),
        ('dinner', 'Dinner'),
        ('desserts', 'Desserts'),
        ('snacks', 'Snacks'),
    ]
    cat_name = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    is_veg = models.BooleanField(default=True)  # Veg/Non-Veg

    def str(self):
        return self.name
    
    from django.db import models



class Review(models.Model):
    recipe = models.ForeignKey('Recipe', on_delete=models.CASCADE, related_name='reviews',null=True, blank=True)
    reviewer = models.CharField(max_length=100, null=True, blank=True)
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])  # Rating from 1 to 5
    comment = models.TextField(null=True, blank=True)  # Review text
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp

    def __str__(self):
        return f"{self.reviewer} - {self.rating} Stars"
