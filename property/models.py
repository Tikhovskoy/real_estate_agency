from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

class Owner(models.Model):
    name = models.CharField('ФИО собственника', max_length=200)
    phone = models.CharField('Телефон собственника', max_length=20, blank=True, null=True)
    email = models.EmailField('Email собственника', blank=True, null=True)

    flats = models.ManyToManyField('property.Flat', related_name='owners', blank=True)

    def __str__(self):
        return self.name

class Complaint(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    flat = models.ForeignKey('property.Flat', on_delete=models.CASCADE, verbose_name="Квартира, на которую пожаловались")  # Используем строковое имя модели
    complaint_text = models.TextField("Текст жалобы", help_text="Опишите проблему")
    created_at = models.DateTimeField("Когда подана жалоба", auto_now_add=True)

    def __str__(self):
        return f"Жалоба от {self.user.username} на {self.flat.address}"


class Flat(models.Model):
    owner = models.CharField('ФИО владельца', max_length=200)
    owners_phonenumber = models.CharField('Номер владельца', max_length=20)
    owner_pure_phone = PhoneNumberField('Нормализованный номер владельца', blank=True, null=True, region='RU')
    created_at = models.DateTimeField(
        'Когда создано объявление',
        default=timezone.now,
        db_index=True)

    description = models.TextField('Текст объявления', blank=True)
    price = models.IntegerField('Цена квартиры', db_index=True)

    town = models.CharField(
        'Город, где находится квартира',
        max_length=50,
        db_index=True)
    town_district = models.CharField(
        'Район города, где находится квартира',
        max_length=50,
        blank=True,
        help_text='Чертаново Южное')
    address = models.TextField(
        'Адрес квартиры',
        help_text='ул. Подольских курсантов д.5 кв.4')
    floor = models.CharField(
        'Этаж',
        max_length=3,
        help_text='Первый этаж, последний этаж, пятый этаж')

    rooms_number = models.IntegerField(
        'Количество комнат в квартире',
        db_index=True)
    living_area = models.IntegerField(
        'количество жилых кв.метров',
        null=True,
        blank=True,
        db_index=True)

    has_balcony = models.BooleanField('Наличие балкона', null=True, db_index=True)
    active = models.BooleanField('Активно-ли объявление', db_index=True)
    construction_year = models.IntegerField(
        'Год постройки здания',
        null=True,
        blank=True,
        db_index=True)
    
    new_building = models.BooleanField(
        'Новостройка', 
        null=True, 
        blank=True, 
        db_index=True
    )

    likes = models.ManyToManyField(User, related_name='liked_flats', blank=True)

    def __str__(self):
        return f'{self.town}, {self.address} ({self.price}р.)'
