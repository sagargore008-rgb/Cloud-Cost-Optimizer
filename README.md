# ☁️ Cloud Cost Optimizer & Monitoring Platform

A cloud-based cost optimization and monitoring platform that analyzes AWS spending, identifies unusual cost patterns, forecasts future expenses, and provides actionable cost optimization recommendations.

This project combines **AWS, Terraform, Docker, Kubernetes, GitHub Actions, Python/FastAPI, React, and PostgreSQL** to demonstrate an end-to-end Cloud and DevOps workflow.

---

## 🚀 Project Overview

Managing cloud infrastructure can become expensive when resources are not properly monitored or optimized.

The **Cloud Cost Optimizer** provides a centralized dashboard to:

- 💰 View current AWS spending
- 📊 Analyze costs by AWS service
- 📈 Track daily cost history
- 🚨 Detect unusual cost patterns
- 🔮 Forecast future monthly spending
- 💡 Generate cost optimization recommendations
- 🗄️ Store historical cost data in PostgreSQL
- 🐳 Containerize applications using Docker
- ☸️ Deploy applications using Kubernetes/Amazon EKS
- 🏗️ Provision infrastructure using Terraform
- 🔄 Automate CI/CD using GitHub Actions

---

# 🏗️ Architecture

                         ┌─────────────────────┐
                         │      Developer      │
                         │       GitHub        │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │   GitHub Actions    │
                         │      CI / CD        │
                         └──────────┬──────────┘
                                    │
                   ┌────────────────┴────────────────┐
                   │                                 │
                   ▼                                 ▼
          ┌─────────────────┐              ┌─────────────────┐
          │ Docker Images   │              │    Terraform    │
          │ Frontend        │              │ Infrastructure  │
          │ Backend         │              │       as Code   │
          └────────┬────────┘              └────────┬────────┘
                   │                                │
                   └────────────────┬───────────────┘
                                    ▼
                           ┌──────────────────┐
                           │     AWS EKS      │
                           │    Kubernetes    │
                           └────────┬─────────┘
                                    │
                   ┌────────────────┼────────────────┐
                   │                │                │
                   ▼                ▼                ▼
           ┌──────────────┐ ┌──────────────┐ ┌──────────────┐
           │   Frontend   │ │   Backend    │ │  PostgreSQL  │
           │ React + Nginx│ │   FastAPI    │ │   Database   │
           └──────┬───────┘ └──────┬───────┘ └──────┬───────┘
                  │                │                │
                  │                ▼                │
                  │       ┌─────────────────┐       │
                  │       │ AWS Cost        │       │
                  │       │ Explorer        │       │
                  │       └─────────────────┘       │
                  │                                 │
                  └──────────────┬──────────────────┘
                                 ▼
                         Cost Analytics

✨ Key Features
1. 💰 Current AWS Cost

The application integrates with AWS Cost Explorer to retrieve the current month's AWS expenditure.
```text
Example:

Current Month Cost
       ↓
     $1.50

The backend retrieves cost information directly from AWS.

2. 📊 Cost by AWS Service

The platform analyzes AWS spending and groups costs by service.
```text
Example:

Service                  Cost
--------------------------------
Amazon EC2               $0.80
Amazon EKS               $0.40
Elastic Load Balancer    $0.20
Amazon ECR               $0.10
Other                    $0.00

This helps identify which AWS services contribute the most to cloud expenditure.

3. 📈 Daily Cost History

