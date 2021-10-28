from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from user.views import userLogin, userLogout, userDashboard, userRecovery, changePassword


urlpatterns = [

    path('admin/', admin.site.urls),

    path('login/', userLogin, name='login'),
    path('logout/', userLogout, name='logout'),
    path('', userDashboard, name='dashboard'),
    path('recovery/', userRecovery, name='recovery'),
    path('changePassword/<email>/<path:password>', changePassword, name='changePassword'),

    path('event/', include('event.urls')),
    path('sales/', include('sales.urls')),
    path('user/', include('user.urls')),
]
