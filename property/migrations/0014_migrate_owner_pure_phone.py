from django.db import migrations

def migrate_owner_pure_phone(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Owner = apps.get_model('property', 'Owner')

    for flat in Flat.objects.all():
        if flat.owner_deprecated:
            owner, created = Owner.objects.get_or_create(
                name=flat.owner_deprecated,
                phone=flat.owners_phonenumber,
            )
            if flat.owner_pure_phone:
                owner.pure_phone = flat.owner_pure_phone
                owner.save()
            flat.owners.add(owner)

class Migration(migrations.Migration):

    dependencies = [
        ('property', '0013_owner_pure_phone'),  
    ]

    operations = [
        migrations.RunPython(migrate_owner_pure_phone),
    ]
