from django.core.mail import send_mail


def send_post_create_notification(form):
    from_email = "archives987@gmail.com"
    recipient_list = ['ambitiouslavee@gmail.com']
    subject = "Blog Post Created"
    message = \
    """\
    Title: %s
    Author: %s
    Body: %s
    """ % (
        form.cleaned_data['title'],
        form.cleaned_data['author'],
        form.cleaned_data['body'],
    )
    send_mail(
        subject=subject,
        message=message,
        from_email=from_email,
        recipient_list=recipient_list,
        fail_silently=False
    )


def got_hit_notification(page=None, **kwargs):
    from_email = "archives987@gmail.com"
    recipient_list = ['ambitiouslavee@gmail.com']
    subject = "Got a hit on Another Solution"
    message = \
    """\
    Page: %s
    """ % (
        page
    )
    send_mail(
        subject=subject,
        message=message,
        from_email=from_email,
        recipient_list=recipient_list,
        fail_silently=False
    )