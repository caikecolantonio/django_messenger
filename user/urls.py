from rest_framework.routers import DefaultRouter
from user.views import UserRegistrationViewSet, UserLoginViewSet, UserLogoutViewSet, UserListViewSet
from django.urls import include, path

router = DefaultRouter()
router.register(r"register", UserRegistrationViewSet, basename="user-registration")

urlpatterns = [
    path('', include(router.urls)),
    path('login/', UserLoginViewSet.as_view({'post': 'login'}), name='user-login'),
    path('logout/', UserLogoutViewSet.as_view({'get': 'logout'}), name='user-logout'),
    path('users-list/', UserListViewSet.as_view({'get': 'list'}), name='user-list')
]