from django.conf.urls import patterns, url

comm_urls = patterns('',

    url(r'^$',
        'crmapp.communications.views.comm_detail', name="comm_detail"
    ),
    url(r'^edit/$',
        'crmapp.communications.views.comm_cru', name='comm_update'
    ),

)
