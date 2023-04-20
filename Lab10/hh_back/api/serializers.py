from rest_framework import serializers

from .models import *

class VacancySerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacancy
        fields = ['id', 'name', 'description', 'salary', 'company']
        extra_kwargs = {'id': {'read_only': True}}

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['id', 'name', 'description', 'city', 'address']
        extra_kwargs = {'id': {'read_only': True}}
