
---

## 🧱 Part 1: Flask Application (30 Marks)

- `GET /` – Displays "Hello, World!".
- `GET /form` – Shows a form to enter name and age.
- `POST /form` – Displays a personalized greeting.
- Error handling included for invalid input (e.g. non-numeric age).

Flask is served on **[http://localhost:5001](http://localhost:5001)**

---

## 🌐 Part 2: Django Application (40 Marks)

- Homepage displays a list of items (e.g., books).
- Form on the homepage to add new items.
- Admin panel for managing items.

Django is served on **[http://localhost:8001](http://localhost:8001)**

Login to admin panel at `/admin`.

---

## 🐳 Part 3: Docker Compose Setup (30 Marks)

### 📄 Dockerfiles
- Separate Dockerfiles for both Flask and Django apps.

### 🔧 `docker-compose.yml`
- Runs both services on different ports:
  - Flask: `localhost:5001`
  - Django: `localhost:8001`

---


t
