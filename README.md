---
# Secret Server 
Secret Server implementation for Allmyles Full Stack Developer homework. The server can store and retrieve secrets strings in a hashed format. Secrets may have an expiration and can be retrieved only for a limited
amount of time. 

## 🛠️ Built with
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)

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