The application retrieves daily AWS spending and stores historical records in PostgreSQL.
```text
Example:

Date          Cost
---------------------
2026-09-07    $0.12
2026-09-08    $0.18
2026-09-09    $0.21
2026-09-10    $0.25
2026-09-11    $0.19

The frontend displays the historical data using charts.

🚨 4. Cost Anomaly Detection

The platform analyzes historical cost data to identify unusual spending patterns.

The current implementation uses statistical analysis based on:

Mean Cost + (2 × Standard Deviation)

If a daily cost exceeds the calculated threshold, it is identified as a potential anomaly.

Example:

Normal Daily Cost
       ↓
     $0.20

Detected Cost
       ↓
     $0.65

Status
       ↓
⚠️ Unusual spending detected
🔮 5. Cost Forecasting

The application estimates future monthly AWS spending based on the current average daily cost.

Conceptually:

Average Daily Cost
        ×
Number of Days in Month
        =
Forecasted Monthly Cost

Example:

Average Daily Cost: $0.25

Estimated Monthly Cost: $7.50

This helps users understand potential future cloud expenditure.

💡 6. Cost Optimization Recommendations

The platform analyzes AWS service costs and generates recommendations based on spending patterns.

Example:

⚠️ EC2 is contributing significantly to total cost.
Review instance utilization and instance size.

⚠️ EBS costs detected.
Review unused volumes and snapshots.

⚠️ Load Balancer costs detected.
Review whether the Load Balancer is still required.

The objective is to help identify potential cloud cost-saving opportunities.

# 🗄️ 7. PostgreSQL Cost Storage

Historical AWS cost information is stored in **PostgreSQL** to maintain cost records and support historical analysis, anomaly detection, and forecasting.

### Database Structure

```text
PostgreSQL
    │
    └── cloud_cost_optimizer
          │
          └── cost_records
                ├── id
                ├── date
                ├── service
                └── cost
This allows the application to maintain historical cost information.

🛠️ Technology Stack
☁️ Cloud
AWS
AWS Cost Explorer
Amazon EKS
Amazon EC2
Amazon ECR
Application Load Balancer
Amazon VPC
🏗️ Infrastructure as Code
Terraform
🐳 Containers
Docker
Docker Compose
☸️ Container Orchestration
Kubernetes
Amazon EKS
kubectl
⚙️ Backend
Python
FastAPI
Uvicorn
SQLAlchemy
🎨 Frontend
React
Vite
JavaScript
Recharts
HTML
CSS
Nginx
🗄️ Database
PostgreSQL
🔄 CI/CD
GitHub Actions
📦 Version Control
Git
GitHub

🔄 Application Workflow
                    User
                     │
                     ▼
              React Dashboard
                     │
                     ▼
              FastAPI Backend
                     │
          ┌──────────┴──────────┐
          │                     │
          ▼                     ▼
  AWS Cost Explorer       PostgreSQL
          │                     │
          ▼                     ▼
    AWS Cost Data       Historical Data
          │                     │
          └──────────┬──────────┘
                     ▼
              Cost Analysis
                     │
        ┌────────────┼────────────┐
        ▼            ▼            ▼
    Anomaly      Forecast    Optimization
    Detection    Analysis    Recommendations
        │            │            │
        └────────────┼────────────┘
                     ▼
              React Dashboard

🐳 Docker

The frontend and backend applications are containerized using Docker.

Backend

The backend Docker image contains:

Python
FastAPI
Uvicorn
Application Dependencies
Frontend

The React application is built for production and served using Nginx.

🐳 Docker Compose

The project can also be run locally using Docker Compose.

Architecture:

Frontend
    │
    ▼
Backend
    │
    ▼
PostgreSQL

Start the application:

docker compose up --build

Stop the application:

docker compose down

☸️ Kubernetes Deployment

The application was designed to run on Kubernetes/Amazon EKS.

Kubernetes is used for:

Container orchestration
Pod management
Deployments
Service networking
Replica management
Scaling
Fault tolerance

Useful commands:

kubectl get pods
kubectl get deployments
kubectl get services
kubectl get nodes
☁️ AWS Infrastructure

Terraform was used to provision the AWS infrastructure.

Main AWS components include:

# ☁️ AWS VPC Infrastructure

The project uses **Amazon Virtual Private Cloud (VPC)** to create an isolated and secure network environment for the cloud infrastructure.

