from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class user(User):
	userID = models.BigAutoField(primary_key=True)
	name = models.CharField(max_length=50)
	dob = models.DateField()
	userLocation = models.CharField(max_length=50)
	userDesc = models.TextField()

	# REQUIRED_FIELDS = []

	def __str__(self):
		return self.name

class NGO(models.Model):
	ngoID = models.BigAutoField(primary_key=True)
	ngoName = models.CharField(max_length=30)
	username = models.CharField(max_length=45)
	password = models.CharField(max_length=150)
	ngoLocation = models.CharField(max_length=50)
	ngoImpactLocation = models.CharField(max_length=50)
	ngoDesc = models.TextField()

	def __str__(self):
		return self.ngoName

class Projects(models.Model):
	projectID = models.BigAutoField(primary_key=True)
	name = models.CharField(max_length=40)
	projDesc = models.TextField()
	ngo = models.ForeignKey(NGO, on_delete=models.CASCADE)
	user = models.ManyToManyField(user)

	def __str__(self):
		return self.name