from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
    path('', views.PostsListView.as_view(), name='home'),
    path('search/', views.search, name='search'),
    path('signup/', views.SignupUserView.as_view(), name='signup'),
    path('login/', views.LoginUserView.as_view(), name='login'),
    path('logout/', views.LogoutUserView.as_view(), name='logout'),
    path('friend-request/<int:id>/', views.send_friend_request, name='send-friend-request'),
    path('accept-friend-request/<int:id>/', views.accept_friend_request, name='accept-friend-request'),
    path('users/', views.UsersListView.as_view(), name='users-list'),
    path('activate/<uidb64>/<token>', views.ActivateView.as_view(), name='activate'),
    path('profile/<int:pk>/', views.ProfileView.as_view(), name='profile'),
    path('add-post/', login_required(views.PostCreateView.as_view()), name='add-post'),
    path('post-like/', views.post_like, name="post-like"),
    path('comment-like/', views.comment_like, name="comment-like"),
    path('profile/<int:pk>/update/', views.UserUpdateView.as_view(), name='update-profile'),
    path('delete-post/<int:pk>/', views.PostDeleteView.as_view(), name='delete-post'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='detail-post'),
    path('delete-comment/<int:pk>/', views.CommentDeleteView.as_view(), name='delete-comment'),
    
]