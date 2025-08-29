#!/bin/sh
# start.sh

# Default values for DB host/port
DB_HOST=${DB_HOST:-db}
DB_PORT=${DB_PORT:-5432}

echo "Waiting for PostgreSQL at $DB_HOST:$DB_PORT..."

# Wait until PostgreSQL is ready
while ! nc -z $DB_HOST $DB_PORT; do
  echo "PostgreSQL is unavailable - sleeping"
  sleep 2
done

echo "PostgreSQL is up - starting FastAPI"

# Start your FastAPI app
# Replace "main:app" with your actual app module if different
uvicorn main:app --host 0.0.0.0 --port 8000
