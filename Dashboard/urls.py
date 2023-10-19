from django.urls import path
from .views import front_page, edit_task


urlpatterns = [
    path('', front_page, name='start'),
    path('update_tasks/<int:pk>', edit_task, name='update_task'),

]