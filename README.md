# RECIPE DJANGO APP

## Commands

### Execute the container

```bash
docker compose up
```

### Running commands inside the container

```bash
docker compose run --rm app sh -c ""
```

### Lint

```bash
docker compose run --rm app sh -c "flake8"
```

### Test

```bash
docker compose run --rm app sh -c "python manage.py test"
```
