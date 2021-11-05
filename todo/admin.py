from django.contrib import admin
from todo.models import Courses, Article


class CoursesAdmin(admin.ModelAdmin):
    list_display_courses = ('name', 'description','duration','author')


class UserAdmin(admin.ModelAdmin):
    list_display_users = ('author', 'is_author')


admin.site.register(Courses, CoursesAdmin)
admin.site.register(Article, UserAdmin)
