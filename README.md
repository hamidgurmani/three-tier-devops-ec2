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
