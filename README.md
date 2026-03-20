# 🚀 Mertmart Cloud Platform – Flask App on AWS ECS Fargate

![Architecture](./architecture.png)

---

## 🧠 Overview

This project is a **production-style cloud application** built for **Mertmart Group**, showcasing real-world implementation of:

* Cloud Infrastructure (AWS)
* DevOps & CI/CD Automation
* Containerized Deployments
* Cloud Security Best Practices

💡 Unlike typical demo projects, this system is designed to **support actual business workflows**, making it a practical example of cloud engineering in action.

---

## 🏗️ Architecture Diagram

![Image](https://miro.medium.com/1%2AjcmnWZ5X17ABsRgJXCaiUA.png)

![Image](https://d2908q01vomqb2.cloudfront.net/7719a1c782a1ba91c031a682a0a2f8658209adbf/2022/03/27/1-ArchitectureDiagram.png)

![Image](https://media2.dev.to/dynamic/image/width%3D1000%2Cheight%3D500%2Cfit%3Dcover%2Cgravity%3Dauto%2Cformat%3Dauto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fddvi9pya9qo8o8zs6a8o.png)

![Image](https://miro.medium.com/v2/resize%3Afit%3A1400/1%2AQbdXPsgP0lGNifMcQzgANQ.jpeg)

### 🔹 Architecture Flow

1. User request hits **Application Load Balancer (ALB)**
2. Traffic routed to **ECS Fargate service**
3. Containers pull images from **Amazon ECR**
4. Logs and metrics sent to **CloudWatch**
5. CI/CD pipeline updates application automatically

---

## ⚙️ Core Features

* 🚀 Containerized Flask application (Docker)
* ☁️ Serverless compute using ECS Fargate
* 🔁 Automated CI/CD with GitHub Actions
* ⚖️ Load-balanced architecture for scalability
* 🔐 IAM-based security and access control
* 📊 Monitoring and logging with CloudWatch

---

## 🧩 Real-World Business Impact (Mertmart)

This system is part of **Mertmart Group’s cloud platform**, enabling:

* Internal business operations support
* Foundation for inventory and order management
* Scalable infrastructure for future growth

💥 Demonstrates how small businesses can adopt **enterprise-grade cloud solutions**

---

## 🔁 CI/CD Pipeline

```yaml id="m6t2wr"
name: Deploy to AWS ECS

on:
  push:
    branches: [ main ]

jobs:
  deploy:
    runs-on: ubuntu-latest
```

### Pipeline Flow:

* Push code → GitHub
* Build Docker image
* Push to Amazon ECR
* Deploy to ECS Fargate

---

## 🚀 Deployment Steps

```bash id="65myrg"
# Build Docker image
docker build -t mertmart-app .

# Tag image
docker tag mertmart-app:latest <ECR-REPO-URI>

# Push to ECR
docker push <ECR-REPO-URI>
```

---

## 🔐 Security Implementation

* IAM roles with **least privilege access**
* Secure container registry (ECR)
* Network isolation via VPC & Security Groups
* Environment variable management for secrets
* Centralized logging (CloudWatch)

---

## 💻 Run Locally

```bash id="2m0z11"
# Install dependencies
pip install -r requirements.txt

# Run app
python app.py
```

Then open:
👉 [http://localhost:5000](http://localhost:5000)

---

## 📂 Project Structure

```id="mjla00"
├── app.py
├── Dockerfile
├── requirements.txt
```

---

## 📸 Screenshots

![Image](https://www.researchgate.net/publication/301443552/figure/fig3/AS%3A724329746665474%401549705077433/Screenshot-of-Amazon-EC2-Management-Console-showing-the-running-instances.ppm)

![Image](https://d2908q01vomqb2.cloudfront.net/972a67c48192728a34979d9a35164c1295401b71/2020/10/15/Sampledashboard.png)

![Image](https://media.amazonwebservices.com/blog/2016/alb_add_rule_1.png)

![Image](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2019/10/06/2019-10-06_15-50-35.png)

💡 Replace these with your actual screenshots:

* ECS running service
* CloudWatch logs
* ALB DNS working
* App in browser

---

## 🛠️ Tech Stack

* Python (Flask)
* Docker
* AWS ECS Fargate
* Amazon ECR
* GitHub Actions
* AWS CloudWatch
* Terraform (Infrastructure provisioning)

---

## 📊 Skills Demonstrated

* Cloud Architecture (AWS)
* Infrastructure as Code (Terraform)
* DevOps & CI/CD
* Containerization
* Cloud Security
* Monitoring & Observability

---

## 📈 Future Enhancements

* 🔹 Database integration (RDS / DynamoDB)
* 🔹 Authentication system (JWT / AWS Cognito)
* 🔹 Auto-scaling policies
* 🔹 Advanced monitoring dashboards
* 🔹 Basic anomaly/fraud detection

---

## 👤 Author

**Richard Kweku Addae**
Cloud & DevOps Engineer | AWS Certified Solutions Architect

🔗 [https://linkedin.com/in/richard-addae](https://linkedin.com/in/richard-addae)
🔗 [https://github.com/codrich](https://github.com/codrich)

---
