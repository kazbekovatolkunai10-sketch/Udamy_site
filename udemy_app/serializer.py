from rest_framework import serializers
from .models import (UserProFile, Category, SubCategory, Lesson, Course, Assignment,
                     Exam, Questions, Option, Certificate,Review, Cart, CartItem)

class UserProFileSerializer(serializers.Serializer):
    class Meta:
        model = UserProFile
        fields = '__all__'

class CategorySerializer(serializers.Serializer):
    class Meta:
        model = Category
        fields = '__all__'

class SubCategorySerializer(serializers.Serializer):
    class Meta:
        model = SubCategory
        fields = '__all__'

class LessonSerializer(serializers.Serializer):
    class Meta:
        model = Lesson
        fields = '__all__'

class CourseSerializer(serializers.Serializer):
    class Meta:
        model = Course
        fields = '__all__'

class AssignmentSerializer(serializers.Serializer):
    class Meta:
        model = Assignment
        fields = '__all__'

class ExamSerializer(serializers.Serializer):
    class Meta:
        model = Exam
        fields = '__all__'

class QuestionsSerializer(serializers.Serializer):
    class Meta:
        model = Questions
        fields = '__all__'

class OptionSerializer(serializers.Serializer):
    class Meta:
        model = Option
        fields = '__all__'

class CertificateSerializer(serializers.Serializer):
    class Meta:
        model = Certificate
        fields = '__all__'

class ReviewSerializer(serializers.Serializer):
    class Meta:
        model = Review
        fields = '__all__'

class CartSerializer(serializers.Serializer):
    class Meta:
        model = Cart
        fields = '__all__'

class CartItemSerializer(serializers.Serializer):
    class Meta:
        model = CartItem
        fields = '__all__'
