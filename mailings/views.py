from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, UpdateView, DetailView, DeleteView, CreateView
from mailings.models import Mailing
from mailings.forms import MailingUpdateForm

# Create your views here.
class MailingListView(ListView):
    model = Mailing

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        mailings = Mailing.objects.all()
        context['mailings_list'] = mailings
        return context

class MailingUpdateView(UpdateView):
    model = Mailing
    form_class = MailingUpdateForm
    success_url = reverse_lazy('mailings:mailings_list')

    def get_success_url(self):
        return reverse('mailings:mailing_detail', args=[self.kwargs.get('pk')])

class MailingDetailView(DetailView):
    model = Mailing

class MailingDeleteView(DeleteView):
    model = Mailing
    success_url = reverse_lazy('mailings:mailings_list')

class MailingCreateView(CreateView):
    model = Mailing
    form_class = MailingUpdateForm
    success_url = reverse_lazy('mailings:mailings_list')