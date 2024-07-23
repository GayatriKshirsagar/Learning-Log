from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# A class named Topic inherits from Model - a parent class included in django
class Topic(models.Model):
	"""A topic the user is learning about."""
	# Use CharField when we want to store small amount od text, (name, title, city)
	text = models.CharField(max_length=200)
	# auto_now_add sets current date time whenever user creates a new topic
	date_added = models.DateTimeField(auto_now_add= True)
	owner = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		"""Return the string representation of the model."""
		return self.text

class Entry(models.Model):
	"""Something specific learned about the topic. """
	topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
	text = models. TextField()
	date_added = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name_plural = 'entries'

	def __str__(self):
		"""Return a string representation of the model."""
		# Only show first 50 characters of the text
		return f"{self.text[:50]}..."