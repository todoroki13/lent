from django.urls import path
from .views import *

urlpatterns = [
    path('', LogListt.as_view(), name='log_list'),
    path('person/', LogListp.as_view(), name='log_list'),
    
    path('createtype/', LogCreatet.as_view(), name='log_create'),
    path('createperson/', LogCreatep.as_view(), name='log_create'),
    path('createitem/', LogCreatei.as_view(), name='log_create'),
    path('createborrow/', LogCreateb.as_view(), name='log_create'),
    path('createborrows/<int:aid>', LogCreatebs.as_view(), name='log_create'),
    path('createborrowp/<int:eid>', LogCreatebp.as_view(), name='log_create'),
    
    path('<int:pk>/', LogViewt.as_view(), name='log_view'),
    path('person/<int:pk>/', LogViewp.as_view(), name='log_view'),
    path('item/<int:pk>/', LogViewi.as_view(), name='log_view'),
]