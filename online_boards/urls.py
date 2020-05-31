from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import re_path, reverse_lazy
from django.urls import path
from django.contrib.auth import views as auth_views

from boards import views as boards_views
from accounts import views as accounts_views


urlpatterns = [
    path('', boards_views.BoardListView.as_view(), name='home'),
    path('signup/', accounts_views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('boards/<int:pk>/', boards_views.TopicListView.as_view(), name='board_topics'),
    path('boards/<int:pk>/new/', boards_views.new_topic, name='new_topic'),
    path('boards/<int:pk>/topics/<int:topic_pk>/', boards_views.PostListView.as_view(), name='topic_posts'),
    path('boards/<int:pk>/topics/<int:topic_pk>/posts/<int:post_pk>/edit/',
         boards_views.PostUpdateView.as_view(), name='edit_post'),
    path('boards/<int:pk>/topics/<int:topic_pk>/reply/', boards_views.reply_topic, name='reply_topic'),
    path('settings/account/', accounts_views.UserUpdateView.as_view(), name='my_account'),
    path('settings/password/', auth_views.PasswordChangeView.as_view(template_name='password_change.html'),
         name='password_change'),
    path('settings/password/done/',
         auth_views.PasswordChangeDoneView.as_view(template_name='password_change_done.html'),
         name='password_change_done'),
    path('user/contact/', boards_views.ContactView.as_view(), name='contact_us'),
    path('reset_password/',
         auth_views.PasswordResetView.as_view(
             template_name='reset/password_reset.html',
             email_template_name='reset/password_reset_email.html',
             success_url=reverse_lazy('password_reset_done'),
             subject_template_name='reset/password_reset_subject.txt'
         ),
         name='password_reset'),
    path('reset/done/',
         auth_views.PasswordResetDoneView.as_view(template_name='reset/password_reset_done.html'),
         name='password_reset_done'),
    re_path('reset/(?P<uidb64>[0-9A-Za-z]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/',
            auth_views.PasswordResetConfirmView.as_view(template_name='reset/password_reset_confirm.html',
                                                        success_url=reverse_lazy('password_reset_complete')),
            name='password_reset_confirm'),
    path('reset/complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='reset/password_reset_complete.html'),
         name='password_reset_complete'),
    path('admin/', admin.site.urls)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
