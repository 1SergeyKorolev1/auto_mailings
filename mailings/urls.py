# from django.urls import path

from mailings.apps import MailingsConfig

# from mailings.views import MailingListView, MailingDetailView, MailingUpdateView, MailingDeleteView, \
#     MailingCreateView, ContactView

app_name = MailingsConfig.name

urlpatterns = [
    # path('', MailingListView.as_view(), name='home'),
    # path('contact', ContactView.as_view(), name='contact'),
    # path('mailing_detail/<int:pk>', MailingDetailView.as_view(), name='mailing_detail'),
    # path('mailing_update/<int:pk>', MailingUpdateView.as_view(), name='mailing_update'),
    # path('mailing_delete/<int:pk>', MailingDeleteView.as_view(), name='mailing_delete'),
    # path('create/', MailingCreateView.as_view(), name='create_mailing')

]
