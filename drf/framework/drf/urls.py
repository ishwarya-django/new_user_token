

from django.urls import path,include
from.views import RegisterView,LoginView,UserView,LogoutView
# TransformerList,TransformerDetail,student

urlpatterns = [
  
    path('register/',RegisterView.as_view()),
    path('login/',LoginView.as_view()),
    path('user/',UserView.as_view()),
    path('logout/',LogoutView.as_view()),
    # path('transformer/',TransformerList.as_view()),
    # path('transformer/<int:pk>/',TransformerDetail.as_view()),
    # path('student/',student.as_view()),


]
