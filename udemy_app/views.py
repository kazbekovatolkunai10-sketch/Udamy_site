from rest_framework import viewsets
from .models import (UserProFile, Category, SubCategory, Lesson, Course, Assignment,
                     Exam, Questions, Option, Certificate,Review, Cart, CartItem)
from .serializer import (UserProFileSerializer, CategorySerializer, SubCategorySerializer, LessonSerializer,
                         CourseSerializer, AssignmentSerializer, ExamSerializer, QuestionsSerializer, OptionSerializer,
                         CertificateSerializer, ReviewSerializer, CartSerializer, CartItemSerializer)

class UserProFileViewSet(viewsets.ModelViewSet):
    queryset = UserProFile.objects.all()
    serializer_class = UserProFileSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_classes = CategorySerializer

class SubCategoryViewSet(viewsets.ModelViewSet):
    queryset = SubCategory.objects.all()
    serializers_classes = SubCategorySerializer

class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_classes = CourseSerializer

class AssignmentViewSet(viewsets.ModelViewSet):
    queryset = Assignment.objects.all()
    serializer_classes = AssignmentSerializer

class ExamViewSet(viewsets.ModelViewSet):
    queryset = Exam.objects.all()
    serializer_classes = ExamSerializer

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Questions.objects.all()
    serializer_classes = QuestionsSerializer

class OptionViewSet(viewsets.ModelViewSet):
    queryset = Option.objects.all()
    serializer_classes = OptionSerializer

class CertificateVIewSet(viewsets.ModelViewSet):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_classes = ReviewSerializer

class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

class CartItemViewSet(viewsets.ModelViewSet):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
