# Three-Tier DevOps Project – CI/CD with Jenkins, Kubernetes, Terraform & Ansible

## 📌 Project Overview
This project demonstrates a **production-style DevOps workflow** for deploying a **three-tier application** using modern DevOps tools and best practices.

The focus is on:
- Infrastructure as Code
- Configuration Management
- CI/CD automation
- Containerization & orchestration

This project was built incrementally to reflect **real-world DevOps problem solving**, not just a demo setup.

---

## 🏗️ Architecture Overview

**Three-tier application**
- Frontend (Nginx)
- Backend (FastAPI)
- Database (PostgreSQL)

**Infrastructure & Tools**
- **Terraform** – AWS EC2 provisioning
- **Ansible** – Server configuration & automation
- **Docker** – Containerization
- **Kubernetes** – Application orchestration
- **Jenkins** – CI/CD pipeline

---

## 🔌 Network Ports & Services

| Component        | Port | Purpose                          |
|------------------|------|----------------------------------|
| Jenkins          | 8080 | CI/CD Web Interface              |
| Kubernetes API   | 6443 | Cluster API Server               |
| Frontend (Nginx) | 80   | User-facing application          |
| Backend (API)    | 8000 | FastAPI backend service          |
| PostgreSQL       | 5432 | Database (internal only)         |
| SSH              | 22   | Server access (IP-restricted)    |


## 📂 Repository Structure

```text
three-tier-devops-project/
├── Jenkinsfile                # CI/CD pipeline definition
├── app/                        # Application source code
│   ├── frontend/
│   ├── backend/
│   └── database/
├── k8s/                        # Kubernetes manifests
├── terraform/                  # Infrastructure as Code (AWS)
│   ├── main.tf
│   ├── provider.tf
│   ├── variables.tf
│   └── outputs.tf
├── ansible/                    # Configuration management
│   ├── inventory/
│   ├── playbooks/
│   └── roles/                  # (To be extended)
└── README.md

🚀 Workflow Summary
1️⃣ Infrastructure Provisioning (Terraform)

AWS EC2 instance provisioned

Security groups configured

SSH access restricted via CIDR

Outputs include public IP & SSH command

2️⃣ Configuration Management (Ansible)

Ansible used as automation engine

Docker installation fully automated

System bootstrapped using idempotent playbooks

Current progress checkpoint: Docker installed via Ansible

3️⃣ CI/CD Pipeline (Jenkins)

Jenkins runs inside Docker

Builds Docker images

Deploys to Kubernetes cluster

4️⃣ Container Orchestration (Kubernetes)

Kubernetes manifests for all tiers

Services & deployments separated

Designed for CI-driven deployments

## ⚙️ Environment & Assumptions

- OS: Ubuntu 20.04 / 22.04 LTS
- Cloud: AWS EC2
- User: `ubuntu`
- Access:
  - SSH key-based authentication
  - Security groups restrict SSH by IP
- Tools installed via automation (Ansible):
  - Docker
  - kubectl
  - Jenkins (Docker-based)


🔐 Security & Best Practices

Infrastructure defined as code

No credentials committed

SSH access restricted by IP

Separation of concerns (IaC vs config vs app)

📌 Status

🟡 In Progress

Completed:

Terraform infrastructure

Ansible baseline

Docker automation

Jenkins CI pipeline (functional)

Planned:

Kubernetes cluster setup via Ansible

Jenkins-driven Kubernetes deployments

Ansible roles refactor

## ✅ Validation & Testing

### Infrastructure
```bash
terraform plan
terraform apply
Ansible Connectivity
ansible -i inventory/hosts.ini all -m ping
Docker
docker ps
docker images
Jenkins
Access Jenkins UI:

http://<EC2_PUBLIC_IP>:8080
Kubernetes
kubectl get nodes
kubectl get pods -A
kubectl get svc

👤 Author

Hamid Gurmani
DevOps Engineer (Hands-on CI/CD, Cloud & Automation)

📬 Notes for Reviewers

This repository is intentionally structured to reflect real DevOps workflows rather than a single-command demo.

Each stage can be reviewed independently:
