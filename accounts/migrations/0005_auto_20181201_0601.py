from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0004_userstripe'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='userStripe',
            new_name='StripeAccount',
        ),
    ]
