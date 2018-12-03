# Sample Django Microservice

This is an example microservice written in Django, intended to be used as part of 2hog's Docker trainings.

## Spec
It provides a sign in mechanism along with a single endpoint (`GET /`), which:

1. Requires session authentication
2. Requests a greeting via a `POST` request to the **greeting** service
3. Passes the provided greeting via a `GET` URL parameter to the **content** service
4. Returns the received HTML fragment as part of a complete HTML document to the user

## Deployment

Before deploying this app with Docker Swarm or Kubernetes, make sure to build its image by running the following command

```sh
docker build -t 2hog/docker-training-samples-micro-django
```

### Docker Swarm

```sh
docker stack deploy -c docker-compose.yml docker-training-samples-micro-django
```

### Kubernetes

```sh
kubectl apply -f kube/
```

## License

This software is [MIT licensed](LICENSE).