from django import forms
from .models import Recipe
from .models import Review


class RecipeForm(forms.ModelForm):
    CATEGORY_CHOICES = [
        ('breakfast', 'Breakfast'),
        ('lunch', 'Lunch'),
        ('dinner', 'Dinner'),
        ('dessert', 'Dessert'),
        ('snacks', 'Snacks'),
    ]

    SUBCATEGORY_CHOICES = [
        ('veg', 'Veg'),
        ('nonveg', 'Non-Veg'),
    ]

    category = forms.ChoiceField(choices=CATEGORY_CHOICES, required=True, label="Category")
    subcategory = forms.ChoiceField(choices=SUBCATEGORY_CHOICES, required=True, label="Veg/Non-Veg")

    class Meta:
        model = Recipe
        fields = ['title', 'category', 'subcategory', 'ingredients', 'instructions']

class RecipeSearchForm(forms.Form):
    query = forms.CharField(
        max_length=100, 
        required=False, 
        label="Search Recipes by Ingredients", 
        widget=forms.TextInput(attrs={'placeholder': 'Enter ingredient...'})
    )

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['reviewer', 'rating', 'comment']

        widgets = {
            'reviewer': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'}),
            'rating': forms.Select(attrs={'class': 'form-control'}),
            'comment': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Write your review...', 'rows': 4}),
        }