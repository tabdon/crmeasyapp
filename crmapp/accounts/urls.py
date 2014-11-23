from django.conf.urls import patterns, url

account_urls = patterns('',

    url(r'^$',
        'crmapp.accounts.views.account_detail', name='account_detail'
    ),
    url(r'^edit/$',
        'crmapp.accounts.views.account_cru', name='account_update'
    ),
)
