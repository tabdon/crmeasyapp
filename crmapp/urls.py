from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

from marketing.views import HomePage
from accounts.views import AccountList
from accounts.urls import account_urls
from contacts.urls import contact_urls
from contacts.views import ContactDelete
from communications.urls import comm_urls
from communications.views import CommDelete

urlpatterns = patterns('',

    # Marketing pages
    url(r'^$', HomePage.as_view(), name="home"),

    # Subscriber related URLs
    url(r'^signup/$',
        'crmapp.subscribers.views.subscriber_new', name='sub_new'
    ),

    # Admin URL
    (r'^admin/', include(admin.site.urls)),

    # Login/Logout URLs
    (r'^login/$',
        'django.contrib.auth.views.login', {'template_name': 'login.html'}
    ),
    (r'^logout/$',
        'django.contrib.auth.views.logout', {'next_page': '/login/'}
    ),

    # Account related URLs
    url(r'^account/new/$',
        'crmapp.accounts.views.account_cru', name='account_new'
    ),
    url(r'^account/list/$',
        AccountList.as_view(), name='account_list'
    ),
    url(r'^account/(?P<uuid>[\w-]+)/', include(account_urls)),

    # Contact related URLS
    url(r'^contact/(?P<pk>[\w-]+)/delete/$',
        ContactDelete.as_view(), name='contact_delete'
    ),
    url(r'^contact/new/$',
        'crmapp.contacts.views.contact_cru', name='contact_new'
    ),
    url(r'^contact/(?P<uuid>[\w-]+)/', include(contact_urls)),

    # Communication related URLs
    url(r'^comm/new/$',
        'crmapp.communications.views.comm_cru', name='comm_new'
    ),
    url(r'^comm/(?P<uuid>[\w-]+)/', include(comm_urls)),
    url(r'^comm/(?P<pk>[\w-]+)/delete/$',
        CommDelete.as_view(), name='comm_delete'
    ),

)