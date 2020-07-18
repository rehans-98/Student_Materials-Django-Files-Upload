from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from mysite.core import views


urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('upload/', views.upload, name='upload'),
    path('ref/', views.ref, name='ref'), 
    path('books/', views.book_list, name='book_list'),
    path('notes/', views.notes, name='book_list1'),
    path('books/upload/', views.upload_book, name='upload_book'),
    path('ref/upload', views.upload_ref, name='upload_ref'),
    
    path('books/<int:pk>/', views.delete_book, name='delete_book'),
    path('ref/<int:pk>/', views.delete_ref, name='delete_ref'),


    path('class/books/', views.BookListView.as_view(), name='class_book_list'),
    #path('class/books/upload/', views.UploadBookView.as_view(), name='class_upload_book'),
    path('login/',auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
