from django.urls import path
from .views import HomePageView , EditPageView , DeletePageView , CreatePageView

urlpatterns = [
    path('', HomePageView , name='home'),
    path('edit/', EditPageView, name='edit_data'),
    path('delete/', DeletePageView, name='delete_data'),
    path('create/', CreatePageView, name='create_data')
]
