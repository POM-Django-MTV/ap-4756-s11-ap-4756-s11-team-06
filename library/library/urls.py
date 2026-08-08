from django.urls import include, path


urlpatterns = [
    path('author/', include('author.urls')),
    path('book/', include('book.urls')),
    path('order/', include('order.urls')),
    path('user/', include('user.urls')),
]
