from django.db import models
from django.utils.translation import gettext_lazy as _
import uuid # Used for generating unique booking references

# Assuming you have a Booking model defined already in this file/app
# If your Booking model is in a different app, you must import it.
# e.g., from bookings.models import Booking 

class Payment(models.Model):
    # --- Choices for Payment Status ---
    class PaymentStatus(models.TextChoices):
        PENDING = 'PENDING', _('Pending')
        COMPLETED = 'COMPLETED', _('Completed')
        FAILED = 'FAILED', _('Failed')
        REFUNDED = 'REFUNDED', _('Refunded')

    # Foreign Key to link the payment back to a specific booking (optional, but highly recommended)
    # If the Booking model is not yet created, comment this out and add it later:
    # booking = models.OneToOneField(
    #     'Booking',  # Replace 'Booking' with the actual model name if different
    #     on_delete=models.SET_NULL,
    #     null=True,
    #     blank=True,
    #     related_name='payment'
    # )

    # Required Fields
    booking_reference = models.CharField(
        max_length=50,
        unique=True,
        default=uuid.uuid4, # Use a unique ID generator for reliable references
        verbose_name=_("Booking Reference")
    )
    
    transaction_id = models.CharField(
        max_length=100,
        unique=True,
        blank=True,
        null=True,
        verbose_name=_("Transaction ID")
    )

    amount = models.DecimalField(
        max_digits=10, 
        decimal_places=2,
        verbose_name=_("Amount Paid")
    )

    payment_status = models.CharField(
        max_length=10,
        choices=PaymentStatus.choices,
        default=PaymentStatus.PENDING,
        verbose_name=_("Payment Status")
    )

    # Tracking/Audit Fields
    payment_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_("Payment Date")
    )

    # String representation for the Django Admin
    def __str__(self):
        return f"Payment {self.booking_reference} - {self.get_payment_status_display()}"

    # Metadata options
    class Meta:
        verbose_name = _("Payment")
        verbose_name_plural = _("Payments")