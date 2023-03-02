from django.urls import path
from . import views


urlpatterns = [
    
    # using  an empty tring here makes this our root route
    # views . home renders refers to a file that  render views 
    # the name  = 'home'
    #
    #
    path( '', views.home, name ='home'),
    path('about/', views.about, name='about')
]