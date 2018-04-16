from django.db import models
from django.utils import timezone


class Post(models.Model):
	title = models.CharField(max_length=200)
	slug = models.SlugField(max_length=200)
	body = models.TextField()
	pub_date = models.DateTimeField(default=timezone.now)

	class Meta:
		ordering = ('-pub_date',)
		verbose_name = 'post'
		verbose_name_plural = verbose_name

	def __str__(self):
		return self.title

