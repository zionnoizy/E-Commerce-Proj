from django.contrib import admin
from django.urls import path, include
from django.conf import settings
# from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home_page.urls')),
    path('chat/', include('chat_app.urls')),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('products/', include('products.urls')),
    path('shopping_cart/', include('shopping_cart.urls')),
    path('checkout/', include('checkout.urls'))
]

# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_URL)
#     urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_URL)
