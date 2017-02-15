"""
Send email for some views.
"""
from constance import config
from django.contrib.flatpages.models import FlatPage
from django.core.mail import send_mail, mail_admins
from django.core.urlresolvers import reverse

from .settings import DEFAULT_FROM_EMAIL

def reverse_full(*args, **kargs):
    """Return the full address using Django reverse."""
    # FIXME Avoid hard code the domain.
    return '{}{}'.format(
        config.DOMAIN,
        reverse(*args, **kargs)
    )

def new_notification(admin_url, admin_context, user_url, user_email, user_context):
    # Email to admin
    flatemail = FlatPage.objects.get(url=admin_url)
    mail_admins(
        flatemail.title,
        flatemail.content.format(**admin_context),
        fail_silently=False,
    )

    # Email to claimant
    flatemail = FlatPage.objects.get(url=user_url)
    send_mail(
        flatemail.title,
        flatemail.content.format(**user_context),
        DEFAULT_FROM_EMAIL,
        [user_email],
        fail_silently=False
    )

def new_fund_notification(fund):
    admin_url = "/email/template/fund/admin/"
    admin_context = {
        "link": reverse_full("fund_review", args=[fund.id]),
    }

    user_url = "/email/template/fund/claimant/"
    user_context = {
        "link": reverse_full("fund_detail", args=[fund.id]),
    }
    user_email = fund.claimant.email

    new_notification(admin_url, admin_context, user_url, user_email, user_context)

def new_expense_notification(expense):
    admin_url = "/email/template/expense/admin/"
    admin_context = {
        "link": reverse_full("expense_review", args=[expense.id]),
    }

    user_url = "/email/template/expense/claimant/"
    user_context = {
        "link": reverse_full("expense_detail", args=[expense.id]),
    }
    user_email = expense.fund.claimant.email

    new_notification(admin_url, admin_context, user_url, user_email, user_context)

def new_blog_notification(blog):
    admin_url = "/email/template/blog/admin/"
    admin_context = {
        "link": reverse_full("blog_review", args=[blog.id]),
    }

    user_url = "/email/template/blog/claimant/"
    user_context = {
        "link": reverse_full("blog_detail", args=[blog.id]),
    }
    user_email = blog.fund.claimant.email

    new_notification(admin_url, admin_context, user_url, user_email, user_context)

def review_notification(mail, url):
    # Email to user
    flatemail = FlatPage.objects.get(url=url)
    send_mail(
        flatemail.title,
        flatemail.content.format(
            new_message=mail.justification
        ),
        mail.sender.email,
        [mail.receiver.email],
        fail_silently=False
    )

def fund_review_notification(mail):
    review_notification(mail, "/email/template/fund/claimant/new/")

def expense_review_notification(mail):
    review_notification(mail, "/email/template/expense/claimant/new/")

def blog_review_notification(mail):
    review_notification(mail, "/email/template/blog/claimant/new/")