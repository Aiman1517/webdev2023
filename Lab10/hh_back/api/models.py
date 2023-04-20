from django.db import models

# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=255)
    description  = models.TextField()
    city = models.CharField(max_length=255)
    address = models.TextField()

    def __str__(self):
        return f'{self.id}: {self.name}'
    
    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'city': self.city,
            'address': self.address,
        }
    
class Vacancy(models.Model):
    name = models.CharField(max_length=255)
    description  = models.TextField()
    salary = models.CharField(max_length=255)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='vacancy')

    def __str__(self):
        return f'{self.id}: {self.name}'