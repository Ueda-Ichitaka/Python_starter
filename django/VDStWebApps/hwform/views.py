from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.http.response import Http404
from django.utils import timezone
from datetime import datetime

from .models import Ticket
from .forms import TicketForm

class IndexView(generic.ListView):
    template_name = "hwform/index.html"
    context_object_name = "ticket_list"
    model = Ticket
    
    def get_queryset(self):
        return Ticket.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')#[:5]

class DetailView(generic.DetailView):
    template_name = "hwform/detail.html"
    model = Ticket

class TicketListView(generic.ListView):
    template_name = "hwform/ticket_list.html"
    context_object_name = "ticket_list"
    model = Ticket
    
    def get_queryset(self):
        return Ticket.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')#[:5]

def ticket_upload(request):
    if request.method == 'GET':
        return render(request, 'hwform/upload.html', {})
    elif request.method == 'POST':
        ticket = Ticket.objects.create(ticket_descr=request.POST['ticket_descr'], ticket_name=request.POST['ticket_name'],
                                     pub_date=datetime.utcnow())
        # No need to call post.save() at this point -- it's already saved.
        return HttpResponseRedirect(reverse('hwform:ticket_detail', args=(ticket.id,)))


def ticket_form_upload(request):
    if request.method == 'GET':
        form = TicketForm()
    else:
        # A POST request: Handle Form Upload
        form = TicketForm(request.POST) # Bind data from request.POST into a PostForm
   
        # If data is valid, proceeds to create a new post and redirect the user
        if form.is_valid():
            ticket_name = form.cleaned_data['ticket_name']
            ticket_room = form.cleaned_data['ticket_room']
            ticket_sum = form.cleaned_data['ticket_sum']
            ticket_descr = form.cleaned_data['ticket_descr']
            ticket = Ticket.objects.create(ticket_name=ticket_name, ticket_room=ticket_room, ticket_sum=ticket_sum, ticket_descr=ticket_descr, pub_date=datetime.utcnow())
            return HttpResponseRedirect(reverse('hwform:ticket_detail', args=(ticket.id,)))
   
    return render(request, 'hwform/ticket_form_upload.html', {
        'form': form,
    })

# def index(request):
#     two_days_ago = datetime.utcnow() - timedelta(days=2)
#     recent_tickets = Ticket.objects.filter(pub_date__gt=two_days_ago).all()
#     context = Context({
#         'ticket_list': recent_tickets
#     })
#     return render(request, 'hwForm/index.html', context)
#     
#    
# def ticket_detail(request, ticket_id):
#     try:
#         ticket = Ticket.objects.get(pk=ticket_id)
#     except Ticket.DoesNotExist:
#         # If no Post has id post_id, we raise an HTTP 404 error.
#         raise Http404
#     return render(request, 'hwForm/detail.html', {'ticket': ticket})




    
    