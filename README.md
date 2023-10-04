---
# Secret Server 
Secret Server implementation for Allmyles Full Stack Developer homework. By using the frontend application or the server api you can store and retrieve secret strings in a hashed format. Secrets may have an expiration and can be retrieved only for a limited amount of time. 

## 🔨 Built with
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)
![Next.js](https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white)
![Material UI](https://img.shields.io/badge/Material--UI-0081CB?style=for-the-badge&logo=material-ui&logoColor=white)

## 💾 Setup
### Backend
```
cd backend/
python -m venv venv
source venv/bin/activate  # For Windows use `venv\Scripts\activate`
pip install -r requirements.txt
```
### Frontend
```
  cd ../frontend/
  npm install
```
## 🚀 Usage
### Backend
The server is hosted at https://secret-server-api-a8ae5f120a2a.herokuapp.com
You can send secrets through https://secret-server-api-a8ae5f120a2a.herokuapp.com/api/secret/ with 'application/x-www-form-urlencoded' encoding.
When sending a secret, ensure your POST request uses the `application/x-www-form-urlencoded` content type. Below are the parameters that you should include in the request body:

| Key               | Value Description                               | Type    | Requirement  |
|-------------------|-------------------------------------------------|---------|--------------|
| `secret_text`     | The secret message you want to share.           | String  | Required     |
| `expireAfterViews`| The number of views after which the secret should expire. | Integer | Optional     |
| `expireAfter`     | The time (in minutes) after which the secret should expire. | Integer | Optional     |

You can retrive the secrets through https://secret-server-api-a8ae5f120a2a.herokuapp.com/api/secret/{hash} .
### 🔧 Testing
After cloning the repository and setting up the backend you can run api tests by running: 
```
python manage.py migrate
python manage.py test secret_server.tests.secret_api_test.SecretAPITest
```
### Frontend
The app is deployed at [`here`](https://secret-server-frontend-654ae452fccd.herokuapp.com/).
You can create or retrive secrets after navigating to the corresponding pages from the homepage. For retrieving secrets you can toggle on and off recieving XML response type.
