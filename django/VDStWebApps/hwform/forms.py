from django import forms
 
class TicketForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(TicketForm, self).__init__(*args, **kwargs)
        self.fields['ticket_name'].label = "Your Name"
        self.fields['ticket_room'].label = "Your Room"
        self.fields['ticket_sum'].label = "Summary"
        self.fields['ticket_descr'].label = "Your Problem"
    
    ticket_name = forms.CharField(max_length=200)
    ticket_room = forms.CharField(max_length=200)
    ticket_sum = forms.CharField(max_length=200)
    ticket_descr = forms.CharField(widget=forms.Textarea)