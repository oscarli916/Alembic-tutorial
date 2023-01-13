## Start Database

`docker compose up`

## Alembic

-   Change `sqlalchemy.url` in `alembic.ini`

-   Create migration script (manually)

`alembic revision -m "<operation for migration>"`

1. Implement upgrade and downgrade
2. `alembic upgrade head`/`alembic downgrade -1`

-   Create migration script (auto)

1. Create model
2. Edit env.py (Import models, metadata \* if more than 1 than `[model1.metadata, model2.metadata]`)
3. `alembic revision --autogenerate -m "<operation for migration>"`
4. `alembic upgrade head`/`alembic downgrade -1`
