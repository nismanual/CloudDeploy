# CloudDeploy — Containerized CI/CD Deployment Platform

CloudDeploy is a containerized FastAPI application with an automated CI/CD workflow that builds, tests, publishes, and deploys application updates.

The project demonstrates automated testing, Docker image publishing, cloud deployment, health monitoring, and periodic deployment updates using AWS EC2.

## Architecture

Developer Push → GitHub Actions → Automated Tests → Docker Image Build → GitHub Container Registry (GHCR) → AWS EC2 → Running FastAPI Application

## Tech Stack

- **Backend:** Python, FastAPI
- **Testing:** Pytest, HTTPX
- **Containerization:** Docker
- **CI/CD:** GitHub Actions
- **Container Registry:** GitHub Container Registry (GHCR)
- **Cloud Infrastructure:** AWS EC2
- **Deployment Automation:** Bash, systemd timer
- **Version Control:** Git, GitHub

## Features

- REST API with health and version endpoints
- Automated tests executed through GitHub Actions
- Docker image build and publishing to GHCR
- Containerized deployment on AWS EC2
- Periodic image checks and automated application updates
- Previous-container preservation during updates to support rollback
- Health-check endpoint for basic service verification

## API Endpoints

| Endpoint | Purpose |
|---|---|
| `/` | Application information and running status |
| `/health` | Health check |
| `/version` | Application version information |
| `/docs` | Interactive FastAPI documentation |

## CI/CD Workflow

1. Code changes are pushed to the GitHub repository.
2. GitHub Actions installs dependencies and runs automated tests.
3. The workflow builds a Docker image and publishes it to GHCR.
4. An AWS EC2 systemd timer periodically checks for a newer image.
5. When a new image is detected, the deployment script updates the running container.

**Note:** The EC2 instance currently checks the registry periodically; GitHub Actions does not directly initiate deployment over SSH.

## Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/nismanual/CloudDeploy.git
cd CloudDeploy
```

### 2. Install dependencies

```bash
python -m venv .venv
```

Activate the environment:

**Windows PowerShell**
```powershell
.venv\Scripts\Activate.ps1
```

**Linux/macOS**
```bash
source .venv/bin/activate
```

Install the required packages:

```bash
pip install -r requirements.txt
```

### 3. Start the application

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

### 4. Open the endpoints

- Application: http://127.0.0.1:8000/
- Health check: http://127.0.0.1:8000/health
- Version: http://127.0.0.1:8000/version
- API documentation: http://127.0.0.1:8000/docs

### 5. Run tests

```bash
pytest -v
```

## Deployment Verification

After deployment, verify that the application responds correctly:

```bash
curl http://localhost/health
curl http://localhost/version
```

Expected health-check response:

```json
{"status":"healthy"}
```

The version endpoint reports the deployed application version.

## Repository Structure

```text
CloudDeploy/
├── .github/
│   └── workflows/
├── app/
├── tests/
├── Dockerfile
├── .dockerignore
├── requirements.txt
└── README.md
```

## Future Improvements

- HTTPS with a domain and TLS certificate
- Deployment notifications and improved observability
- Automated rollback based on health-check failures
- Infrastructure provisioning using Terraform
- More comprehensive integration tests

## Author

**Nisigandha Mallick**

GitHub: [@nismanual](https://github.com/nismanual)

---

*Educational DevOps project demonstrating containerization, CI/CD automation, container registry integration, and cloud deployment.*
