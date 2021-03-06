from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone

from .models import Choice, Question


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('pub_date')#[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'
    
    def get_context_data(self, **kwargs):
        context = super(DetailView , self).get_context_data(**kwargs)
        context['questions'] = Question.objects.filter(pub_date__lte=timezone.now()).order_by('pub_date')
        return context
    
    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'
    
    
class ResultsView(generic.ListView):
    template_name = 'polls/results_list.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('pub_date')
    
    
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choices = request.POST.getlist('choice')
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        for choice in selected_choices:
            q = get_object_or_404(Choice, pk=choice)
            print(q)
            print(q.votes)
            q.votes +=1
            q.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
    
    
