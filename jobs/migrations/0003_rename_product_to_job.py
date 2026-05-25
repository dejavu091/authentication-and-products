# Generated manually to preserve existing product table while renaming the model to Job
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_rename_decription_product_description_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='product',
            new_name='Job',
        ),
        migrations.RenameField(
            model_name='job',
            old_name='price',
            new_name='salary',
        ),
        migrations.RenameField(
            model_name='job',
            old_name='quantity',
            new_name='qualification',
        ),
    ]
