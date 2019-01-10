from django.urls import path
from . import views as qa_views

app_name = 'qa'
urlpatterns = [
    path('tests/', qa_views.tests, name='tests'),
    path('', qa_views.latest, name='latest'),
    path('topics/', qa_views.TopicsView.as_view(), name='home'),
    path('topics/<int:pk>/', qa_views.QuestionsView.as_view(), name = 'topic_questions'),
    path('topics/<int:pk>/new/', qa_views.new_question, name = 'new_question'),
    path('topics/<int:pk>/questions/<int:question_pk>/', qa_views.AnswersView.as_view(), name = 'question_answers'),
    path('topics/<int:pk>/questions/<int:question_pk>/reply/', qa_views.answer_question, name = 'answer_question'),
    path('topics/<int:pk>/questions/<int:question_pk>/answers/<int:answer_pk>/edit/', qa_views.AnswerUpdateView.as_view(), name = 'modify_answer'),
]