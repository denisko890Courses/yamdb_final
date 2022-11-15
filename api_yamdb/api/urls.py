from api.views import (CategoryViewSet, CommentViewSet, GenreViewSet,
                       ReviewsViewSet, TitleViewSet)
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from users.views import CreateTokenView, SignUpView, UsersViewSet

app_name = 'api'

router_v1 = DefaultRouter()


router_v1.register('categories', CategoryViewSet, basename='categories')
router_v1.register('genres', GenreViewSet, basename='genres')
router_v1.register('titles', TitleViewSet, basename='titles')
router_v1.register(r'titles/(?P<title_id>\d+)/reviews',
                   ReviewsViewSet, basename='reviews')
router_v1.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewSet, basename='comments')
router_v1.register('users', UsersViewSet, basename='users')

urlpatterns = [
    path('v1/auth/signup/', SignUpView.as_view(), name='signup'),
    path('v1/auth/token/', CreateTokenView.as_view(), name='create_token'),
    path('v1/', include(router_v1.urls)),
]
