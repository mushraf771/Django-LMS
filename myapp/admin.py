from django.contrib import admin
from .models import UserAccount,Thread,Course,Module,Enrollment,Submission,Assignment,Forum,Lesson
@admin.register(UserAccount)
class Admin(admin.ModelAdmin):
    list_display = ('id', 'email', 'name',  'is_instructor','is_active')
    list_display_links = ('id', 'name', 'email')
    search_fields = ('name', 'email', 'id')
    list_per_page = 20
 
@admin.register(Course)
class Admin(admin.ModelAdmin):
    list_display = ('id', 'title',)
    list_display_links = ('id', 'title')
    search_fields = ('title', 'id')
    list_per_page = 20
 
@admin.register(Thread)
class Admin(admin.ModelAdmin):
    list_display = ('id', 'forum','title','user')
    list_display_links = ('id', 'title',)
    search_fields = ('user', 'title', 'id')
    list_per_page = 20
 
@admin.register(Module)
class Admin(admin.ModelAdmin):
    list_display = ('id', 'title', 'course',  )
    list_display_links = ('id', 'course', )
    search_fields = ('course', 'id')
    list_per_page = 20
 
@admin.register(Lesson)
class Admin(admin.ModelAdmin):
    list_display = ('id', 'module', 'title',)
    list_display_links = ('id', 'title', 'module')
    search_fields = ('title', 'module', 'id')
    list_per_page = 20
 
@admin.register(Enrollment)
class Admin(admin.ModelAdmin):
    list_display = ('id', 'student', 'course',  'progress',)
    list_display_links = ('id', 'course', 'student')
    search_fields = ('course', 'student', 'id')
    list_per_page = 20
 
@admin.register(Assignment)
class Admin(admin.ModelAdmin):
    list_display = ('id', 'title', 'course', )
    list_display_links = ('id', 'course', 'title')
    search_fields = ('course', 'title', 'id')
    list_per_page = 20
 
@admin.register(Submission)
class Admin(admin.ModelAdmin):
    list_display = ('id', 'student', 'assignment',  'content',)
    list_display_links = ('id', 'assignment', 'student')
    search_fields = ('assignment', 'student', 'id')
    list_per_page = 20
 
@admin.register(Forum)
class Admin(admin.ModelAdmin):
    list_display = ('id', 'course', )
    list_display_links = ('id', 'course')
    search_fields = ('course', 'id')
    list_per_page = 20
 