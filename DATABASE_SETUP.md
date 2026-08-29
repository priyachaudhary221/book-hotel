# Database Migration: SQLite → PostgreSQL (Neon)

## What changed

1. **settings.py** – Replaced SQLite with PostgreSQL using your Neon connection string.
2. **requirements.txt** – Added `psycopg2-binary`, `whitenoise`, `dj-database-url`.
3. Migrations have already been applied successfully to your Neon database.

## Connection details used

- Host: `ep-cold-thunder-aeahf5ew-pooler.c-2.us-east-2.aws.neon.tech`
- Database: `neondb`
- User: `neondb_owner`
- SSL: required

## How to run locally

```bash
pip install -r requirements.txt
python manage.py migrate   # already done, but safe to re-run
python manage.py createsuperuser
python manage.py runserver
```

## On Vercel / production

Set the environment variable:

```
DATABASE_URL=postgresql://neondb_owner:npg_RejAm7EBwX3c@ep-cold-thunder-aeahf5ew-pooler.c-2.us-east-2.aws.neon.tech/neondb?sslmode=require&channel_binding=require
```

(You can also override SECRET_KEY and set DEBUG=False)

## Notes

- SQLite file (`db.sqlite3`) is no longer used and can be deleted.
- All existing migrations were applied cleanly to the new PostgreSQL database.
- WhiteNoise is configured so static files work on Vercel.
