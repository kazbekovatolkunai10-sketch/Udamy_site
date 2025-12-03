from rest_framework import viewsets, generics
from .models import (UserProFile, Category, SubCategory, Lesson, Course, Assignment,
                     Exam, Questions, Option, Certificate,Review, Cart, CartItem)
from .serializer import (UserProFileSerializer, UserProFilSimpleSerializer, CategorySerializer, SubCategorySerializer, LessonListSerializer, LessonDetailSerializer,
                         CourseSerializer, AssignmentListSerializer,AssignmentDetailSerializer, ExamListSerializer,ExamDetailSerializer,
                         QuestionsListSerializer, QuestionsDetailSerializer, OptionListSerializer,OptionDetailSerializer,
                         CertificateListSerializer, CertificateDetailSerializer, ReviewListSerializer, ReviewDetailSerializer,
                         CartSerializer, CartItemSerializer, CourseListSerializer, CourseDetailSerializer)

class UserProFileAPIView(generics.ListAPIView):
    queryset = UserProFile.objects.all()
    serializer_class = UserProFileSerializer

class UserProFileSimpleAPIView(generics.ListAPIView):
    queryset = UserProFile.objects.all()
    serializer_class = UserProFilSimpleSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class SubCategoryViewSet(viewsets.ModelViewSet):
    queryset = SubCategory.objects.all()
    serializers_class = SubCategorySerializer

class LessonListAPIView(generics.ListAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonListSerializer

class LessonDetailAPIView(generics.RetrieveAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonDetailSerializer

class CourseAPIView(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class CourseListAPIView(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseListSerializer

class CourseDetailAPIView(generics.RetrieveAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseDetailSerializer

class AssignmentListAPIView(generics.RetrieveAPIView):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentListSerializer

class AssignmentDetailAPIView(generics.RetrieveAPIView):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentDetailSerializer

class ExamListAPIView(generics.ListAPIView):
    queryset = Exam.objects.all()
    serializer_class = ExamListSerializer

class ExamDetailAPIView(generics.RetrieveAPIView):
    queryset = Exam.objects.all()
    serializer_class = ExamDetailSerializer

class QuestionListAPIView(generics.ListAPIView):
    queryset = Questions.objects.all()
    serializer_class = QuestionsListSerializer

class QuestionDetailAPIView(generics.RetrieveAPIView):
    queryset = Questions.objects.all()
    serializer_class = QuestionsDetailSerializer

class OptionListAPIView(generics.ListAPIView):
    queryset = Option.objects.all()
    serializer_class = OptionListSerializer

class OptionDetailAPIView(generics.RetrieveAPIView):
    queryset = Option.objects.all()
    serializer_class = OptionDetailSerializer

class CertificateListAPIVIew(generics.ListAPIView):
    queryset = Certificate.objects.all()
    serializer_class = CertificateListSerializer

class CertificateDetailAPIVIew(generics.RetrieveAPIView):
    queryset = Certificate.objects.all()
    serializer_class = CertificateDetailSerializer

class ReviewListAPIView(generics.ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewListSerializer

class ReviewDetailView(generics.RetrieveAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewDetailSerializer

class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

class CartItemViewSet(viewsets.ModelViewSet):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
