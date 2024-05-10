# Djangorestframework jwt_authentication

## About
Its just a test project
## Test Case Scenarios

- Authentication(jwt)
- User customization
  
## API Endpoints

### Users

- `/account/register/`: User registration endpoint
- `/account/api/token/`: User login endpoint
- `/account/logout/`: User logout endpoint
- `/account/change_password/`: Change user password endpoint
- `/account/api/token/refresh/`: Refresh token endpoint
## Install

```bash
pip install -r requirements.txt
```
## Run

```bash
python manage.py migrate
python manage.py runserver
```
