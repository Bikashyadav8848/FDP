from django.db import migrations


def create_default_categories(apps, schema_editor):
    FeeCategory = apps.get_model('fees', 'FeeCategory')
    default_categories = [
        {'name': 'Tuition', 'description': 'Standard tuition fees for classes.'},
        {'name': 'Transportation', 'description': 'Transportation and bus fees.'},
        {'name': 'Library', 'description': 'Library and resource usage fees.'},
        {'name': 'Exam', 'description': 'Examination and assessment fees.'},
    ]

    for cat in default_categories:
        FeeCategory.objects.get_or_create(name=cat['name'], defaults={'description': cat['description']})


class Migration(migrations.Migration):

    dependencies = [
        ('fees', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_default_categories),
    ]
