from django.urls import path
from django.views.decorators.cache import cache_page

from apps.mailings.views import MailCreateView, MailListView, MailDeleteView, MailUpdateView, MailingsCreateView, \
    MailingsListView, MailingsUpdateView, MailingsDeleteView, MailingLogListView, HomePageView

app_name = 'mailings'

urlpatterns = [
    path('', cache_page(60)(HomePageView.as_view()), name='home'),
    # mails urls
    path('add_mail/', MailCreateView.as_view(), name='add_mail'),
    path('mails/', MailListView.as_view(), name='mails'),
    path('mail/update/<int:pk>', MailUpdateView.as_view(), name='mail_update'),
    path('mail/delete/<int:pk>', MailDeleteView.as_view(), name='mail_delete'),

    # mailings urls
    path('add_mailing/', MailingsCreateView.as_view(), name='add_mailing'),
    path('mailings/', MailingsListView.as_view(), name='mailings'),
    path('mailing/update/<int:pk>', MailingsUpdateView.as_view(), name='mailings_update'),
    path('mailing/delete/<int:pk>', MailingsDeleteView.as_view(), name='mailings_delete'),

    # logs urls
    path('logs', MailingLogListView.as_view(), name='logs'),
]
