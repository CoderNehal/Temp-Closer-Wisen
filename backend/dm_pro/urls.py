from django.urls import path
from . import views
from .views import *


urlpatterns = [
    path('',views.home,name="home"),
    path('assignment1/',views.assignment1,name="assignment1"),
    path('assignment2/',views.assignment2,name="assignment2"),
    path('assignment3/',views.assignment3,name="assignment3"),
    path('assignment3/confuse_matrix/',views.assignment3_confuse_matrix,name="assignment3_confuse_matrix"),
    path('assignment4/',views.assignment4,name="assignment4"),
    path('assignment5/',views.assignment5,name="assignment5"),
    path('api/upload-csv/', CSVFileUploadView.as_view(), name='upload-csv-api'),



]