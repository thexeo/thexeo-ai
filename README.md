# Thexeo AI Project

This project demonstrates how to run a Python application inside Docker containers to interact with a MySQL database. It includes functionality to insert data into a `worker` table and send an email with the data.

## Table of Contents
- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
- [Project Structure](#project-structure)
- [Usage](#usage)
- [Environment Variables](#environment-variables)
- [Contributing](#contributing)
- [License](#license)

## Overview

This repository contains:
- A `Dockerfile` to build the application image.
- A `docker-compose.yml` file to manage MySQL and application services.
- A Python script (`app.py`) that inserts data into MySQL and sends an email.
- A requirements file for Python dependencies.

The application uses GPU capabilities for calculating a 'rate' value, demonstrating how to leverage GPU for computations.

## Prerequisites

- Docker
- Docker Compose
- GPU with CUDA support (optional, for GPU computation)

## Getting Started

1. **Clone the repository:**
   ```bash
   git clone git@github.com:yourusername/thexeo-ai.git
   cd thexeo-ai

2.
   Set up your environment variables:
Create a .env file in the project directory and add the following:
MYSQL_ROOT_PASSWORD=yourpassword
MYSQL_DATABASE=thexeodb
MAIL_USERNAME=your_email@gmail.com
MAIL_PASSWORD=yourmailpassword

Replace yourpassword, your_email@gmail.com, and yourmailpassword with your actual MySQL root password, email address, and email password.
Build and run the containers:
bash
docker-compose up --build

This command will build the Docker images and start the containers.

Project Structure
Dockerfile - Instructions to build the Docker image for the application.
docker-compose.yml - Configuration for Docker Compose to run the services.
app.py - The main Python script which interacts with the database and sends emails.
requirements.txt - List of Python dependencies.
.env - Environment variables file for sensitive information.

Usage
Upon running the application, it will:
Insert a record into the worker table in MySQL.
Send an email with the data from the worker table.

Environment Variables
MYSQL_ROOT_PASSWORD: Password for MySQL root user.
MYSQL_DATABASE: Name of the database to use.
MAIL_USERNAME: Email address used for sending emails.
MAIL_PASSWORD: Password for the email account.

Contributing
Contributions are welcome! Please fork this repository and submit pull requests. Here are some guidelines:

Ensure your code passes existing tests.
Add tests for any new features.
Document your code with clear comments.

License
This project is licensed under the MIT License (LICENSE).

