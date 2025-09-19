#!/usr/bin/env bash
set -e

until docker compose exec db pg_isready -U postgres -d appdb > /dev/null 2>&1; do
  echo "Waiting for PostgreSQL..."
  sleep 2
done

echo "PostgreSQL is ready!"
