from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

import stripe


class Subscriber(models.Model):
    user_rec = models.ForeignKey(User)
    address_one = models.CharField(max_length=100)
    address_two = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=2)
    stripe_id = models.CharField(max_length=30, blank=True)

    class Meta:
        verbose_name_plural = 'subscribers'

    def __unicode__(self):
        return u"%s's Subscription Info" % self.user_rec

    def charge(self, request, email, fee):
        # Set your secret key: remember to change this to your live secret key
        # in production. See your keys here https://manage.stripe.com/account
        stripe.api_key = settings.STRIPE_SECRET_KEY

        # Get the credit card details submitted by the form
        token = request.POST['stripeToken']

        # Create a Customer
        stripe_customer = stripe.Customer.create(
            card=token,
            description=email
        )

        # Save the Stripe ID to the customer's profile
        self.stripe_id = stripe_customer.id
        self.save()

        # Charge the Customer instead of the card
        stripe.Charge.create(
            amount=fee, # in cents
            currency="usd",
            customer=stripe_customer.id
        )

        return stripe_customer
