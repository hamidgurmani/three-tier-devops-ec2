🚀 Three‑Tier DevOps Project (EC2 • Jenkins • Docker • Kubernetes • Terraform • Ansible)
📌 Overview

This project demonstrates an end‑to‑end DevOps workflow for deploying a production‑style three‑tier application using Infrastructure as Code, Configuration Management, CI/CD, Containers, and Kubernetes.

The goal of this repository is to showcase real‑world DevOps engineering practices, not just a demo app.

🧱 Architecture

High‑level flow:

Developer → GitHub → Jenkins (CI/CD)
                 ↓
            Docker Build
                 ↓
            DockerHub
                 ↓
            Kubernetes (K3s on EC2)
Infrastructure

AWS EC2

Jenkins + Kubernetes (K3s) on single EC2

Terraform

EC2 provisioning

Security Groups

Ansible

Jenkins installation

Docker installation

K3s bootstrap

🧩 Application Layers
Frontend

Nginx‑based static UI

Dockerized

Deployed via Kubernetes Deployment + Service

Backend

Python (FastAPI)

Dockerized REST API

Deployed via Kubernetes Deployment + Service

Database

PostgreSQL

Kubernetes Deployment + Service

⚙️ CI/CD Pipeline (Jenkins)

The pipeline is defined using a Declarative Jenkinsfile and performs the following stages:

Checkout Code from GitHub

Build Backend Docker Image

Build Frontend Docker Image

Authenticate to DockerHub (Credentials‑based)

Push Images to DockerHub

Deploy to Kubernetes using kubectl

Jenkinsfile Location
/three-tier-devops-project/Jenkinsfile
☸️ Kubernetes

Distribution: K3s (lightweight Kubernetes)

Cluster Type: Single‑node control plane

Manifests Location:

/k8s
Running Pods (Example)
backend    → Running
frontend   → Running
postgres  → Running
🔐 Security & Credentials

DockerHub credentials stored securely in Jenkins Credentials Manager

SSH access restricted via Security Group (CIDR‑based)

No secrets hard‑coded in repository

🌐 Networking & Ports
| Component        | Port | Purpose                          |
|------------------|------|----------------------------------|
| Jenkins          | 8080 | CI/CD Web Interface              |
| Kubernetes API   | 6443 | Cluster API Server               |
| Frontend (Nginx) | 80   | User-facing application          |
| Backend (API)    | 8000 | FastAPI backend service          |
| PostgreSQL       | 5432 | Database (internal only)         |
| SSH              | 22   | Server access (IP-restricted)    |

🧪 Validation & Testing
Verify Kubernetes
kubectl get nodes
kubectl get pods
kubectl get svc
Verify CI/CD

Trigger Jenkins job

Confirm Docker images pushed to DockerHub

Confirm pods recreated successfully

📁 Repository Structure
three-tier-devops-project/
├── Jenkinsfile
├── README.md
├── ansible/
│   ├── inventory
│   ├── playbooks
│   └── roles
├── terraform/
├── app/
│   ├── frontend
│   ├── backend
│   └── database
├── k8s/
└── jenkins/
🔁 How a Reviewer Can Test This Project
Option 1: Review Architecture & Code

Inspect Terraform, Ansible, Jenkinsfile, and Kubernetes manifests

Review CI/CD logic and best practices

Option 2: Reproduce on Own AWS Account

Clone repository

Apply Terraform

Run Ansible playbooks

Configure Jenkins credentials

Trigger pipeline

🧠 Key DevOps Concepts Demonstrated

Infrastructure as Code (Terraform)

Configuration Management (Ansible)

CI/CD Automation (Jenkins)

Containerization (Docker)

Orchestration (Kubernetes)

Secure credential handling

Real production troubleshooting & fixes

👤 Author

Hamid Gurmani
GitHub: https://github.com/hamidgurmani
