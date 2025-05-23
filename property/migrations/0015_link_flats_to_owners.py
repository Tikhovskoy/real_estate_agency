# Generated by Django 4.2.20 on 2025-03-25 07:18

from django.db import migrations

def link_flats_to_owners(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Owner = apps.get_model('property', 'Owner')

    for flat in Flat.objects.all():
        if flat.owner_deprecated:
            owner, created = Owner.objects.get_or_create(
                name=flat.owner_deprecated,
                phone=flat.owners_phonenumber,
                defaults={'pure_phone': flat.owner_pure_phone} 
            )
            
            flat.owners.add(owner)

            owner.owned_flats.add(flat)
            owner.save()
            flat.save()

class Migration(migrations.Migration):

    dependencies = [
        ('property', '0014_migrate_owner_pure_phone'),
    ]

    operations = [
        migrations.RunPython(link_flats_to_owners),
    ]
