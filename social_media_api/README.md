# Social Media API

This project implements a basic social media API using Django REST Framework, focusing on user registration, authentication, and profile management.

---

## 🚀 Setup Instructions

### 1️⃣ Clone Repository
```bash
git clone https://github.com/Jaspe-source/Alx_DjangoLearnLab.git
cd Alx_DjangoLearnLab/social_media_api


## Follow & Feed Endpoints

### Follow / Unfollow
- `POST /api/accounts/follow/<user_id>/` — Follow a user (authenticated).
- `DELETE /api/accounts/follow/<user_id>/` — Unfollow a user (authenticated).

### Followers / Following Lists
- `GET /api/accounts/<user_id>/followers/` — List users who follow `<user_id>`.
- `GET /api/accounts/<user_id>/following/` — List users `<user_id>` is following.

### Feed
- `GET /api/posts/feed/` — Returns posts authored by users the current (authenticated) user follows.
  - Ordered by newest first.
  - Supports pagination and `?search=` query on post title/content.
