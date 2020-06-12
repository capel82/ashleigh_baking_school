from django.shortcuts import render
from django.contrib import messages

from .forms import ContactForm
from .models import Contact

def contact(request):
    template = "contact/contact.html"

    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, f'Inquiry sent. We will contact you soon.')

    else:
        form = ContactForm()


    return render(request, template, {'form': form})