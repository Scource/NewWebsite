# NewWebsite

Enhancement of TW_info_flow

## PREREQUISITES

- Docker and docker-compose

## SETUP

The first thing to do is to clone the repository:

```
$ git clone https://github.com/Scource/NewWebsite
$ cd NewWebsite
```

#### Docker setup

- From root application folder run `docker compose up`
- Application should be up and running at `http://localhost:3000`

#### PostgresDB setup

- Migrate tables to new DB
  `docker-compose exec backend python manage.py migrate`

* Create first user in new DB
  `docker-compose exec backend python manage.py createsuperuser`
