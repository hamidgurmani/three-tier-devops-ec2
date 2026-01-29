🚀 Three-Tier DevOps Project (Terraform + Ansible + Jenkins + Docker + Kubernetes)
📌 Project Overview

This project demonstrates a production-style DevOps CI/CD pipeline for a three-tier application using modern DevOps tools and best practices.

It covers the complete DevOps lifecycle:

Infrastructure provisioning

Configuration management

CI/CD automation

Containerization

Kubernetes deployment

The goal is to show real-world DevOps skills, not just theory.

🏗️ Architecture

Three-Tier Application

Frontend → Nginx (HTML)

Backend → FastAPI (Python)

Database → PostgreSQL

Infrastructure & Tools

AWS EC2 – Compute

Terraform – Infrastructure as Code

Ansible – Configuration Management

Docker – Containerization

K3s (Kubernetes) – Orchestration

Jenkins – CI/CD Automation

Docker Hub – Image Registry


⚙️ Stage 1 – Infrastructure (Terraform)

Terraform provisions:

EC2 instance

Security Groups

SSH access

Outputs (Public IP, SSH command)

Commands
terraform init
terraform plan
terraform apply

⚙️ Stage 2 – Configuration Management (Ansible)

Ansible configures the EC2 instance by:

Installing Docker

Installing Jenkins

Installing K3s (Kubernetes)

Configuring kubeconfig for Jenkins & ubuntu user

Inventory Example
[jenkins_k8s]
jenkins ansible_host=<EC2_PUBLIC_IP> ansible_user=ubuntu

Run Playbook
ansible-playbook -i inventory/hosts.ini playbooks/site.yml

⚙️ Stage 3 – Containerization (Docker)

Backend and frontend are containerized

Images are built inside Jenkins

Images are pushed to Docker Hub

Example images:

hamid009/backend:latest
hamid009/frontend:latest

⚙️ Stage 4 – Kubernetes (K3s)

Kubernetes objects:

Deployments

Services

Pods

Verify
kubectl get nodes
kubectl get pods
kubectl get svc

⚙️ Stage 5 – CI/CD Pipeline (Jenkins)
Jenkinsfile Responsibilities

Checkout code from GitHub

Build backend & frontend Docker images

Login to Docker Hub

Push images

Deploy to Kubernetes

🌐 Networking & Ports

| Component        | Port | Purpose                          |
|------------------|------|----------------------------------|
| Jenkins          | 8080 | CI/CD Web Interface              |
| Kubernetes API   | 6443 | Cluster API Server               |
| Frontend (Nginx) | 80   | User-facing application          |
| Backend (API)    | 8000 | FastAPI backend service          |
| PostgreSQL       | 5432 | Database (internal only)         |
| SSH              | 22   | Server access (IP-restricted)    |


✅ Validation & Testing
Kubernetes
kubectl get pods
kubectl get nodes

Jenkins

Jenkins UI accessible on port 8080

Successful pipeline build confirms CI/CD working

🔐 Security & Best Practices

SSH access restricted by IP

Secrets stored in Jenkins Credentials

Infrastructure managed via IaC

No hardcoded passwords in code

Modular Ansible roles

📌 What This Project Demonstrates

✔ Real DevOps workflow
✔ Infrastructure as Code
✔ Configuration Management
✔ CI/CD Automation
✔ Docker & Kubernetes
✔ Troubleshooting real production issues

👤 Author

Hamid Gurmani
DevOps Engineer
GitHub: https://github.com/hamidgurmani
