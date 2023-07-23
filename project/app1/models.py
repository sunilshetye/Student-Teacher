from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import datetime


#CustomUser represents both teacher as well as student
# class CustomUser(AbstractUser):
#     pass

class User(AbstractUser): 
    username =models.CharField(max_length=100,unique= True, null=False, blank=False)
    name = models.CharField(max_length=100,default='Default Name')
    password = models.CharField(max_length=100)
    # REQUIRED_FIELDS=(user_name)
    ROLE_CHOICES = (
        ('student', 'Student'),
        ('teacher', 'Teacher'),
    )
    
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='student')
    def __str__(self):
        return self.name
    



class Teacher(User):
    pass



class Student(User):
    pass

class Admin(User):
     pass

# class Announcement(models.Model):
#     teacher_name = models.CharField(max_length=100)
#     timestamp= models.DateTimeField(default= datetime.now)
#     message = models.TextField()



# class Notification(models.Model):
#     teacher_name = models.CharField(max_length=100)
#     message = models.TextField()
#     student_username = models.CharField(max_length=100)


class Announcement(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.PROTECT, default=None)
    student = models.ForeignKey(Student, on_delete=models.PROTECT, default=None)


    acknowledgement= models.BooleanField(default=False)
    timestamp= models.DateTimeField(default= datetime.now)
    # teacher_name= models.CharField(max_length=100,default='', null=True, blank=True)

    message = models.TextField()
