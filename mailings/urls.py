from django.urls import path
from mailings.services import start_apscheduler
from mailings.apps import MailingsConfig

from mailings.views import MailingListView, MailingUpdateView, MailingDetailView, MailingDeleteView, MailingCreateView

app_name = MailingsConfig.name
start_apscheduler()

urlpatterns = [
    path('', MailingListView.as_view(), name='mailings_list'),
    path('mailing_update/<int:pk>', MailingUpdateView.as_view(), name='mailing_update'),
    path('mailing_detail/<int:pk>', MailingDetailView.as_view(), name='mailing_detail'),
    path('mailing_delete/<int:pk>', MailingDeleteView.as_view(), name='mailing_delete'),
    path('create/', MailingCreateView.as_view(), name='create_mailing')

]
