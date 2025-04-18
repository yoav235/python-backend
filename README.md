# Aqua - Home Assignment

This is a simple Django-based REST server that manages user data.

## ✅ Features

- Reads user data from a `users.json` file on server start
- Stores user data in a Python dictionary (`ID` as key)
- Supports the following REST API endpoints:

### API Endpoints

| Method | URL                        | Description                            |
|--------|----------------------------|----------------------------------------|
| GET    | `/users/`                  | Returns a list of all user names       |
| GET    | `/users/<name>/`          | Returns full user details by name      |
| POST   | `/users/create/`          | Creates a new user                     |

### User data includes:
- ID
- Phone Number
- Name
- Address

### Bonus Features:
- Validates Israeli ID (with control digit check)
- Validates Israeli phone number format (`05X-XXXXXXX` or `05XXXXXXXX`)
- Rejects invalid users from `users.json` with a console message

---

## 🧪 Example `POST` Body (JSON):
```json
{
  "id": "123456782",
  "name": "David Cohen",
  "phone": "052-1234567",
  "address": "Herzl St 12, Tel Aviv"
}
```

---

## 🚀 Setup Instructions (Linux)

### Option 1: Clone from GitHub
```bash
git clone https://github.com/yoav235/python-backend.git
cd ./python-backend
```

### Option 2: If you received a ZIP file
Extract the ZIP and open the folder:
```bash
cd aqua-assignment
```

### Create virtual environment
```bash
python3 -m venv venv
source venv/bin/activate
```

### Install dependencies
```bash
pip install -r requirements.txt
```

### Run migrations
```bash
python manage.py migrate
```

### Start the development server
```bash
python manage.py runserver
```

The server will be available at `http://127.0.0.1:8000/`.

---

## 📁 File Structure

```
project/
├── manage.py
├── users.json              # Input user file
├── requirements.txt
├── README.md
├── users/
│   ├── views.py
│   ├── urls.py
│   └── ...
├── djangoProject/
│   ├── settings.py
│   └── urls.py
```

---


## ✅ Running Tests

To run the tests (after setting up the environment and installing dependencies), use:

```bash
python manage.py test
```

This will run the test suite defined in `users/tests.py`.

---

## 🔐 Accessing Django Admin Panel

To access the Django Admin interface and manage users visually:

### 1. Create a superuser
```bash
python manage.py createsuperuser
```
You will be prompted to enter a username, email (optional), and password.

### 2. Run the server
```bash
python manage.py runserver
```

### 3. Open your browser and go to:
```
http://127.0.0.1:8000/admin/
```

### 4. Log in using the superuser credentials you just created.

Once logged in, you will see the `User` model and be able to add, edit, or delete users via a simple web interface.
