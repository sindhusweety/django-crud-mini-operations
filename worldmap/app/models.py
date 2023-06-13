from django.db import models

class Continents(models.Model):
    continent_name = models.CharField(max_length=50, blank=True, default='')

    def __str__(self):
        return self.continent_name

class Country(models.Model):
    country_name = models.CharField(max_length=100, blank=True, default='')
    continent_id = models.ForeignKey("Continents", on_delete=models.CASCADE)

    def __str__(self):
        return self.country_name

class State(models.Model):
    state_name = models.CharField(max_length=100, blank=True, default='')
    continent_id = models.ForeignKey('Continents', on_delete=models.CASCADE)
    country_id = models.ForeignKey('Country', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.state_name
