from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Contact


@login_required()
def contact_detail(request, uuid):

    contact = Contact.objects.get(uuid=uuid)

    return render(request, 
                'contacts/contact_detail.html', 
                {'contact': contact}
    )
