# Migrations Lab — SQLAlchemy + Alembic + PostgreSQL

A hands-on database migrations project built as part of my DevOps learning path.
Covers the full migration lifecycle from first model to production-grade schema changes.

## Tech Stack

- PostgreSQL 14 (Ubuntu/Vagrant VM)
- SQLAlchemy 2.x (ORM)
- Alembic 1.x (migration tool)
- psycopg2-binary (PostgreSQL driver)
- Python 3.10 + virtualenv

## Project Structure

migrations-lab/
├── alembic/
│   ├── env.py              # wired to Base.metadata
│   ├── script.py.mako      # migration file template
│   └── versions/           # all migration files
├── models.py               # SQLAlchemy User model
├── alembic.ini             # Alembic config + DB connection
├── requirements.txt        # pinned dependencies
└── WORKFLOW.md             # migration command reference

## Migration History

| # | Migration | Type |
|---|-----------|------|
| 1 | create users table | Schema |
| 2 | add is_active to users | Schema |
| 3 | add bio to users | Schema |
| 4 | add first_name and last_name to users | Schema (expand) |
| 5 | backfill first_name and last_name from full_name | Data migration |

## Key Concepts Covered

**Non-destructive migrations** — Adding columns with `server_default` so existing rows
are never left with invalid NULL values on NOT NULL columns.

**The expand-contract pattern** — The production-safe way to rename a column:
1. Add new columns alongside the old one (expand)
2. Backfill data from old to new (data migration)
3. Update app code to use new columns (switch)
4. Drop old column in a later migration (contract)

**Upgrade and downgrade** — Every migration has a working `downgrade()` function.
A CI/CD pipeline can roll back the schema automatically if a deployment fails.

**Migration chain** — Each migration's `down_revision` points to the one before it,
forming a linked list Alembic walks in order. A fresh database runs
`alembic upgrade head` and gets the full schema applied correctly every time.

## Quick Start

```bash
# Clone and set up
git clone https://github.com/AgentPierre/migrations-lab.git
cd migrations-lab
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt

# Configure your DB connection in alembic.ini
# sqlalchemy.url = postgresql://user:password@localhost/dbname

# Apply all migrations
alembic upgrade head

# Check current state
alembic current

# Roll back one step
alembic downgrade -1
```

## Context

Built as part of a structured DevOps curriculum covering CI/CD, IaC, and automated
pipelines. Follows the same migration patterns used by teams at scale — non-destructive
changes, reversible deployments, schema history in version control.
