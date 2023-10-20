from django.db import models
import uuid
from shortuuid.django_fields import ShortUUIDField
from users.models import User



ACCOUNT_STATUS = (
    ('active', 'Active'),
    ('in-active', 'In-active')
)

MARITAL_STATUS = (
    ('simgle', 'Single'),
    ('married', 'Married'),
    ('other', 'Other')
)

GENDER = (
    ('male', 'Male'),
    ('female', 'Female'),
    ('other', 'Other')
)

IDENTITY_TYPE = (
    ('international_passport', 'International Passport'),
    ('drivers_licence', 'Drivers Licence')
)


def user_directory_path(instance, filename):
    ext = filename.split(".")[-1]
    filename = "%s_%s" % (instance.id, ext)
    return "user_{0}/{1}".format(instance.user.id, filename)


class Account(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, defualt=uuid.uuid4, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    account_balance = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    account_number = ShortUUIDField(unique=True, length=10, max_length=25, prefix='119', alphabet='1234567890')
    account_id = ShortUUIDField(unique=True, length=7, max_length=25, prefix='ZIZ', alphabet='1234567890')
    pin_number = ShortUUIDField(unique=True, length=4, max_length=7, alphabet='1234567890')
    ref_code = ShortUUIDField(unique=True, length=10, max_length=7, alphabet='abcdefgh1234567890')
    account_status = models.CharField(max_length=100, choices=ACCOUNT_STATUS, default='In-active')
    date = models.DateTimeField(auto_now_add=True)
    kyc_submitted = models.BooleanField(default=False)
    kyc_confirmed = models.BooleanField(default=False)
    recommended_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='recommended_by')

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.user
