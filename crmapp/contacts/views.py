from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.http import HttpResponseForbidden

from .models import Contact
from .forms import ContactForm


@login_required()
def contact_detail(request, uuid):

    contact = Contact.objects.get(uuid=uuid)

    return render(request, 
                'contacts/contact_detail.html', 
                {'contact': contact}
    )

@login_required()
def contact_cru(request):

    if request.POST:
        form = ContactForm(request.POST)
        if form.is_valid():
            # make sure the user owns the account
            account = form.cleaned_data['account']
            if account.owner != request.user:
                return HttpResponseForbidden()
            # save the data
            contact = form.save(commit=False)
            contact.owner = request.user
            contact.save()
            # return the user to the account detail view
            reverse_url = reverse(
                'crmapp.accounts.views.account_detail',
                args=(account.uuid,)
            )
            return HttpResponseRedirect(reverse_url)
    else:
        form = ContactForm()

    variables = {
        'form': form,
    }

    template = 'contacts/contact_cru.html'

    return render(request, template, variables)
