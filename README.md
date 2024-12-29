# Thexeo AI Project Worker

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
   docker-compose up --build
   app-1  | Data inserted successfully Status Code: 200
   docker-compose stop
   docker-compose build
   docker-compose up -d

$ docker ps
CONTAINER ID   IMAGE           COMMAND                  CREATED         STATUS         PORTS                 NAMES
5286c9738174   thexeo-ai-app   "python app.py"          5 seconds ago   Up 4 seconds                         thexeo-ai-app-1
19db33af9920   mysql:5.7       "docker-entrypoint.s…"   2 hours ago     Up 5 seconds   3306/tcp, 33060/tcp   thexeo-ai-db-1

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

