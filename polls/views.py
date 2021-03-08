from django.shortcuts import get_object_or_404,  render
from django.http import HttpResponse
from django.http import Http404
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import generic
from django.views.generic.edit import DeleteView, CreateView
from django.db.models import Sum
from .forms import PollForm

from .models import Choice, Question

# Django generic views (might not work when I'll need to add my button)
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


class PollDelete(DeleteView):
    template_name = 'polls/delete.html'
    success_url = "/polls"

    def get_object(self):
        queryset = Question.objects.all().annotate(total_votes=Sum('choice__votes'))
        question = get_object_or_404(queryset, pk=self.kwargs['pk'])  # get_object_or_404 can take a queryset
        return question

# #TODO find a way to pass the current time for the Pub date field
# #TODO create fields for up to 4 choices associated with the new question
# class PollCreate(CreateView):
#     model= Question
#     template_name = 'polls/poll_create.html'
#     fields = '__all__'
#     success_url = "/polls"

# change routing
def create_poll(request):
    if request.method == 'POST':
        question = request.POST.get('question')

        question_obj = Question.objects.create(question_text=question)
        choices_first = request.POST.get('choices_first')
        choices_second = request.POST.get('choices_second')
        choices_third = request.POST.get('choices_third')
        choices_fourth = request.POST.get('choices_fourth')

        choices_first_obj = Choice.objects.create(question=question_obj, choice_text=choices_first)
        choices_second_obj = Choice.objects.create(question=question_obj, choice_text=choices_second)
        choices_third_obj = Choice.objects.create(question=question_obj, choice_text=choices_third)
        choices_fourth_obj = Choice.objects.create(question=question_obj, choice_text=choices_fourth)

        return redirect('/polls/')

    return render(request, 'polls/poll_create.html')


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

#this is the function used to create the hhtp response for /polls
#non Django generic views :
# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     context = {'latest_question_list': latest_question_list}
#     return render(request, 'polls/index.html', context)
#
# def detail(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/detail.html', {'question': question})
#
# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/results.html', {'question': question})
#
# def vote(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     try:
#         selected_choice = question.choice_set.get(pk=request.POST['choice'])
#     except (KeyError, Choice.DoesNotExist):
#         # Redisplay the question voting form.
#         return render(request, 'polls/detail.html', {
#             'question': question,
#             'error_message': "You didn't select a choice.",
#         })
#     else:
#         selected_choice.votes += 1
#         selected_choice.save()
#         # Always return an HttpResponseRedirect after successfully dealing
#         # with POST data. This prevents data from being posted twice if a
#         # user hits the Back button.
#         return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))