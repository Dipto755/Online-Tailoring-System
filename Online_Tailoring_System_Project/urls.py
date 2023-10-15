"""
URL configuration for Online_Tailoring_System_Project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import TailorApp.views as tviews

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("home/", tviews.home_view, name='home'),
    path("", tviews.home_view, name='home'),
    path('login/', tviews.login_view, name='login'),
    # path('homepage/<str:fname>/', tviews.homepage_view, name = 'homepage'),
    path('homepage/', tviews.homepage_view, name = 'homepage'),
    path('signup/', tviews.signup_view, name='signup'),
    path('homepage/logout', tviews.logout_views, name="logout"),
    path('fabric/', tviews.fabric_view, name = "fabric"),
    path('homepage/fabric/', tviews.fabric_view, name = "fabric"),
    path('homepage/fabric/<int:pk>/type/', tviews.type_view, name = "type"),
    # path('homepage/fabric/type/design/<int:pk>/<int:ty_id>', tviews.design_view, name="design"),
    path('homepage/fabric/type/<int:pk>/design/', tviews.design_view, name="design"),
    path('homepage/user-details/', tviews.user_details_view, name = "user-details"),
    path('homepage/user-details/update-profile/', tviews.update_profile_view, name = "update-profile"),
    path('homepage/fabric/type/design/kameez-designs-details/measurement-kameez/', tviews.measurement_kameez_views, name='measurement-kameez'),
    path('homepage/fabric/type/design/salowaar-designs-details/measurement-salwar/', tviews.measurement_salowaar_view, name='measurement-salwar'),
    path('homepage/fabric/type/design/shirt-designs-details/measurement-shirt/', tviews.measurement_shirt_view, name='measurement-shirt'),
    path('homepage/fabric/type/design/kameez-designs-details/<int:pk>', tviews.d_details_kameez_view, name="kameez-designs-details"),
    path('homepage/fabric/type/design/salowaar-designs-details/<int:pk>', tviews.d_details_salowaar_view, name="salowaar-designs-details"),
    path('homepage/fabric/type/design/shirt-designs-details/<int:pk>', tviews.d_details_shirt_view, name="shirt-designs-details"),
    path('homepage/fabric/type/design/kameez-designs-details/measurement-kameez/payment', tviews.order_confirm_payment_view, name='payment'),
    path('homepage/fabric/type/design/salowaar-designs-details/measurement-salwar/payment2', tviews.order_confirm_payment_view, name='payment2'),
    path('homepage/fabric/type/design/kameez-designs-details/measurement-kameez/payment-method', tviews.payment_method, name='payment-method'),
    path('/homepage/fabric/type/design/salowaar-designs-details/measurement-salwar/payment-method', tviews.payment_method, name='payment-method2'),
    
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
