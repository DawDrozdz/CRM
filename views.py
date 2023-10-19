from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import send_mail
from django.contrib import messages
from .forms import SendEmailForm
from Dashboard.views import front_page
from django.contrib.auth.decorators import login_required
from .models import SendEmail


@login_required()
def mail_sender(request):
    if request.method == 'POST':
        send_emails_form = SendEmailForm(request.POST or None)
        if send_emails_form.is_valid():
            topic = send_emails_form.cleaned_data['topic']
            text = send_emails_form.cleaned_data['text']
            sender = 'programming.sender@gmail.com'
            recipient = send_emails_form.cleaned_data['recipient']
            send_mail(
                topic,
                text,
                sender,
                [recipient],
                fail_silently=False
            )
            send_emails_form.save()
            messages.success(request, 'Message was sent.')
        return redirect(front_page)

    else:
        send_emails_form = SendEmailForm()

        return render(request, 'send.html', {
            'send_emails_form': send_emails_form,
        })


def previous_messages(request):
    email = SendEmail.objects.all()
    return render(request, 'previous_messages.html', {
        'previous_message': email,
    })


def remove_mails(request, pk):
    remove = get_object_or_404(SendEmail, pk=pk)

    if request.method == 'POST':
        remove.delete()
        messages.error(request, 'Message was removed from DB.')
        return redirect(previous_messages)

    return render(request, 'remove_messages.html', {
        'remove_message': remove,
    })
