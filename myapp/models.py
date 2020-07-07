from django.db import models
# from django.core.validators import MaxValueValidator, MinValueValidator

# # Create your models here.
# class Course(models.Model):
#     name=models.CharField(max_length=200)
#     category=models.CharField(max_length=50)
#     rate=models.IntegerField(default=5,validators=[
#             MaxValueValidator(5),
#             MinValueValidator(1)
#         ])
#     price=models.CharField(max_length=5)


class CourseCategary(models.Model):
    title=models.CharField(max_length=200)
    price=models.IntegerField(default=0)
    image=models.ImageField(upload_to='course_categary',default='course_categary/course.png')
    language=models.CharField(max_length=30)
    difficulty=models.CharField(max_length=20,default='Beginner')
    content=models.TextField(default='')
    class Meta:
        db_table='course_categary'
        
    def __str__(self):
        return self.title
            