from django.shortcuts import render,HttpResponseRedirect,reverse
from django.views import generic
from django.urls import reverse_lazy
from .models import *
from .forms import *
# Create your views here.
class PollCreateView(generic.CreateView):
    model = Poll
    template_name = "poll_app/poll_create.html"
    success_url = reverse_lazy('list')
    form_class = PollForm
class PollListView(generic.ListView):
    model = Poll
    template_name = "poll_app/poll_list.html"
class PollVoteView(generic.TemplateView):
    model = Poll
    template_name = "poll_app/poll_vote.html"
    success_url = reverse_lazy('list')
    def get_context_data(self, poll_id,**kwargs):
        context = super().get_context_data(**kwargs)
        context["poll"] = Poll.objects.get(pk = poll_id) 
        return context
    def post(self, request, poll_id):
        poll = Poll.objects.get(pk = poll_id)
        option_chosen = request.POST['poll']
        poll.increement(option=option_chosen)
        return HttpResponseRedirect(reverse('list'))
class PollResultView(generic.TemplateView):
    template_name = "poll_app/poll_result.html"
    def get_context_data(self, poll_id,**kwargs):
        context = super().get_context_data(**kwargs)
        context["poll"] = Poll.objects.get(pk = poll_id) 
        return context

    


