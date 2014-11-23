from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden

from .models import Communication

@login_required()
def comm_detail(request, uuid):

    comm = Communication.objects.get(uuid=uuid)
    if comm.owner != request.user:
            return HttpResponseForbidden()

    return render(request, 'communications/comm_detail.html', {'comm':comm})
