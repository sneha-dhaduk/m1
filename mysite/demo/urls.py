from django.urls import path
from . import views

urlpatterns = [
    path('forms/',views.forms,name='forms'),
    path('detail/',views.detail,name='detail'),

    path('create/', views.StudentCreateView.as_view(), name='create'),
    path('list/', views.StudentListView.as_view(), name='list'),
    path('<pk>/update/', views.StudentUpdateView.as_view(), name='update'),

    path('employeeform/',views.employeeCreateView.as_view(),name='employeeform'),
    path('employeelist/',views.employeeListView.as_view(),name='employeelist'),
    path('<pk>/employeeupdate/', views.employeeUpdateView.as_view(), name='employeeupdate'),
    path('<pk>/employeedelete/', views.employeeDeleteView.as_view(), name='employeedelete'),
    path('<pk>/employeedetail/', views.employeeDetailView.as_view(), name='employeedetail'),

]
