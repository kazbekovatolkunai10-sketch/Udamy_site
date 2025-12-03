from tokenize import TokenError

from rest_framework import viewsets, generics, status
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.views import APIView

from .filters import CourseFilter
from .models import (UserProFile, Category, SubCategory, Lesson, Course, Assignment,
                     Exam, Questions, Option, Certificate,Review, Cart, CartItem)
from .pagination import CoursePagination
from .serializer import (UserProFileSerializer, UserProFilSimpleSerializer, CategorySerializer, SubCategorySerializer, LessonListSerializer, LessonDetailSerializer,
                         CourseSerializer, AssignmentListSerializer,AssignmentDetailSerializer, ExamListSerializer,ExamDetailSerializer,
                         QuestionsListSerializer, QuestionsDetailSerializer, OptionListSerializer,OptionDetailSerializer,
                         CertificateListSerializer, CertificateDetailSerializer, ReviewListSerializer, ReviewDetailSerializer,
                         CartSerializer, CartItemSerializer, CourseListSerializer, CourseDetailSerializer,
                         LoginSerializer, UserSerializer)
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken

class RegisterView(generics.CreateAPIView):
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CustomLoginView(TokenObtainPairView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except Exception:
            return Response({"detail": "Неверные учетные данные"}, status=status.HTTP_401_UNAUTHORIZED)

        user = serializer.validated_data
        return Response(serializer.data, status=status.HTTP_200_OK)


class LogoutView(APIView):
    def post(self, request):
        try:
            refresh_token = request.data.get('refresh')
            if not refresh_token:
                return Response({'detail': 'Refresh токен не предоставлен.'}, status=status.HTTP_400_BAD_REQUEST)
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({'detail': 'Вы успешно вышли.'}, status=status.HTTP_200_OK)
        except TokenError as e:
            return Response({'detail': 'Недействительный токен.'}, status=status.HTTP_400_BAD_REQUEST)


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
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = CourseFilter
    search_fields = ['course_name']
    ordering_fields = ['price']
    pagination_class = CoursePagination

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
