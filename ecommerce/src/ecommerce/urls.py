from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView
from django.contrib import admin
from django.conf.urls import url, include
from accounts.views import login_page, register_page, guest_register_view
from .views import home_page, contact_page, about_page
from addresses.views import checkout_address_create_view, checkout_address_reuse_view

urlpatterns = [
  url(r'^$', home_page, name="home"),
  url(r'^contact/$', contact_page, name="contact"),
  url(r'^about/$', about_page, name="about"),
  url(r'^admin/', admin.site.urls),
  url(r'^login/$', login_page, name="login"),
  url(r'^checkout/address/create/$', checkout_address_create_view, name="checkout_address_create"),
  url(r'^checkout/address/reuse/$', checkout_address_reuse_view, name="checkout_address_reuse"),
  url(r'^register/guest/$', guest_register_view, name="guest_register"),
  url(r'^logout/$', LogoutView.as_view(), name="logout"),
  url(r'^register/$', register_page, name="register"),
  url(r'^products/', include("products.urls")),
  url(r'^search/', include("search.urls")),
  url(r'^cart/', include("carts.urls")),
]

if settings.DEBUG:
  urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
  urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
