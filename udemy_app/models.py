from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

class UserProFile(AbstractUser):
    username = models.CharField(max_length=60, unique=True)
    ROLE_CHOICES = (
        ('клиент', 'клиент'),
        ('преподаватель', 'преподаватель'),
    )
    role = models.CharField(max_length=34, choices=ROLE_CHOICES, default='клиент')
    full_name = models.CharField(max_length=100)
    profile_picture = models.ImageField(upload_to='profile_picture/', null=True, blank=True)
    bio = models.TextField()

    def __str__(self):
        return f'{self.username}, {self.role}'

class Category(models.Model):
    category_name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.category_name}'

class SubCategory(models.Model):
    subcategory_name = models.CharField(max_length=64)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.subcategory_name}'

class Lesson(models.Model):
    title_name = models.CharField(max_length=100)
    video_url = models.URLField()
    content = models.TextField()

    def __str__(self):
        return f'{self.title_name}'

class Course(models.Model):
    course_name = models.CharField(max_length=82)
    descriptions = models.TextField()
    category = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    LEVEL_CHOICES = (
        ('начальный', 'начальный'),
        ('средний', 'средний'),
        ('подвинутый', 'подвинутый'),
    )
    level = models.CharField(max_length=42, choices=LEVEL_CHOICES)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_by = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateField()

    def __str__(self):
        return f'{self.course_name}, {self.level}'

class Assignment(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    due_date = models.DateField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    students = models.ForeignKey(UserProFile, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title}'

class Exam(models.Model):
    title = models.CharField(max_length=100)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    duration = models.DurationField()

    def __str__(self):
        return f'{self.title}'

class Questions(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    question_name = models.CharField(max_length=100)
    passing_score = models.PositiveSmallIntegerField()

    def __str__(self):
        return f'{self.exam}, {self.passing_score}'

class Option(models.Model):
    question = models.ForeignKey(Questions, on_delete=models.CASCADE)
    CHOICES_OPTION = (
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
    )
    option = models.CharField(max_length=2)
    bool = models.BooleanField()

    def __str__(self):
        return f'{self.bool}'

class Certificate(models.Model):
    student = models.ForeignKey(UserProFile, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    issued_at = models.DateField()
    certificate_url = models.URLField()

    def __str__(self):
        return f'{self.student}, {self.course}'

class Review(models.Model):
    user = models.ForeignKey(UserProFile, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='course_review')
    rating = models.PositiveSmallIntegerField(validators=[MaxValueValidator(1), MinValueValidator(5)])
    comment = models.TextField()

    def __str__(self):
        return f'{self.user}'

class Cart(models.Model):
    user = models.ForeignKey(UserProFile, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user}'

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=1)

    def __str__(self):
        return f'{self.cart}, {self.course}'