### VPC Architecture


                       AWS VPC
                    10.0.0.0/16
                         │
              ┌──────────┴──────────┐
              │                     │
              ▼                     ▼
       ┌──────────────┐      ┌──────────────┐
       │ Public       │      │ Public       │
       │ Subnet 1     │      │ Subnet 2     │
       │ 10.0.1.0/24  │      │ 10.0.2.0/24  │
       └──────┬───────┘      └──────┬───────┘
              │                     │
              └──────────┬──────────┘
                         │
                         ▼
                 Internet Gateway
                         │
                         ▼
                      Internet

AWS services used:

Amazon VPC
Amazon EKS
Amazon EC2
Amazon ECR
AWS Cost Explorer
Elastic Load Balancing

🏗️ Terraform

Terraform is used as Infrastructure as Code (IaC).

Typical workflow:

terraform init
terraform validate
terraform plan
terraform apply

To destroy Terraform-managed infrastructure:

terraform destroy

Terraform provides reproducible and version-controlled cloud infrastructure.

🔐 Security

The project follows the principle of least privilege for AWS permissions.

The backend requires AWS Cost Explorer permissions to retrieve cost information.

Example permission:

ce:GetCostAndUsage
🔒 Secrets

Never commit sensitive information to GitHub.

The following should remain private:

.env
AWS credentials
Access keys
Secret keys
Terraform state files
Database passwords

These files should be excluded using .gitignore.

🔄 CI/CD Pipeline

# 🔄 CI/CD Workflow

The project uses **GitHub Actions** to automate the application build, testing, Docker image creation, and deployment process.

### CI/CD Pipeline

```text
┌──────────────────────┐
│      Developer       │
│                      │
│   Code Changes       │
└──────────┬───────────┘
           │
           │ git push
           ▼
┌──────────────────────┐
│   GitHub Repository  │
│                      │
│  Cloud-Cost-Optimizer│
└──────────┬───────────┘
           │
           │ Trigger
           ▼
┌──────────────────────┐
│    GitHub Actions    │
│       Workflow       │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│   Checkout Code      │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│   Build Application  │
│                      │
│ Frontend + Backend   │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│       Testing        │
│                      │
│  Build / Validation  │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│    Docker Build      │
│                      │
│ Frontend + Backend   │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│    Docker Images     │
│                      │
│   Build & Tag        │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│   Container Registry │
│      Amazon ECR      │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│    Amazon EKS        │
│     Kubernetes       │
│                      │
│  Deploy Application  │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│   Running Application│
│                      │
│  Frontend + Backend  │
└──────────────────────┘
This demonstrates Continuous Integration and Continuous Deployment practices.

🧪 Local Development
Backend

Navigate to the backend directory:

cd backend

Create a Python virtual environment:

python -m venv venv

Activate the environment on Windows PowerShell:

.\venv\Scripts\Activate.ps1

Install dependencies:

pip install -r requirements.txt

Run the FastAPI server:

uvicorn app.main:app --reload

Backend:

http://localhost:8000

API documentation:

http://localhost:8000/docs
💻 Frontend Development

Navigate to the frontend:

cd frontend

Install dependencies:

npm install

Start the development server:

npm run dev
🗄️ Database Configuration

The application uses PostgreSQL.

Example configuration:

DATABASE_URL=postgresql://USERNAME:PASSWORD@localhost:5432/cloud_cost_optimizer

Do not commit .env to GitHub.

# 📊 Dashboard

The dashboard provides a centralized view of AWS cloud expenditure.

### Main Dashboard Sections

```text
┌─────────────────────────────────────────┐
│         Cloud Cost Optimizer            │
├─────────────────────────────────────────┤
│                                         │
│   Current Cost          Forecast        │
│                                         │
├─────────────────────────────────────────┤
│                                         │
│        Cost by AWS Service              │
│                                         │
├─────────────────────────────────────────┤
│                                         │
│          Daily Cost Trend               │
│                                         │
├─────────────────────────────────────────┤
│                                         │
│          Anomaly Detection              │
│                                         │
├─────────────────────────────────────────┤
│                                         │
│   Optimization Recommendations          │
│                                         │
└─────────────────────────────────────────┘
🧠 DevOps Concepts Demonstrated
Cloud Computing
AWS
IAM
VPC
EC2
EKS
ECR
Cost Explorer
Load Balancing
Infrastructure as Code
Terraform
Infrastructure provisioning
Resource lifecycle management
Containerization
Docker
Dockerfiles
Docker Compose
Container networking
Kubernetes
Pods
Deployments
Services
Replica management
YAML configuration
Scaling
Fault tolerance
CI/CD
GitHub Actions
Automated builds
Docker image creation
Deployment automation
Backend
Python
FastAPI
REST APIs
SQLAlchemy
Frontend
React
Vite
JavaScript
Recharts
Nginx
Database
PostgreSQL
SQLAlchemy
Historical cost storage
🎯 Project Objectives

