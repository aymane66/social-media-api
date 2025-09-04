# Social Media API  

A **Django REST Framework (DRF)** based backend for a simple social media app.  
Users can register, follow/unfollow others, create posts, like, comment, and receive notifications — all with secure JWT authentication.  

---

## Features  

- **Authentication**: JWT login, registration, and protected routes.  
- **User System**: Custom user model with profile, bio, profile picture, followers & following.  
- **Posts**: Create, update, delete, search, and filter posts.  
- **Comments**: Add, edit, or delete comments on posts.  
- **Likes**: Like/unlike posts with unique constraints.  
- **Notifications**: Real-time-like system for likes & follows, with read/unread tracking.  
- **Feed**: View posts only from followed users.  

---

## Tech Stack  

- **Backend**: Django, Django REST Framework  
- **Auth**: JWT (SimpleJWT)  
- **Database**: PostgreSQL  
- **Deployment**: Render  
- **Extras**: DRF Pagination, Search, Permissions  

---

## Project Structure  

social_media_api/
│── accounts/ # Custom user model, auth, follow/unfollow
│── posts/ # Posts, comments, likes, feed
│── notifications/ # User notifications
│── social_media_api/ # Project config, settings, urls
│── manage.py



---

## Setup & Installation  

1. **Clone the repo**  
```bash
   git clone https://github.com/<your-username>/social_media_api.git
   cd social_media_api
```

2. Create a virtual environment & install dependencies
```bash
python -m venv venv
source venv/bin/activate   # on Linux/Mac
venv\Scripts\activate      # on Windows
pip install -r requirements.txt
```

3. Set up environment variables (example .env):
```bash
SECRET_KEY=your-secret-key
DEBUG=True
POSTGRES_DB=your-db-name
POSTGRES_USER=your-db-user
POSTGRES_PASSWORD=your-db-password
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
```

4. Run migrations & start server
```bash
python3 manage.py migrate
python3 manage.py runserver
```

## Authentication (JWT)

- Obtain access & refresh token:
```bash
POST /api/token/
```

- Refresh access token:
```bash
POST /api/token/refresh/
```


## API Endpoints

### Account

| Method | Endpoint                            | Description       |
| ------ | ----------------------------------- | ----------------- |
| POST   | `/api/accounts/register/`           | Register new user |
| GET    | `/api/accounts/profile/`            | Get own profile   |
| POST   | `/api/accounts/follow/<user_id>/`   | Follow user       |
| POST   | `/api/accounts/unfollow/<user_id>/` | Unfollow user     |


### Posts

| Method | Endpoint                  | Description                      |
| ------ | ------------------------- | -------------------------------- |
| GET    | `/api/posts/`             | List all posts                   |
| POST   | `/api/posts/`             | Create a new post                |
| GET    | `/api/feed/`              | Get feed (followed users’ posts) |
| POST   | `/api/posts/<id>/like/`   | Like post                        |
| POST   | `/api/posts/<id>/unlike/` | Unlike post                      |


### Comments

| Method | Endpoint         | Description       |
| ------ | ---------------- | ----------------- |
| GET    | `/api/comments/` | List all comments |
| POST   | `/api/comments/` | Add comment       |


### Notifications

| Method | Endpoint                        | Description            |
| ------ | ------------------------------- | ---------------------- |
| GET    | `/api/notifications/`           | List all notifications |
| POST   | `/api/notifications/<id>/read/` | Mark notification read |
