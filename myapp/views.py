from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib import messages
from .models import Recipe
from .forms import RecipeForm, ReviewForm
from .models import Review

# Function to check if the user is an admin
def is_admin(user):
    return user.is_staff

def home(request):
    recipes = Recipe.objects.all()
    return render(request, 'home.html', {'recipes': recipes})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.is_staff = False  # Ensuring the user is not an admin
            user.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def signin(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'signin.html', {'form': form})

def signout(request):
    logout(request)
    return redirect('signin')

@login_required
@user_passes_test(is_admin)  # Only admins can add recipes
def add_recipe(request):
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
    
    if request.method == 'POST':
        title = request.POST.get('title')
        category = request.POST.get('category')
        short_description = request.POST.get('short_description')
        subcategory = request.POST.get('subcategory')
        ingredients = request.POST.get('ingredients')
        instructions = request.POST.get('instructions')
        image = request.FILES.get('image')  

        if title and category and subcategory and ingredients and instructions:
            Recipe.objects.create(
                title=title,
                category=category,
                short_description=short_description,
                subcategory=subcategory,
                ingredients=ingredients,
                instructions=instructions,
                image=image  
            )
            return redirect('home')
        
    return render(request, 'add_recipe.html', {'categories': CATEGORY_CHOICES, 'subcategories': SUBCATEGORY_CHOICES})

def recipe_list(request):
    recipes = Recipe.objects.all()
    return render(request, 'list.html', {'recipes': recipes})

@login_required
@user_passes_test(is_admin)   
def update_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    
    if request.method == 'POST':
        recipe.title = request.POST.get('title', recipe.title)
        recipe.category = request.POST.get('category', recipe.category)
        recipe.short_description = request.POST.get('short_description', recipe.short_description)
        recipe.subcategory = request.POST.get('subcategory', recipe.subcategory)
        recipe.ingredients = request.POST.get('ingredients', recipe.ingredients)
        recipe.instructions = request.POST.get('instructions', recipe.instructions)
        
        if 'image' in request.FILES:
            recipe.image = request.FILES['image']
        
        recipe.save()
        return redirect('home')
    
    return render(request, 'update_recipe.html', {'recipe': recipe})

@login_required
@user_passes_test(is_admin)  # Only admins can delete recipes
def delete_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    recipe.delete()
    return redirect('home')

def recipe_detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    reviews = Review.objects.filter(recipe=recipe).order_by('-created_at')  # Fetch reviews for this recipe

    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.recipe = recipe  # Associate review with recipe
            if request.user.is_authenticated:
                review.reviewer = request.user.username  # Assign username if logged in
            review.save()
            return redirect('recipe_detail', recipe_id=recipe.id)
    else:
        form = ReviewForm()

    return render(request, 'recipe_detail.html', {'recipe': recipe, 'reviews': reviews, 'form': form})


@login_required
def recipe_category(request, category):
    recipes = Recipe.objects.filter(category=category)
    return render(request, 'recipe_category.html', {'recipes': recipes, 'category': category})

def recipe_subcategory(request, category, subcategory):
    recipes = Recipe.objects.filter(category=category, subcategory=subcategory)
    return render(request, 'recipe_subcategory.html', {'recipes': recipes, 'category': category, 'subcategory': subcategory})

def search_recipe(request, category, subcategory):
    query = request.GET.get('q')
    recipes = Recipe.objects.filter(category=category, subcategory=subcategory)
    
    if query:
        recipes = recipes.filter(ingredients__icontains=query)

    return render(request, 'recipe_subcategory.html', {'recipes': recipes, 'category': category, 'subcategory': subcategory, 'query': query})
 

 

def review_view(request):
    reviews = Review.objects.all().order_by('-created_at')  # Fetch all reviews, newest first

    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()  # Save the review
            return redirect('reviews')  # Redirect to the same page after submission
    else:
        form = ReviewForm()

    return render(request, 'review.html', {'form': form, 'reviews': reviews})