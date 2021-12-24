from django.urls import path
from .views import *

urlpatterns = [
    path('', LogListt.as_view(), name='log_list'),
    path('person/', LogListp.as_view(), name='log_list'),
    
    path('createtype/', LogCreatet.as_view(), name='log_create'),
    path('createperson/', LogCreatep.as_view(), name='log_create'),
    path('createitem/', LogCreatei.as_view(), name='log_create'),
    path('createitemsl/<int:iid>', LogCreateisl.as_view(), name='log_create'),
    path('createborrow/', LogCreateb.as_view(), name='log_create'),
    path('createborrows/<int:aid>', LogCreatebs.as_view(), name='log_create'),
    path('createborrowp/<int:eid>', LogCreatebp.as_view(), name='log_create'),
    
    path('<int:pk>/', LogViewt.as_view(), name='log_view'),
    path('person/<int:pk>/', LogViewp.as_view(), name='log_view'),
    path('item/<int:pk>/', LogViewi.as_view(), name='log_view'),

    path('<int:pk>/update', LogUpdatet.as_view(), name='log_update'),
    path('item/<int:pk>/update', LogUpdatei.as_view(), name='log_update'),
    path('person/<int:pk>/update', LogUpdatep.as_view(), name='log_update'),
    path('borrow/<int:pk>/update', LogUpdateb.as_view(), name='log_update'),

    path('<int:pk>/delete', LogDeletet.as_view(), name='log_delete'),
    path('item/<int:pk>/delete', LogDeletei.as_view(), name='log_delete'),
    path('person/<int:pk>/delete', LogDeletep.as_view(), name='log_delete'),
    path('borrow/<int:pk>/delete', LogDeleteb.as_view(), name='log_delete'),
]