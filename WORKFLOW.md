# Alembic Migration Workflow

## The 3-Step Loop (repeat for every schema change)
1. Start by editing  models.py
2. alembic revision --autogenerate -m "description"
3. alembic upgrade head

## Key Commands I learned about
- alembic current means  what revision is the DB at?
- alembic history is a full migration chain
- alembic upgrade head apply all pending
- alembic downgrade -1 → roll back one step
- alembic downgrade base → reset everything
- alembic upgrade <rev> → go to specific revision

## Non-Dsestructive Rule
Always ADD columns, never RENAME or DROP in a live deploy.
Rename pattern: add new → backfill → update code → remove old.


# CI/CD Order
tests → build → alembic upgrade head → deploy → health check → deploy → health check
On failure: redeploy old code → alembic downgrade -1

