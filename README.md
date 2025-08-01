# 241-353 AI ECOSYSTEM MODULE

## Flask Notes App with PostgreSQL

### Project Overview

A simple web application built with Flask, SQLAlchemy, and PostgreSQL, allowing users to create, edit, delete, and tag notes. The app uses Docker for easy setup and includes pgAdmin for managing the PostgreSQL database.

---

### Features

- Create, view, edit, and delete notes.
- Manage tags (view, edit, delete).
- Add multiple tags to each note.
- Tag-based note filtering.

---


### Setup & Installation

Ensure that you have Python installed on your system before proceeding.

1. Clone the repository:
   ```bash
   git clone https://github.com/Keetasin/postgresql-flask.git
   ```
2. Navigate to the project directory:
   ```bash
   cd postgresql-flask
   ```
3. Create a virtual environment:
   ```bash
   python -m venv venv
   ```
4. Activate the virtual environment:
   - On Windows:
      ```bash
      venv\Scripts\activate
      ```
   - On macOS/Linux:
      ```bash
      source venv/bin/activate
      ```
5. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
6. Start PostgreSQL and pgAdmin using Docker:
   ```bash
   docker-compose up -d
   ```
7. To manage the database visually via pgAdmin:
   ```bash
   http://localhost:7080/
   ```
---

### Running and Viewing the Application

Ensure you are inside the project directory, have activated the virtual environment,  
and started PostgreSQL and pgAdmin with `docker-compose up -d`.

1. Run the application:
   ```bash
   python psunote/noteapp.py
   ```
2. Open your browser and go to the Flask app:
   ```bash
   http://127.0.0.1:5000/
   ```