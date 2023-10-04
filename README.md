---
# Secret Server 
Secret Server implementation for Allmyles Full Stack Developer homework. The server can store and retrieve secrets strings in a hashed format. Secrets may have an expiration and can be retrieved only for a limited
amount of time. 

## 🛠️ Built with
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)

## 🚀 Usage
The server is hosted at https://secret-server-api-a8ae5f120a2a.herokuapp.com
You can send secrets through https://secret-server-api-a8ae5f120a2a.herokuapp.com/api/secret/ with 'application/x-www-form-urlencoded' encoding.
Structure your POST request body similar to this:
```json
{
    "hash": "2fcd0441-6a39-4ee0-8f35-fb2b8f964a1c",
    "secret_text": "YourSecretHere",
    "createdAt": "2023-10-04T10:41:15.217850+00:00",
    "expiresAt": "2023-10-04T11:41:15.217850+00:00"
}

You can retrive the secrets through https://secret-server-api-a8ae5f120a2a.herokuapp.com/api/secret/{hash} .
