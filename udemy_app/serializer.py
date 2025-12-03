from rest_framework import serializers
from .models import (UserProFile, Category, SubCategory, Lesson, Course, Assignment,
                     Exam, Questions, Option, Certificate,Review, Cart, CartItem)

class UserProFileSerializer(serializers.Serializer):
    class Meta:
        model = UserProFile
        fields = ['username', 'role', 'full_name', 'profile_picture', 'bio']

class UserProFilSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProFile
        fields = ['full_name']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['category_name']

class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = ['subcategory_name', 'category']

class LessonListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['title_name', 'video_url']

class LessonDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['title', 'video_url', 'content']

class CourseListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['course_name', 'category', 'level', 'price']

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['course_name']

class AssignmentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields = ['title', 'course']

class AssignmentDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields = ['title', 'description', 'due_date', 'assignment_course', 'students_course']

class ExamListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exam
        fields = ['title']

class ExamDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exam
        fields = ['title', 'course', 'duration']

class QuestionsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questions
        fields = ['question_name']

class QuestionsDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questions
        fields = ['exam', 'question_name', 'passing_score']

class OptionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = ['option']

class OptionDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = ['question', 'option', 'bool']

class CertificateListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = ['student', 'course']

class CertificateDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = ['student', 'course', 'issued_at', 'certificate_url']

class ReviewListSerializer(serializers.ModelSerializer):
    user = UserProFilSimpleSerializer(many=True, read_only=True)
    course = CourseSerializer(read_only=True)
    class Meta:
        model = Review
        fields = ['user', 'comment', 'course']

class ReviewDetailSerializer(serializers.ModelSerializer):
    user = UserProFilSimpleSerializer(many=True, read_only=True)
    course = CourseSerializer(read_only=True)
    class Meta:
        model = Review
        fields = ['user', 'comment', 'course', 'rating']

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['user']

class CartItemSerializer(serializers.ModelSerializer):
    course = CourseListSerializer(read_only=True)
    class Meta:
        model = CartItem
        fields = ['cart', 'course', 'quantity']

class CourseDetailSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    assignment_course = AssignmentListSerializer(many=True, read_only=True)
    course_review = ReviewDetailSerializer(many=True)
    cart_course = CartSerializer(read_only=True)
    class Meta:
        model = Course
        fields = ['course_name', 'level', 'descriptions', 'created_by', 'created_at', 'update_at', 'category', 'price', 'assignment_course']
