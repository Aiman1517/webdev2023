from django.urls import path, re_path
from api.views import *
from api import views

urlpatterns = [
    path('vacancies/', VacancyListAPIView.as_view()),
    path('vacancies/<int:pk>/', VacancyGetUpdateDestroyAPIView.as_view()),
    path('vacancies/top_ten/', VacancyTopTenListAPIView.as_view()),
    path('companies/', views.company_list),
    path('companies/<int:id>/', views.company_detail),
    path('companies/<int:id>/vacancies/', views.vacancies_by_company),
]