The main objectives are:

Monitor AWS cloud expenditure.
Analyze costs by AWS service.
Maintain historical cost records.
Detect unusual spending patterns.
Forecast future cloud spending.
Provide cost optimization recommendations.
Containerize applications using Docker.
Deploy applications using Kubernetes/Amazon EKS.
Provision infrastructure using Terraform.
Implement CI/CD using GitHub Actions.
📚 Key Learning Outcomes

Through this project, I gained practical experience with:

AWS cloud infrastructure
AWS Cost Explorer
IAM permissions
Terraform Infrastructure as Code
Docker containerization
Kubernetes
Amazon EKS
Amazon ECR
FastAPI REST APIs
PostgreSQL
React
Nginx
GitHub Actions
Cloud cost analysis
Anomaly detection
Cost forecasting
Cloud optimization
🔮 Future Improvements

Potential future enhancements:

Machine-learning-based cost forecasting
Advanced anomaly detection
AWS Trusted Advisor integration
Automated cost alerts
Multi-account AWS support
Multi-region cost analysis
Budget threshold notifications
Historical cost comparison
CSV/PDF cost reports
Authentication
Role-based access control
💼 Resume Project Description
Cloud Cost Optimizer & Monitoring Platform

Technologies: AWS, Terraform, Kubernetes, Docker, GitHub Actions, Python, FastAPI, React, PostgreSQL

Developed a cloud cost optimization platform using Python/FastAPI and React to analyze AWS expenditure.
Integrated AWS Cost Explorer to retrieve current costs, service-level spending, and daily cost history.
Implemented statistical anomaly detection and monthly cost forecasting to identify unusual spending and estimate future expenses.
Developed service-based optimization recommendations to identify potential cloud cost-saving opportunities.
Containerized frontend and backend applications using Docker and deployed workloads on Kubernetes/Amazon EKS.
Provisioned AWS infrastructure using Terraform and implemented CI/CD workflows using GitHub Actions.
Used PostgreSQL with SQLAlchemy to persist historical AWS cost data.
⭐ Project Highlights
                     AWS
                      │
        ┌─────────────┼─────────────┐
        │             │             │
   Cost Explorer     EKS           EC2
        │             │
        │            ECR
        │             │
        └──────┬──────┘
               │
           Terraform
               │
               ▼
          Kubernetes
               │
               ▼
             Docker
               │
       ┌───────┴────────┐
       ▼                ▼
    FastAPI           React
       │                │
       ▼                ▼
 PostgreSQL          Nginx
       │
       ▼
 Cost Analytics
       │
 ┌─────┼─────────┐
 ▼     ▼         ▼
Anomaly Forecast Optimization
Detection        Recommendations
👨‍💻 Author

Sagar Gore

B.Tech – Computer Engineering

Areas of Interest
Cloud Engineering
DevOps
AWS
Kubernetes
Terraform
Docker
CI/CD
Infrastructure as Code
