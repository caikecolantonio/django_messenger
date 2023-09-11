# User-to-User Messaging Backend

**Table of Contents:**

1. [Overview](#overview)
2. [Features](#features)
3. [Requirements](#requirements)
4. [Setup and Installation](#setup-and-installation)
5. [API Documentation](#api-documentation)
6. [Usage](#usage)
    - [User Registration](#user-registration)
    - [User Login and Logout](#user-login-and-logout)
    - [List Users](#list-users)
    - [Send and List Messages](#send-and-list-messages)
    - [CSRF Token Usage in Postman](#csrf-token-usage-in-postman)
7. [Example Postman Configuration](#example-postman-configuration)
8. [User Model](#user-model)

## Overview

This is the backend for a user-to-user messaging application built with Django and Django REST framework. It provides API endpoints for user registration, login, logout, user listing, and messaging.


## Features

- User registration with unique usernames and email addresses.
- User login and logout using session-based authentication.
- Listing all available users for messaging.
- Sending messages between users.
- Listing messages between a user and a specific recipient.
- Pagination for handling a potentially large number of messages.
- Proper error handling and validation for API requests.

## Requirements

- Python 3.x
- Django
- Django REST framework
- Other dependencies (listed in `requirements.txt`)

## Setup and Installation

1. Clone this repository to your local machine:

```bash
git clone https://github.com/yourusername/messaging-backend.git
cd messaging-backend
```

2. Create a virtual environment (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate # On Windows: venv\Scripts\activate
```

3. Install the required dependencies:

```bash
pip install -r requirements.txt
```

4. Run database migrations:

```bash
python manage.py migrate
```

5. Start the development server:

```bash
python manage.py runserver
```

6. Access the API at `http://127.0.0.1:8000/`.

## API Documentation

You can find detailed API documentation by accessing the `/api/docs/` endpoint when the server is running.

## Usage

- Register a user: POST to `/register/` with a JSON body containing `username`, `email`, and `password`.
- Login: POST to `/login/` with a JSON body containing `username` and `password`. This will return a CSRF token for authentication.
- Logout: GET `/logout/`. This logs the user out.
- List users: GET `/users-list/`. This lists all users available for messaging.
- Send a message: POST to `/messages/` with a JSON body containing `recipient` (username or email) and `content`.
- List messages: GET `/list-messages/<recipient_username>/`. Lists all messages between the authenticated user and the specified recipient.
- This URL `/docs/` endpoint provides access to the Swagger UI interface, allowing users to explore and interact with the API documentation in a user-friendly manner.

## CSRF Token Usage in Postman

When you log in to the application, you'll receive a CSRF token as part of the login response. This token is important for authenticating subsequent API requests. Here's how to use it in Postman:

1. **Login**: Send a POST request to `/login/` with your username and password. You'll receive a response that includes a CSRF token. Extract the CSRF token from the response.

2. **Set CSRF Token in Headers**: In Postman, set the `X-CSRFToken` header for subsequent requests. Set the value of this header to the CSRF token you extracted from the login response.

3. **Make Authenticated Requests**: With the CSRF token set in the headers, you can now make authenticated requests to protected endpoints like sending messages or listing messages.

Remember to include the `X-CSRFToken` header in all authenticated requests to ensure proper authentication.

## Example Postman Configuration

For reference, here's how you can configure Postman to use the CSRF token:

1. After logging in and obtaining the CSRF token from the login response, go to the "Headers" section of your request in Postman.

2. Add a new header with the key `X-CSRFToken` and set its value to the CSRF token you extracted.

3. Save the request, and you can now use it to make authenticated requests to the application.


## User Model

This project utilizes Django's built-in User model for user management. Therefore, there is no custom User model defined in this application. Django's User model provides the necessary fields for username, email, and password, which are used for user registration, login, and authentication.
