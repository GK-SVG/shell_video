from django.contrib import admin
from .models import (
    CourseCategary,
    CourseLesson,
    Videos)
# Register your models here.
admin.site.register(CourseCategary)
admin.site.register(CourseLesson)
admin.site.register(Videos)