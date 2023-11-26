from django.urls import path

from library import views

urlpatterns = [
    path('', views.home, name='home'),
    path('books_list/', views.books_list, name='books_list'),
    path('add_book_form/', views.add_book_form, name='add_book_form'),
    path('add_user_form/', views.add_user_form, name='add_user_form'),
    path('update_book_info/', views.update_book_info, name='update_book_info'),
    path('confirm_delete/', views.confirm_delete, name='confirm_delete')
]
