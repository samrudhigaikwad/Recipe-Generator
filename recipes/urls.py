

from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from myapp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('', views.signin, name='signin'),
    path('signout/', views.signout, name='signout'),
    path('add/', views.add_recipe, name='add_recipe'),
    path('list/', views.recipe_list, name='list'),

    path('recipe/<int:recipe_id>/', views.recipe_detail, name='recipe_detail'),
    path('recipe/<int:recipe_id>/update/', views.update_recipe, name='update_recipe'),
    path('recipe/<int:recipe_id>/delete/', views.delete_recipe, name='delete_recipe'),
    # path('recipe/<int:recipe_id>/review/', views.add_review, name='add_review'),

    # Category and Subcategory Filtering
    path('category/<str:category>/', views.recipe_category, name='recipe_category'),
    path('category/<str:category>/<str:subcategory>/', views.recipe_subcategory, name='recipe_subcategory'),

    # Search Recipe in Subcategory
    path('category/<str:category>/<str:subcategory>/search/', views.search_recipe, name='search_recipe'),
    path('reviews/', views.review_view, name='reviews'),
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)