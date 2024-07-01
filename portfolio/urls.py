from django.urls import path
from .views import home_view,contact_view, blog_view, blog_detail_view

urlpatterns = [
    path('',home_view,name='home-page'),
    path('contact/',contact_view,name='contact-page'),
    path('blog/', blog_view, name='blog-page'),
    path('blog/<int:id>', blog_detail_view, name='blog-detail')
]



