from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.defaults import *
from ecommerce import settings

# Uncomment the next two lines to enable the admin:

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),
    (r'^grappelli/', include('grappelli.urls')),
    # Examples:
    # url(r'^$', 'ecommerce.views.home', name='home'),
    # url(r'^ecommerce/', include('ecommerce.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:

)


urlpatterns += patterns('accounts.views',
        (r'^register/$', 'register'),
)


"""urlpatterns += patterns('accounts.views',
        (r'^register/$', 'register',
        {'template_name': 'registration/registration.html'},
        'register'),

        (r'^my_account/$', 'my_account',
        {'template_name': 'registration/my_account.html'}, 'my_account'),

        (r'^order_details/(?P<order_id>[-\w]+)/$', 'order_details',
        {'template_name': 'registration/order_details.html'}, 'order_details'),

        (r'^order_info//$', 'order_info',
        {'template_name': 'registration/order_info.html'}, 'order_info'),
)
    """
urlpatterns += patterns('',
        (r'^login/$', 'django.contrib.auth.views.login',
        {'template_name': 'registration/login.html'}, 'login'),
)
