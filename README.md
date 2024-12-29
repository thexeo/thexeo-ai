# Thexeo AI Project

This project leverages parallel processing with GPU capabilities to efficiently gather and manage data relevant to digital marketing and SEO for our clients.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
- [Project Structure](#project-structure)
- [Usage](#usage)
- [Environment Variables](#environment-variables)
- [Contributing](#contributing)
- [License](#license)

## Overview

**Thexeo AI** is designed to process digital marketing and SEO data at high speed using GPU-accelerated computations. It automates the collection of visitor statistics from `thexeo.com`, calculates performance metrics, and stores this data in a MySQL database for further analysis or reporting. This project serves as a backend solution for clients needing real-time, high-performance data processing in their marketing strategies.

## Features

- **GPU-Accelerated Computations:** Performs calculations using CUDA-enabled GPUs for faster processing.
- **SEO and Digital Marketing Data:** Collects visitor data from `thexeo.com` to analyze website performance.
- **Database Integration:** Automatically inserts processed data into a MySQL database for storage and retrieval.
- **Email Reporting:** Sends periodic emails with the latest data to keep clients informed.

## Prerequisites

- Docker
- Docker Compose
- GPU with CUDA Support (for enhanced performance)
- Python with necessary packages (installed via Docker)

## Getting Started

1. **Clone the Repository:**
   ```bash
   git clone git@github.com:yourusername/thexeo-ai.git
   cd thexeo-ai

Setup Environment Variables:
Create a .env file based on .env.example and fill in your credentials.
Build and Run:
bash
docker-compose up --build

Project Structure
Dockerfile - Sets up the environment for Python application with GPU support.
docker-compose.yml - Manages MySQL and app services.
app.py - Main script handling data collection, processing, database operations, and email sending.
requirements.txt - Python dependencies.
.env.example - Template for environment variables.

Usage
The application will:
Collect visitor data from thexeo.com.
Perform GPU-accelerated rate calculations.
Store this data in MySQL under the worker table.

Environment Variables
MYSQL_ROOT_PASSWORD
MYSQL_DATABASE
MAIL_USERNAME
MAIL_PASSWORD

Contributing
Feel free to contribute:

Fork the repo.
Create your feature branch (git checkout -b feature/FooBar).
Commit your changes (git commit -am 'Add some FooBar').
Push to the branch (git push origin feature/FooBar).
Create a new Pull Request.
