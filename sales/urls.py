from django.urls import path
from .views import 홈페이지

app_name = 'namespace와 관계없음'

urlpatterns = [
    path('', 홈페이지),

]