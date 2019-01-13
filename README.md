# Django Sample Microservice

This is an example microservice written in Django, intended to be used as part of 2hog's Docker trainings.

## Spec
Implements a single endpoint (`GET /`) which:

1. Requires session authentication
2. Requests a greeting via a `POST` request from the greeting service
3. Requests an HTML fragment for the received greeting via a `GET` request from the content service
4. Returns an HTML document to the user, including the received HTML fragment

## Configuration

The Django Sample Microservice accepts configuration via environment variables:
- `POSTGRES_HOST`: The hostname of the Postgres server (default: `postgres`)
- `POSTGRES_USER`: The Postgres user of the database (default: `postgres`)
- `POSTGRES_PASSWORD`: The password of the Postgres user(default: `password`)
- `POSTGRES_PORT`: The port to which the Postgres server listens (default: `5432`)
- `POSTGRES_DB`: The Postgres database to use (default: `postgres`)
- `SECRET_KEY`: Secret key used by Django for cookie signing (default: `thisshouldstaysecretforchristssake`)
- `GREETING_APP_URL`: The host of the greeting service (default: `http://greeting:4567/`)
- `GREETING_APP_USER`: The user to use for Basic Authentication in the greeting service (default: `paris`)
- `GREETING_APP_PASSWORD`: The password to use for Basic Authentication in the greeting service (default: `kasidiaris`)
- `CONTENT_APP_URL`: The host of the content service (default: `http://content:5000/`)
- `CONTENT_APP_USER`: The user to use for Basic Authentication in the content service (default: `antonis`)
- `CONTENT_APP_PASSWORD`: The password to use for Basic Authentication in the content service (default: `kalipetis`)

## Secrets

The Django Sample Microservice also accepts and prefers configuration as secret files for the following settings:

- `/run/secrets/database_url`: The full connection URL for the PostgreSQL database
- `/run/secrets/greeting_app_url`: The host of the greeting service
- `/run/secrets/greeting_app_user`: The user to use for Basic Authentication in the greeting service 
- `/run/secrets/greeting_app_password`: The password to use for Basic Authentication in the greeting service
- `/run/secrets/content_app_url`: The host of the content service
- `/run/secrets/content_app_user`: The user to use for Basic Authentication in the content service 
- `/run/secrets/content_app_password`: The password to use for Basic Authentication in the content service

## Deployment

### Docker Swarm

```sh
docker secret create micro-django-database-url -
docker secret create micro-django-secret-key -
docker secret create micro-django-greeting-app-url -
docker secret create micro-django-greeting-app-user -
docker secret create micro-django-greeting-app-password -
docker secret create micro-django-content-app-url -
docker secret create micro-django-content-app-user -
docker secret create micro-django-content-app-password -
docker stack deploy -c docker-compose.yml docker-training-samples-micro-django
```

### Kubernetes

```sh
kubectl create secret generic docker-training-samples-micro-django-secret \
--from-literal=database_url=postgres://postgres:password@postgres:5432/postgres \
--from-literal=postgres_host=postgres \
--from-literal=postgres_user=postgres \
--from-literal=postgres_password=password \
--from-literal=postgres_port=5432 \
--from-literal=postgres_db=postgres \
--from-literal=secret_key=thisshouldstaysecretforchristssake \
--from-literal=greeting_app_url=http://greeting:4567/ \
--from-literal=greeting_app_user=paris \
--from-literal=greeting_app_password=kasidiaris \
--from-literal=content_app_url=http://content:5000/ \
--from-literal=content_app_user=antonis \
--from-literal=content_app_password=kalipetis \
kubectl apply -f kube/
```

## Development

To develop the Django Sample Microservice, follow these steps:

1. Install Docker ([docs](https://docs.docker.com/install/)) and Docker Compose ([docs](https://docs.docker.com/compose/install/))
2. Clone this repository:
    ```
    git clone https://github.com/2hog/docker-training-samples-micro-django
    ```
3. Launch the app with Docker Compose:
    ```
    docker-compose up
    ```
4. Open your repository with your editor and rock n' roll!

## License

This software is [MIT licensed](LICENSE).