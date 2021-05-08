from django.urls import path
from . import views
urlpatterns = [
    path('',views.PollListView.as_view(),name = 'list'),
    path('create/',views.PollCreateView.as_view(),name = 'create'),
    path('vote/<int:poll_id>',views.PollVoteView.as_view(),name = 'vote'),
    path('result/<int:poll_id>',views.PollResultView.as_view(),name = 'result'),
]
