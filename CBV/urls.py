from django.urls import path


from .views import HomePage, PostPreLoadTaskView, SinglePostView

app_name = 'CBV'

urlpatterns = [
    path('', HomePage.as_view()),
    path('ex1/<int:pk>', PostPreLoadTaskView.as_view(), name='redirect-task'),
    path('ex2/<int:pk>', SinglePostView.as_view(), name='single-post'),

]
