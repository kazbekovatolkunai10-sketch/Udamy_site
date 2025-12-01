from .models import (UserProFile, Category, SubCategory, Lesson,
                     Course, Assignment, Exam, Questions, Option)
from modeltranslation.translator import TranslationOptions,register

@register(UserProFile)
class UserProFileTranslationOptions(TranslationOptions):
    fields = ('username', 'full_name', 'bio')

@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('category_name',)

@register(SubCategory)
class SubCategoryTranslationOptions(TranslationOptions):
    fields = ('subcategory_name', 'category')

@register(Lesson)
class LessonTranslationOptions(TranslationOptions):
    fields = ('title_name', 'content')

@register(Course)
class CourseTranslationOptions(TranslationOptions):
    fields = ('course_name', 'descriptions')


@register(Assignment)
class AssignmentTranslationOptions(TranslationOptions):
    fields = ('title', 'description')

@register(Exam)
class ExamTranslationOptions(TranslationOptions):
    fields = ('title',)

@register(Questions)
class QuestionsTranslationOptions(TranslationOptions):
    fields = ('question_name',)

@register(Option)
class OptionTranslationOptions(TranslationOptions):
    fields = ('option',)

