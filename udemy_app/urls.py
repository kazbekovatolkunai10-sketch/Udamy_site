from django.urls import path, include
from rest_framework import routers
from .views import (UserProFileAPIView, UserProFileSimpleAPIView, CategoryViewSet, SubCategoryViewSet, LessonListAPIView,
                    LessonDetailAPIView, CourseAPIView, CourseListAPIView, CourseDetailAPIView,
                    AssignmentListAPIView, AssignmentDetailAPIView, ExamListAPIView, ExamDetailAPIView, QuestionListAPIView,
                    QuestionDetailAPIView, OptionListAPIView, OptionDetailAPIView, CertificateListAPIVIew, CertificateDetailAPIVIew,
                    ReviewListAPIView, ReviewDetailView, CartViewSet, CartItemViewSet)

router = routers.SimpleRouter()
router.register(r'category', CategoryViewSet)
router.register(r'subcategory', SubCategoryViewSet)
router.register(r'cart', CartViewSet)
router.register(r'cart_item', CartItemViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('user/<int:pk>/', UserProFileAPIView.as_view(), name='user'),
    path('user/', UserProFileSimpleAPIView.as_view(), name='user_simple'),
    path('lesson/', LessonListAPIView.as_view(), name='lesson-list'),
    path('lesson/<int:pk>/', LessonDetailAPIView.as_view(), name='lesson-detail'),
    path('courses/', CourseAPIView.as_view(), name='courses'),
    path('course/', CourseListAPIView.as_view(), name='course-list'),
    path('course/<int:pk>/', CourseDetailAPIView.as_view(), name='course-detail'),
    path('assignment/', AssignmentListAPIView.as_view(), name='assignment-list'),
    path('assignment/<int:pk>', AssignmentDetailAPIView.as_view(), name='-detail'),
    path('exam/', ExamListAPIView.as_view(), name='exam-list'),
    path('exam/<int:pk>/', ExamDetailAPIView.as_view(), name='exam-detail'),
    path('question/', QuestionListAPIView.as_view(), name='question-list'),
    path('question/<int:pk>/', QuestionDetailAPIView.as_view(), name='question-detail'),
    path('option/', OptionListAPIView.as_view(), name='option-list'),
    path('option/<int:pk>/', OptionDetailAPIView.as_view(), name='option-detail'),
    path('certificate/', CertificateListAPIVIew.as_view(), name='certificate-list'),
    path('certificate/<int:pk>/', CertificateDetailAPIVIew.as_view(), name='certificate-detail'),
    path('review/', ReviewListAPIView.as_view(), name='review-list'),
    path('review/<int:pk>', ReviewDetailView.as_view(), name='review-detail'),
]
