from django.urls import path
from .views import contacts_view, add_contacts, update, delete, customers_view, add_customers, \
    edit_customers, remove_customers, meeting_type_view, add_meeting, update_meeting, remove_meetings, deals_view, \
    contacts_detail, customers_detail, meeting_detail, remove_deals, add_deals, update_deals, deals_details


urlpatterns = [
    path('deal/', deals_view, name='deals'),
    path('contacts/', contacts_view, name='contacts'),
    path('contacts_detail/<int:pk>/', contacts_detail, name='contacts_detail'),
    path('customers/', customers_view, name='customers'),
    path('customers_detail/<int:pk>/', customers_detail, name='customers_detail'),
    path('meeting/', meeting_type_view, name='meeting'),
    path('meeting_detail/<int:pk>/', meeting_detail, name='meeting_detail'),
    path('add/', add_contacts, name='add'),
    path('add_customers/', add_customers, name='add_customers'),
    path('add_meetings/', add_meeting, name='add_meeting'),
    path('add_deals/', add_deals, name='add_deals'),
    path('update/<int:pk>', update, name='update'),
    path('update_customer/<int:pk>', edit_customers, name='edit_customer'),
    path('update_meetings/<int:pk>', update_meeting, name='update_meeting'),
    path('update_deals/<int:pk>', update_deals, name='update_deals'),
    path('remove/<int:pk>', delete, name='remove'),
    path('remove_customer/<int:pk>', remove_customers, name='remove_customer'),
    path('remove_meeting/<int:pk>', remove_meetings, name='remove_meetings'),
    path('remove_deal/<int:pk>', remove_deals, name='remove_deals'),
    path('deals_details/<int:pk>', deals_details, name='deals_details'),

]
