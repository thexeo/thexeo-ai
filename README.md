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
