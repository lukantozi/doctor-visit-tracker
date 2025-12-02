# Doctor Visit Management App
---

## Description

The **Doctor Visit Management App** is a Django-based web application that allows doctors to manage patients and their medical visits through a clean and intuitive interface. It provides functionality to create, update, and delete records of patients and visits, and it supports user authentication to ensure data privacy.

I built this project as my CS50x final submission to apply my new skills in Python, Django, and web development to a real-world problem: helping doctors track patients and visits digitally with a lightweight, no-frills app.

I plan to improve the application further by adding AI-powered features as I gain more experience in the field.

---

## Features

- **User Authentication:** Only logged-in doctors can access the app’s features.
- **Patient Management:** Add, edit, delete, and search for patients, including their full details.
- **Visit Management:** Add, update, and delete visits linked to patients.
- **Smart Visit Linking:** From a patient’s page, a doctor can add a visit with the patient pre-filled.
- **Search Functionality:** Case-insensitive search in both patient and visit lists.
- **Access Restriction:** Doctors can only access their own patients and visits.
- **Error Handling:** Custom 400, 403, and 404 templates for a better user experience.
- **Success Messages:** User feedback via Django’s built-in messages framework.
- **Clean UI:** Uniform styling for all buttons, forms, and login page via embedded CSS.

---

## Technologies Used

- Python 3  
- Django  
- SQLite (default dev DB)  
- HTML & Django Templating  
- CSS (inline via base.html)  
- Git & GitHub  
- Visual Studio Code  

---

## File Structure

- `models.py`: Patient and Visit models linked to Django’s User model.
- `forms.py`: ModelForms for Patient and Visit, including validation.
- `views.py`: Class-based views for CRUD operations, filtering, and access control.
- `urls.py`: URL routing for all views including login/logout.
- `templates/`: HTML files for all views, including base layout and error pages.
- `README.md`: The file you’re reading now!
- `400.html`, `403.html`, `404.html`: Custom error pages.

---

## Design Decisions

- Chose Django for its built-in auth system and rapid development tools.
- Built user-facing views instead of relying on Django admin to reinforce learning.
- Limited the scope to a single user role (doctor) for simplicity.
- Initially included pagination, then removed it for a smoother user flow.
- Embedded all styling in `base.html` to avoid managing a static directory.
- Implemented optional `pk` injection to pre-fill the visit form when coming from a patient's profile.
- Used custom error templates to replace Django’s defaults.

---

## Potential Improvements (If I Had More Time)

- Add user registration and password reset.
- Export visit summaries as PDF.
- Introduce visit tags (e.g., "Follow-up", "Urgent").
- Add role-based access (e.g., admin vs. doctor).
- Build a Django REST API.
- Use JavaScript for live search and confirmation dialogs.

---

## Use of AI Tools

I used **ChatGPT** to guide me through architectural questions and help refine HTML/CSS layout. However, all decisions regarding design and implementation were made independently. AI tools served only to **boost productivity**, not to replace my own work.

---
