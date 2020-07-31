from django.urls import path
from . import views
urlpatterns = [
    path('',views.tour_main, name = 'tour_main'),
    path('select/',views.select, name = 'select'),
    path('result/',views.result, name = 'result'),
    # path('result_detail/',views.result_detail, name = 'result_detail'),


]
