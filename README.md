# Real Estate Agency

Проект на Django для управления объявлениями о продаже квартир. Позволяет хранить данные о квартирах, владельцах и жалобах пользователей.

## Особенности проекта

- **Django 4.2.20** — основной фреймворк
- **Нормализация номеров** с помощью [django-phonenumber-field](https://github.com/stefanfoulis/django-phonenumber-field) и [phonenumbers](https://github.com/daviddrysdale/python-phonenumbers)
- **Связь квартир и владельцев** (ManyToMany)
- **Подача жалоб** на объявления
- **Фильтрация и поиск** в Django Admin
- **Переменные окружения** (используется [python-dotenv](https://github.com/theskumar/python-dotenv) и [environs](https://github.com/sloria/environs))  

## Установка и запуск

1. **Склонируйте репозиторий**:
   ```bash
   git clone https://github.com/Tikhovskoy/real_estate_agency.git
   cd real_estate_agency
   ```

2. **Создайте виртуальное окружение** (например, с помощью `venv`):
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
   На Windows:
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Установите зависимости**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Настройте переменные окружения** (если нужно):
   - Создайте файл `.env` в корне проекта (рядом с `manage.py`), например:
     ```
     DEBUG=True
     SECRET_KEY=super-secret-key
     ALLOWED_HOSTS=127.0.0.1,localhost
     ```
   - Или воспользуйтесь напрямую `environs`, подставив нужные значения в `settings.py`.

5. **Примените миграции**:
   ```bash
   python manage.py migrate
   ```

6. **Создайте суперпользователя** (для доступа к админке):
   ```bash
   python manage.py createsuperuser
   ```

7. **Запустите сервер разработки**:
   ```bash
   python manage.py runserver
   ```
   Приложение будет доступно по адресу: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## Структура проекта

```
real_estate_agency/
│
├── real_estate_agency/     # Настройки Django, wsgi/asgi и т.д.
│   ├── settings.py
│   └── ...
│
├── property/
│   ├── models.py           # Модели (Flat, Owner, Complaint)
│   ├── views.py            # Представления (вьюхи)
│   ├── admin.py            # Настройки Django Admin
│   └── ...
│
├── venv/                   # Виртуальное окружение (не хранится в репозитории)
├── requirements.txt        # Зависимости
├── manage.py               # Основной скрипт Django
└── README.md               # Текущее описание проекта
```

## Использование

- **Админка**: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)  
  Здесь можно добавлять/редактировать квартиры, владельцев, жалобы.
- **Модель Flat**:
  - `owner_deprecated`: старое поле для ФИО владельца (используется для совместимости).
  - `owners_phonenumber`: телефон владельца (не нормализован).
  - `owner_pure_phone`: нормализованный номер через `PhoneNumberField`.
  - `town`, `address`, `price` и т.д.
- **Модель Owner**:
  - `phone`: телефон в произвольном виде.
  - `pure_phone`: нормализованный телефон (если заполнен).
  - связь `owned_flats` (ManyToMany с `Flat`).
- **Модель Complaint**:
  - `user`: пользователь, который жалуется.
  - `flat`: на какую квартиру жалуются.
  - `complaint_text`: текст жалобы.
