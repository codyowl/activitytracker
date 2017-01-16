from django.db import models
from django.contrib.auth.models import User
# Create your models here.

PROGRESSION_STATUS = (
	(0, 'Completed'),
	(1, 'Almost there'),
	(2, 'Under progression'),
	(3, 'Initialized'),
	)

class Activity(models.Model):
	user = models.ForeignKey(User)
	activity_category = models.CharField(max_length=200)
	creation_date = models.DateTimeField(auto_now_add=True, blank=True)
	details = models.CharField(max_length=500)
	status = models.CharField(max_length=1, choices=PROGRESSION_STATUS)

	def __unicode__(self):
		return self.activity_category

	

