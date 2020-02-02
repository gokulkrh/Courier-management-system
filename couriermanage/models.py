from django.db import models


class Courier(models.Model):
	name = models.CharField(max_length=255)
	service = models.CharField(max_length=255)
	student_rollno = models.CharField(max_length=255)
	date_recieved = models.CharField(max_length=255)