from django.db import models

class CourseTaken(models.Model):
	course_code = models.CharField("Course Code", max_length=10)
	course_title = models.CharField("Course Title", max_length=100)
	credit_units = models.PositiveSmallIntegerField()
	grade = models.PositiveSmallIntegerField()

	def __str__(self):
		return "{} {} {} {}".format(self.course_code, self.course_title, self.credit_units, self.grade)

# Create your models here.
