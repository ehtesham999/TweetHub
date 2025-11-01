# TweetHub

TweetHub is a X-like web application built with Django. Users can register, log in, create, edit, and delete tweets (with optional images). The app features user authentication, media uploads, and a clean responsive UI.

---

## Features

- User registration and login/logout
- Tweet creation, editing, and deletion (CRUD)
- Image upload support for tweets
- Only tweet owners can edit or delete their tweets
- Guest users can view tweets but must log in to post or manage tweets
- Responsive, modern UI with clear navigation
- Secure user authentication and permissions

---
## Tech Stack

- **Backend:** Django 5.2.7 (Python 3.8+)  
- **Database:** PostgreSQL  
- **Frontend:** HTML, CSS, Bootstrap  
- **Image Handling:** Pillow  
- **Environment Management:** python-dotenv  

---
## Project Structure

```
TweetHub/
├── manage.py
├── requirements.txt
├── tweethub_project/
│   ├── settings.py
│   ├── urls.py
│   └── ...
├── tweetApp/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   ├── templates/
│   │   ├── tweet_list.html
│   │   ├── tweet_form.html
│   │   ├── tweet_delete.html
│   │   └── ...
│   └── ...
├── templates/
│   ├── base.html
│   ├── tweets.html
│   └── registration/
│       ├── login.html
│       └── register.html
├── media/
└── staticfiles/
```
---


## Security & Permissions

- Only authenticated users can create, edit, or delete tweets.
- Users can only modify their own tweets.
- Guests can view tweets but must register/login to interact.

---
