from django.shortcuts import render, redirect, get_object_or_404
from Bluecrm.Backend.models import Contacts, Customers, Interactions, Deals
from .forms import ContactsForm, CustomersForm, InteractionsForm, DealsForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages


@login_required()
def deals_view(request):
    filter_option = request.GET.get('filter')
    if filter_option == 'state':
        deal = Deals.objects.filter(choose='STATE').all()
    elif filter_option == 'motorcycle':
        deal = Deals.objects.filter(choose='MOTORCYCLE').all()
    else:
        deal = Deals.objects.all()
    return render(request, 'deals.html', {'deal': deal, 'filter_option': filter_option})


@login_required()
def update_deals(request, pk):
    deal = get_object_or_404(Deals, pk=pk)
    deals = DealsForm(request.POST or None, instance=deal)

    if deals.is_valid():
        deals.save()
        messages.success(request, "Details was updated.")
        return redirect(deals_view)
    return render(request, 'add_deals.html', {
        'deals': deals,
        'true': True,
    })


@login_required()
def add_deals(request):
    deals = DealsForm(request.POST or None)

    if deals.is_valid():
        deals.save()
        messages.success(request, "Deal was added.")
        return redirect(deals_view)
    return render(request, 'add_deals.html', {
        'deals': deals,
        'true': False,
    })


@login_required()
def remove_deals(request, pk):
    remove = get_object_or_404(Deals, pk=pk)

    if request.method == 'POST':
        remove.delete()
        messages.success(request, "Deal was deleted.")
        return redirect(deals_view)
    return render(request, 'remove_deals.html', {
        'remove': remove
    })


@login_required()
def deals_details(request, pk):
    details = get_object_or_404(Deals, pk=pk)
    return render(request, 'deal_detail.html', {
        'details': details
    })


@login_required()
def meeting_type_view(request):
    filter_option = request.GET.get('filter')

    if filter_option == 'SHOW':
        meeting = Interactions.managers.show_apartment()
    elif filter_option == 'VALUATION':
        meeting = Interactions.managers.valuation()
    elif filter_option == 'INSPECTION':
        meeting = Interactions.managers.inspect()
    elif filter_option == 'PICK UP':
        meeting = Interactions.managers.pick_up()
    else:
        meeting = Interactions.managers.all()

    return render(request, 'meeting_type.html', {'meeting': meeting, 'filter_option': filter_option})


@login_required()
def meeting_detail(request, pk):
    meeting = get_object_or_404(Interactions, pk=pk)

    return render(request, 'meeting_detail.html', {
        'meeting': meeting,
    })


@login_required()
def add_meeting(request):
    add_or_update_interactions = InteractionsForm(request.POST or None)

    if add_or_update_interactions.is_valid():
        add_or_update_interactions.save()
        messages.success(request, "Meeting was added.")
        return redirect(meeting_type_view)
    return render(request, 'add_meetings.html', {'add_or_update_interactions': add_or_update_interactions,
                                                 'true': True})


@login_required()
def update_meeting(request, pk):
    meeting = get_object_or_404(Interactions, pk=pk)
    add_or_update_interactions = InteractionsForm(request.POST or None, instance=meeting)

    if add_or_update_interactions.is_valid():
        add_or_update_interactions.save()
        messages.success(request, "Meeting was updated.")
        return redirect(meeting_type_view)
    return render(request, 'add_meetings.html', {'add_or_update_interactions': add_or_update_interactions,
                                                 'true': False})


@login_required()
def remove_meetings(request, pk):
    delete_meeting = get_object_or_404(Interactions, pk=pk)
    if request.method == 'POST':
        delete_meeting.delete()
        messages.success(request, "Meeting was removed.")
        return redirect(meeting_type_view)
    return render(request, 'delete_meeting.html', {'delete_meeting': delete_meeting})


@login_required()
def customers_view(request):
    filter_option = request.GET.get('filter')

    if filter_option == 'state':
        customers = Customers.managers.state().order_by('name')
    elif filter_option == 'motorcycle':
        customers = Customers.managers.motorcycle().order_by('name')
    else:
        customers = Customers.managers.all().order_by('name')

    return render(request, 'customers.html', {'customers': customers, 'filter_option': filter_option})


@login_required()
def customers_detail(request, pk):
    customer = get_object_or_404(Customers, pk=pk)

    return render(request, 'customer_detail.html', {
        'customer': customer,
    })


@login_required()
def add_customers(request):
    if request.method == 'POST':
        add_or_edit_customers = CustomersForm(request.POST or None)

        if add_or_edit_customers.is_valid():
            add_or_edit_customers.save()
            messages.success(request, "Customer was added.")
            return redirect(customers_view)
    else:
        CustomersForm()

    return render(request, 'add_customers.html', {'add_or_edit_customers': add_or_edit_customers, 'true': True})


@login_required()
def edit_customers(request, pk):
    customer = get_object_or_404(Customers, pk=pk)
    add_or_edit_customers = CustomersForm(request.POST or None, instance=customer)

    if add_or_edit_customers.is_valid():
        add_or_edit_customers.save()
        messages.success(request, "Customer was updated.")
        return redirect(customers_view)

    return render(request, 'add_customers.html', {'add_or_edit_customers': add_or_edit_customers, 'true': False})


@login_required()
def remove_customers(request, pk):
    remove_customer = get_object_or_404(Customers, pk=pk)

    if request.method == 'POST':
        remove_customer.delete()
        messages.success(request, "Deal was removed.")
        return redirect(customers_view)
    return render(request, 'delete_customer.html', {'remove_customer': remove_customer})


@login_required()
def contacts_view(request):
    filter_option = request.GET.get('filter')
    if filter_option == 'state':
        contacts = Contacts.managers.state().order_by('name')
    elif filter_option == 'motorcycle':
        contacts = Contacts.managers.motorcycle().order_by('name')
    else:
        contacts = Contacts.managers.all().order_by('name')

    return render(request, 'contacts.html', {'contacts': contacts, 'filter_option': filter_option})


@login_required()
def add_contacts(request):
    add_or_edit = ContactsForm(request.POST or None)

    if add_or_edit.is_valid():
        add_or_edit.save()
        messages.success(request, "Contact was added.")
        return redirect(contacts_view)

    return render(request, 'add.html', {'add_or_edit': add_or_edit, 'true': True})


@login_required()
def contacts_detail(request, pk):
    contact = get_object_or_404(Contacts, pk=pk)

    return render(request, 'contact_detail.html', {
        'contact': contact,
    })


@login_required()
def update(request, pk):
    contacts = get_object_or_404(Contacts, pk=pk)
    add_or_edit = ContactsForm(request.POST or None, instance=contacts)

    if add_or_edit.is_valid():
        add_or_edit.save()
        messages.success(request, "Contact was updated.")
        return redirect(contacts_view)

    return render(request, 'add.html', {'add_or_edit': add_or_edit, 'true': False})


@login_required()
def delete(request, pk):
    remove = get_object_or_404(Contacts, pk=pk)
    if request.method == 'POST':
        remove.delete()
        messages.success(request, "Contact was removed.")
        return redirect(contacts_view)

    return render(request, 'remove.html', {'remove': remove})
