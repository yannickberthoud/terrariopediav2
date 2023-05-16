from django.urls import path
from .views import CommunityList, ChangePasswordView, CommunityDetail, MemberUpdateView

app_name = "member"
urlpatterns = [
    path('membres/', CommunityList, name="member-list"),
    path('password-change/', ChangePasswordView.as_view(), name='password_change'),
    path('membres/<int:pk>/editer', MemberUpdateView.as_view(), name="member-edit"),
    path('membres/<int:pk>', CommunityDetail, name="member-detail"),
]