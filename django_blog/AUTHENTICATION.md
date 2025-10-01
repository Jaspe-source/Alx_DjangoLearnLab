Authentication system docs — summary

Registration: POST /register/ — uses CustomUserCreationForm, requires username + email + password.

Login: GET/POST /login/ — uses Django LoginView; template at templates/blog/login.html.

Logout: GET /logout/ — uses Django LogoutView.

Profile: GET/POST /profile/ — view protected by @login_required. Users can update username, name, and email.

Files changed / added:

blog/forms.py

blog/views.py

blog/urls.py (+ included in project urls.py)

blog/templates/blog/{login.html,logout.html,register.html,profile.html}

optionally blog/models.py if adding Profile.

How to test locally:

Run python manage.py runserver.

Visit /register/ — create account.

Visit /login/ — log in.

Visit /profile/ — update details (must be logged in).

Admin: /admin/ to inspect User and Profile.