# Thexeo AI Project Worker

Thexeo AI Worker Consent Statement

By installing Thexeo AI Worker, you agree to these terms:

No Personal Data: The software does not collect, store, or share personal information. It only connects to the thexeo.com API for functionality and performs web scraping for specific tasks without accessing personal data.
Privacy Commitment: We respect your privacy and ensure no personal data is compromised during use.
Internet Requirement: Internet connection is needed to access the thexeo.com API and for web scraping.
Updates: This statement may be updated; changes will be communicated in new releases or via the software interface.

This project leverages parallel processing with GPU capabilities to efficiently gather and manage data relevant to digital marketing and SEO for our clients.

How to Earn $THEXEO Token Airdrop
By running the Thexeo AI Project Worker, you can participate in the $THEXEO token airdrop. Here's what you need to do:


Setup the Worker Node:
Ensure you have Docker installed on your machine.
Clone this repository:

bash
git clone https://github.com/thexeo/thexeo-ai.git
Navigate to the project directory:
bash
cd thexeo-ai
Deploy the worker using Docker Compose:
bash
docker-compose up -d

Running the Worker:
Once deployed, the worker will start processing tasks relevant to Thexeo AI's decentralized network. Each task completed increases your eligibility for the token airdrop.

Airdrop Eligibility:

Contribution: The more you contribute by running the worker node, the higher your chances of receiving a larger share of the airdrop.
Periodicity: Airdrops might be distributed at set intervals or upon reaching certain milestones within the project. Check the project's announcements for specific dates.

Claim Your Tokens:
Keep your wallet connected to the project's network. Airdrops will be automatically distributed to eligible addresses. Ensure your wallet address is registered with the project.

Stay Updated:
Regularly check this repository or join Thexeo AI's communication channels (Telegram, Twitter) for updates on airdrop schedules, eligibility criteria, and further instructions.

Note: 
Participation in the airdrop is subject to the terms and conditions set by Thexeo AI. Ensure you comply with all guidelines to stay eligible for the airdrop.
The process and amount of tokens distributed may vary based on network performance, number of participants, and other factors determined by Thexeo AI.

Disclaimer: 
The information provided here is subject to change. Always refer to the latest updates from Thexeo AI for the most current information on airdrops.

Make sure to adjust the specific instructions (like the Git clone URL) to match your actual repository details.

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
   git clone git@github.com:thexeoai/thexeo-ai.git
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

