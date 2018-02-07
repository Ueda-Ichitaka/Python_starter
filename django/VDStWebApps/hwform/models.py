from django.db import models


class Ticket(models.Model):
    ticket_name = models.CharField(max_length=200)
    ticket_room = models.CharField(max_length=200)
    ticket_sum = models.CharField(max_length=200)
    ticket_descr = models.TextField('Descriptive text', default='Add your super descriptive text here...')
    pub_date = models.DateTimeField('date published')
   
    def __str__(self):
        return self.ticket_name