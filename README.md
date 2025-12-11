# dockerfile-buildpack-demo

# STAGE 1: INIT

1. Create repo for buildpack images

```bash
gcloud artifacts repositories create buildpack \
    --repository-format=docker \
    --location=us-west1
```

2. Create repo for dockerfile images

```bash
gcloud artifacts repositories create dockerfile \
    --repository-format=docker \
    --location=us-west1
```

3. Build and push buildpack images

```bash
pack-cli build us-west1-docker.pkg.dev/gke-playground-477517/buildpack/my-app:v1 \
    --builder gcr.io/buildpacks/builder:google-22 \
    --publish
```

4. Build and push dockerfile images

```bash
docker build -t us-west1-docker.pkg.dev/gke-playground-477517/dockerfile/my-app:v1 -f ./docker/Dockerfile .
docker push us-west1-docker.pkg.dev/gke-playground-477517/dockerfile/my-app:v1
```

5. Deploy

```bash
kubectl apply -f ./k8s
```

# STAGE 2: NEW APP 

```bash
pack-cli build us-west1-docker.pkg.dev/gke-playground-477517/buildpack/my-node-app:v1 \
    --builder gcr.io/buildpacks/builder:google-22 \
    --publish
```

