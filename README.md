# Movie Explorer Platform

A full-stack application for exploring movies, actors, directors, and genres.

## Project Structure

- `backend/` - FastAPI Python backend with SQLite database
- `frontend/` - React TypeScript frontend with Tailwind CSS

## Features

- Browse movies with detailed information
- Filter movies by genre, director, release year, or actor
- View actor and director profiles
- Explore genre collections
- No authentication required

## Getting Started

### Backend Setup

```bash
cd backend
pip install -r requirements.txt
python main.py
```

Backend will run on `http://localhost:8000`
API documentation available at `http://localhost:8000/docs`

### Frontend Setup

```bash
cd frontend
npm install
npm start
```

Frontend will run on `http://localhost:3000`

## Database Schema

- **Movies**: title, release_year, description, poster_url
- **Actors**: name, birth_date, bio, photo_url
- **Directors**: name, birth_date, bio, photo_url
- **Genres**: name, description
- Relationships: Many-to-many between movies-actors, movies-genres; One-to-many movies-directors
