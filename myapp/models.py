from django.db import models


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
            
class CourseLesson(models.Model):
    lesson_name=models.CharField(max_length=100)
    lessons=models.ForeignKey(CourseCategary,on_delete=models.CASCADE,related_name='Lessons')
    
    class Meta:
        db_table='course_lessons'
    
    def __str__(self):
        return self.lesson_name
    