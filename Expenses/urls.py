from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
from Expenses.views import ExpenseSheetDetail

urlpatterns = patterns('',
    url(r'^$', 'Expenses.views.index', name='index'),
    url(r'^new', 'Expenses.views.new', name='new'),
    url(r'^expense/(?P<pk>\d+)/$', ExpenseSheetDetail.as_view(), name='expense-detail'),
    url(r'^expense/(?P<pk>\d+)/add_row', 'Expenses.views.add_row', name='add-row'),
    url(r'^create', 'Expenses.views.create', name='create'),
    url(r'^login', 'django.contrib.auth.views.login', {'template_name': 'accounts/login.html'}, name='login'),
    url(r'^register', 'Expenses.views.register', name='register'),

    # url(r'^Expenses/', include('Expenses.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
