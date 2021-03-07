from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from .views import Actuators, Alerts, Readings, CreateRegularUser

urlpatterns = [
    path('token/obtain/', jwt_views.TokenObtainPairView.as_view(), name='token_create'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('create-user', CreateRegularUser.as_view(), name='create-user'),
    path('actuators/', Actuators.as_view(), name='actuators'),
    path('alerts/', Alerts.as_view(), name='alerts'),
    path('readings/<int:actuator_id>', Readings.as_view(), name='readings')
]