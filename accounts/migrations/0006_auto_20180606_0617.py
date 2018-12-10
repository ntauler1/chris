from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20181201_0601'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stripeaccount',
            name='user',
        ),
        migrations.AddField(
            model_name='profile',
            name='stripe_id',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.DeleteModel(
            name='StripeAccount',
        ),
    ]
