from . import views
from django.urls import path

urlpatterns = [

    path('',views.detail,name='detail'),
    path('detail',views.detail,name='detail'),
    path('delete/<int:task_id>/',views.delete,name='delete'),
    path('update/<int:id>/',views.update,name='update'),
    # path('homePage/',views.todolistview.as_view(),name='homePage'),
    path('homePage/', views.TodoListView.as_view(), name='homePage'),
    path('detail/<int:pk>/',views.TodoDetailView.as_view(),name='detail'),
    path('edited/<int:pk>/',views.ToDoupdate.as_view(),name='edited'),
    path('Deleted/<int:pk>/',views.ToDoDeleteView.as_view(),name='Deleted'),

]
