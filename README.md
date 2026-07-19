# doctor-visit-tracker

A Django web application for managing patient records and visit histories.

Built as my CS50x final project. Authenticated users can create, view, update,
and delete their own patient and visit records. The project focuses on
relational data modeling, Django forms and class-based views, and user-scoped
access control.

## Features

- Login and logout using Django authentication
- Patient records with contact details and date of birth
- Visit records linked to a patient and the logged-in user
- Create, view, update, and delete patients and visits
- Search patients by name
- Search visits by patient name, date, or notes
- Pagination for patient and visit lists
- User-scoped records: users can access only their own patients and visits
- Custom 400, 403, and 404 error pages
- Success messages after create, update, and delete actions

## Data model

```text
User
 ├── Patient
 │    ├── first name, last name
 │    ├── phone number, email
 │    └── date of birth
 │
 └── Visit
      ├── patient
      ├── date
      └── notes
```

Each patient and visit is associated with a Django user. List queries are
filtered by the logged-in user, and direct access to another user's records is
rejected.

## Setup

```sh
git clone https://github.com/lukantozi/doctor-visit-tracker.git
cd doctor-visit-tracker

python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Open `http://127.0.0.1:8000/` and sign in with the user created above.

## Tech

- Python
- Django
- SQLite
- Django ORM
- Django authentication
- Django class-based views and forms
- Bootstrap templates

## Notes

This is an educational project and is not intended for real medical use. It has
not been designed or reviewed for production security, privacy, or healthcare
compliance.

## License

MIT
