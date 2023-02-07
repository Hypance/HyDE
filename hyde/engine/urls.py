from django.urls import path
from engine import views
app_name = 'engine'
urlpatterns = [path('publish', views.my_pub_view, name='publish'),]