from django.urls import path
from stocks import views
from rest_framework.urlpatterns import format_suffix_patterns

app_name = 'stocks'

urlpatterns = [
    path('stock/info', views.GetStockInfo.as_view()),
    path('stock/news', views.GetStockNews.as_view()),
    path('stock/history', views.GetStockHistory.as_view()),
]


urlpatterns = format_suffix_patterns(urlpatterns)