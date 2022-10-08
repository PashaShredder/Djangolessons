from django.urls import path, re_path, include
from django.views.decorators.cache import cache_page

from .views import *
from rest_framework import routers
from . import views

# router = routers.DefaultRouter()
# router.register(r'medicines', views.MedicinesViewSet)

# urlpatterns = [
#     path('', include(router.urls)),
#     path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
#     # path('some-api/', Medicines.objects.filter({'get': 'list'}))
#
# ]

urlpatterns = [
    path('', MedicinesHome.as_view(), name='home'),
    path('about/', about, name='about'),
    path('addpage/', AddPage.as_view(), name='add_page'),
    path('contact/', ContactFormView.as_view(), name='contact'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    path('category/<slug:cat_slug>/', MedicinesCategory.as_view(), name='category'),

]
