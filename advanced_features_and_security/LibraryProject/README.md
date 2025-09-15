# Advanced Features and Security - Django Project

This project demonstrates **custom user models, permissions, and access control** in Django.

---

## 1. Custom User Model
- Defined in `bookshelf/models.py` using `AbstractUser`.
- Custom fields:
  - `date_of_birth`
  - `profile_photo`
- Authentication is based on **email** instead of username.

---

## 2. Custom Permissions
In the `Book` model (`bookshelf/models.py`), we added custom permissions:

```python
class Meta:
    permissions = [
        ("can_view", "Can view book"),
        ("can_create", "Can create book"),
        ("can_edit", "Can edit book"),
        ("can_delete", "Can delete book"),
    ]
