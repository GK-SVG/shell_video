from django.contrib import admin
from .models import (
    CourseCategary,
    CourseLesson)
# Register your models here.
admin.site.register(CourseCategary)
admin.site.register(CourseLesson)