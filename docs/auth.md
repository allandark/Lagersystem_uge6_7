
| Method | Endpoint             | Description                        | Auth Required | Payload Model           | Response Code |
|--------|----------------------|------------------------------------|---------------|--------------------------|----------------|
| POST   | `/login`               | Login to user                      | No            | `login_model`           | 200 / 401 / 400 |
| POST   | `/register`            | Register new user                  | Yes (JWT)     | `login_model`           | 201            |
| POST   | `/change_password`     | Change password of existing user   | Yes (JWT)     | `change_password_model` | 200 / 401       |
| POST   | `/change_username`     | Change username of existing user   | Yes (JWT)     | `change_username_model` | 200 / 401       |
