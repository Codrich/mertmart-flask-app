# 🚀 Mertmart Cloud Application (Flask + AWS ECS Fargate)

**Production-style cloud application built for Mertmart Group**, demonstrating real-world **Cloud Engineering, DevOps, and Security practices** using AWS.

## 🧠 Project Overview

This project is a **containerized Flask web application** deployed on AWS using modern cloud-native architecture. It serves as part of the **Mertmart Group platform**, supporting internal business workflows while showcasing scalable and secure deployment strategies.

💡 Designed to reflect **real-world DevOps and cloud engineering practices**, not just a demo project.

## 🏗️ Architecture

![Image](https://miro.medium.com/1%2AjcmnWZ5X17ABsRgJXCaiUA.png)

![Image](https://media2.dev.to/dynamic/image/width%3D1600%2Cheight%3D900%2Cfit%3Dcover%2Cgravity%3Dauto%2Cformat%3Dauto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fefsjl54qspy1muw7j7kk.png)

![Image](https://d2908q01vomqb2.cloudfront.net/fe2ef495a1152561572949784c16bf23abb28057/2020/02/05/Screen-Shot-2020-01-08-at-5.55.15-PM.png)

![Image](https://media2.dev.to/dynamic/image/width%3D1280%2Cheight%3D720%2Cfit%3Dcover%2Cgravity%3Dauto%2Cformat%3Dauto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fgnnd2c1i7ksf3ou2fu7q.png)

### 🔹 Components

* **Application:** Python Flask
* **Containerization:** Docker
* **Registry:** Amazon Elastic Container Registry (ECR)
* **Compute:** AWS ECS Fargate (serverless containers)
* **Load Balancer:** Application Load Balancer (ALB)
* **CI/CD:** GitHub Actions
* **Monitoring:** AWS CloudWatch
* **Networking:** VPC with public/private subnets

## ⚙️ Key Features

* ✅ Containerized application for consistent deployment
* ✅ Scalable serverless compute using ECS Fargate
* ✅ Automated CI/CD pipeline for rapid deployment
* ✅ Load-balanced architecture for high availability
* ✅ Secure IAM-based access control
* ✅ Centralized logging and monitoring

## 🧩 Real-World Business Context (Mertmart)

This application is actively used as part of the **Mertmart Group cloud platform**:

* Supports **internal business operations**
* Serves as a base for **inventory and order management systems**
* Demonstrates how small businesses can leverage **enterprise-grade cloud architecture**

💥 This transforms the project from a “demo” → **real engineering experience**

## 🚀 Deployment Workflow

```bash
# Build Docker image
docker build -t mertmart-app .

# Tag image
docker tag mertmart-app:latest <ECR-REPO-URI>

# Push to ECR
docker push <ECR-REPO-URI>

# Deploy via ECS Fargate (via console or CI/CD)

## 🔁 CI/CD Pipeline

* Code pushed to GitHub
* GitHub Actions builds Docker image
* Image pushed to Amazon ECR
* ECS service updated automatically

💡 Enables **fast, repeatable, and reliable deployments**

## 🔐 Security Considerations

* IAM roles with **least privilege access**
* Secure container image storage in ECR
* Environment variables for sensitive configurations
* Network isolation via VPC and security groups
* Monitoring and logging via CloudWatch

## 📂 Project Structure

```id="mjla00"
├── app.py              # Flask application
├── Dockerfile          # Container configuration
├── requirements.txt    # Dependencies
```

## 📊 Skills Demonstrated

* Cloud Infrastructure (AWS)
* Containerization (Docker)
* Orchestration (ECS Fargate)
* CI/CD Automation (GitHub Actions)
* Cloud Security (IAM, Networking)
* Monitoring & Observability (CloudWatch)

## 📈 Future Enhancements

* 🔹 Add database integration (Amazon RDS / DynamoDB)
* 🔹 Implement authentication (JWT / Cognito)
* 🔹 Add autoscaling policies
* 🔹 Integrate advanced monitoring dashboards
* 🔹 Introduce basic fraud/anomaly detection logic

## 👤 Author

**Richard Kweku Addae**
Cloud & DevOps Engineer | AWS Certified Solutions Architect
[LinkedIn](https://linkedin.com/in/richard-addae)
[GitHub](https://github.com/codrich)
