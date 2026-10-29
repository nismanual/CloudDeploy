# CloudDeploy Deployment Guide

## 1. Overview

CloudDeploy is a FastAPI application deployed as a Docker container on AWS EC2.

The deployment workflow uses GitHub Actions for testing and Docker image publishing. The EC2 instance periodically checks GitHub Container Registry (GHCR) for a newer image and updates the running container.

## 2. Deployment Architecture

1. A developer pushes code to the `main` branch.
2. GitHub Actions runs automated tests.
3. The workflow builds a Docker image and publishes it to GHCR.
4. An EC2 systemd timer periodically checks for an updated image.
5. When an update is available, the deployment script replaces the running container.

## 3. Verify the Application

Open these endpoints in a browser:

- Application: http://43.204.232.40/
- Health check: http://43.204.232.40/health
- Version: http://43.204.232.40/version
- Interactive API documentation: http://43.204.232.40/docs

Expected health-check response:

```json
{"status":"healthy"}
```

## 4. Verify the CI/CD Workflow

1. Open the repository's Actions tab.
2. Select the latest CloudDeploy CI workflow run.
3. Confirm the automated test and Docker image publishing jobs succeeded.
4. Open the GHCR package page to inspect published image tags.

## 5. Server-Side Troubleshooting

Connect to the EC2 instance using SSH and the configured key.

Check the running container:

```bash
docker ps
docker logs --tail 100 clouddeploy
```

Check the deployment timer:

```bash
sudo systemctl status clouddeploy-update.timer
sudo systemctl list-timers clouddeploy-update.timer
```

Inspect recent update logs:

```bash
sudo journalctl -u clouddeploy-update.service -n 100 --no-pager
```

Verify the API locally on the EC2 instance:

```bash
curl -s http://localhost/health
curl -s http://localhost/version
```

## 6. Security and Cost Notes

- The public demo currently uses HTTP and should not be treated as a production-secure service.
- Never commit private SSH keys, credentials, access tokens, or other secrets to the repository.
- Monitor AWS billing and account-plan status before adding infrastructure or expanding the deployment.
- The public IP may change if the EC2 instance is stopped and started.

## 7. Current Deployment Model

GitHub Actions publishes images to GHCR. The EC2 instance checks the registry periodically using a systemd timer. Deployment is not directly triggered by an SSH connection from GitHub Actions.

Rollback and recovery procedures should be tested on the actual server before relying on them in production.
