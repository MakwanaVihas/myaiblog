from django.urls import path
from . import views
urlpatterns=[
path("",views.index,name="index"),
path("/news_of_ai=<int:id>",views.page,name="ai"),
path("",views.index1,name="page")

]

