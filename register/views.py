from django.shortcuts import render

# Create your views here.
from django.shortcuts import render_to_response
from django.forms import ModelForm
from models import Contact


class ContactForm(ModelForm):
    class Meta:
        model = Contact


def contact(request):

    contact_form = ContactForm()
    return render_to_response('contact.html', {'contact_form' : contact_form})
