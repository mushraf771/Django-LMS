from django.db import models
from django.contrib.auth.models import User, AbstractBaseUser, PermissionsMixin, BaseUserManager
# Create your models here.
class UserAccountManager(BaseUserManager):
    def create_user(self, email, name,is_instructor, password=None,password2=None):
        if not email:
            raise ValueError('user must be an Email Address')
        email = self.normalize_email(email)
        user = self.model(email=email, name=name, is_instructor=is_instructor)
        user.set_password(password)
        user.is_instructor = False
        user.is_staff = False
        user.save()
        return user

    def create_superuser(self, email, name,is_instructor, password=None):
        user = self.create_user(email, name,is_instructor, password)
        user.is_superuser = True
        user.is_instructor= True
        user.is_staff= True
        user.save()
        return user

"""my custom model"""
class UserAccount(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_instructor = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    profile_picture = models.ImageField(upload_to='profile_pictures/',null=True,blank=True)
    objects = UserAccountManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name','is_instructor']

    def get_full_name(self):
        return self.name + ' ' + self.is_instructor

    def gt_short_name(self):
        return self.name

    def __str__(self):
        return self.name
    # def has_module_perms(self, perm ,obj=None):
        # return self.is_admin
    # def has_module_perms(self, app_label ):
        # return True
    # @property
    # def is_instructor(self):
    #     return self.is_admin
 
# models.py
class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    subject = models.CharField(max_length=255)
    # Add other fields
    def __str__(self):
            return self.title
class Module(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='modules')
    title = models.CharField(max_length=255)
    # Add other fields
    def __str__(self):
            return self.title
class Lesson(models.Model):
    module = models.ForeignKey(Module, on_delete=models.CASCADE, related_name='lessons')
    title = models.CharField(max_length=255)
    content = models.TextField()
    # Add other fields
    def __str__(self):
        return self.title
# models.py
class Enrollment(models.Model):
    student = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    progress = models.FloatField(default=0)
    
# models.py
class Assignment(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    # Add other fields
    def __str__(self):
            return self.title
class Submission(models.Model):
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    student = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    content = models.TextField()
    def __str__(self):
            return self.content
    # Add other fields

# models.py
class Forum(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    # def __str__(self):
    #    return self.course
    
class Thread(models.Model):
    forum = models.ForeignKey(Forum, on_delete=models.CASCADE)
    user = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    # Add other fields
    def __str__(self):
            return self.content

 