import random
import os
import json 
from faker import Faker

fake = Faker()

class CVGenerator:
    def __init__(self):
        self.levels = ["Intern", "Fresher", "Junior", "Senior"]
        self.positions = ["AI Engineer", "Data Engineer", "Back-end Developer", "ML Engineer", "DevOps Engineer"]
        self.tools_pool = ["Docker", "Git", "Airflow", "Github Actions", "Kubernetes", "Jenkins"]
        self.languages_pool = ["Python", "Typescript", "Go", "Java", "Rust"]
        self.frameworks_pool = ["FastAPI", "NextJS", "Pytorch", "Numpy", "Pandas", "Tensorflow", "Selenium", "Scikit-learn"]
        self.databases_pool = ["PineconeDB", "Faiss", "MongoDB", "GCP", "ElasticSearch", "PostgreSQL", "Neo4j", "Firebase"]
        self.language_levels = ["A1", "A2", "B1", "B2", "C1", "C2"]
        self.project_templates = self._load_project_templates()
        self.save_dir = os.path.join(os.getcwd(), "..", "data")
        self.degree_levels = ["Bachelor", "Master", "PhD"]
        self.majors = ["Computer Science", "Data Science", "Artificial Intelligence", 
                      "Software Engineering", "Computer Engineering", "Information Technology"]
        self.institutions = [
            "International University-VNU, HCMC",
            "University of Science, VNU-HCM",
            "University of Technology, VNU-HCM",
            "Hanoi University of Science and Technology",
            "FPT University",
            "RMIT University Vietnam",
            "Posts and Telecommunications Institute of Technology",
            "Ton Duc Thang University",
            "University of Information Technology, VNU-HCM",
        ]

        os.makedirs(self.save_dir, exist_ok=True)
    
    def _load_project_templates(self):
        return [
            # AI/ML Projects
            {
                "Name": "AI-Powered Fashion Recommender",
                "Role": "AI Engineer",
                "Details": [
                    "Developed recommendation engine using collaborative filtering and content-based approaches",
                    "Implemented computer vision model for style analysis using PyTorch",
                    "Built Flask API for serving recommendations",
                    "Optimized model performance using ONNX runtime"
                ],
                "Tech": ["Python", "PyTorch", "Flask", "ONNX", "Docker"]
            },
            {
                "Name": "Medical Image Segmentation System",
                "Role": "ML Engineer",
                "Details": [
                    "Developed U-Net architecture for medical image segmentation",
                    "Preprocessed DICOM images using NumPy and OpenCV",
                    "Achieved 92% dice score on test dataset",
                    "Deployed model as microservice using FastAPI"
                ],
                "Tech": ["Python", "TensorFlow", "OpenCV", "FastAPI", "Kubernetes"]
            },
            
            # Backend Projects
            {
                "Name": "E-commerce Platform API",
                "Role": "Back-end Developer",
                "Details": [
                    "Designed RESTful API for e-commerce platform using Django REST Framework",
                    "Implemented JWT authentication and role-based access control",
                    "Optimized database queries reducing response time by 40%",
                    "Integrated Stripe payment processing system"
                ],
                "Tech": ["Python", "Django", "PostgreSQL", "Redis", "Celery"]
            },
            {
                "Name": "Real-time Chat Application",
                "Role": "Back-end Developer",
                "Details": [
                    "Built WebSocket-based chat service using Socket.io",
                    "Implemented message persistence with MongoDB",
                    "Added end-to-end encryption using AES-256",
                    "Deployed on AWS with auto-scaling"
                ],
                "Tech": ["Node.js", "Socket.io", "MongoDB", "AWS", "Docker"]
            },
            
            # Data Engineering Projects
            {
                "Name": "Data Lake for IoT Devices",
                "Role": "Data Engineer",
                "Details": [
                    "Designed data ingestion pipeline processing 10M+ events daily",
                    "Implemented stream processing using Apache Flink",
                    "Built data quality monitoring with Great Expectations",
                    "Optimized Parquet storage for efficient querying"
                ],
                "Tech": ["Python", "Apache Flink", "Parquet", "AWS S3", "Airflow"]
            },
            {
                "Name": "Customer 360 Data Warehouse",
                "Role": "Data Engineer",
                "Details": [
                    "Built dimensional data model using Kimball methodology",
                    "Implemented slowly changing dimensions Type 2",
                    "Created data marts for different business units",
                    "Reduced report generation time from hours to minutes"
                ],
                "Tech": ["SQL", "Snowflake", "dbt", "Python", "Tableau"]
            },
            
            # DevOps Projects
            {
                "Name": "Kubernetes Cluster Automation",
                "Role": "DevOps Engineer",
                "Details": [
                    "Automated EKS cluster provisioning using Terraform",
                    "Implemented GitOps workflow with ArgoCD",
                    "Set up monitoring with Prometheus and Grafana",
                    "Reduced deployment time by 70%"
                ],
                "Tech": ["Terraform", "AWS EKS", "ArgoCD", "Prometheus", "Helm"]
            },
            {
                "Name": "CI/CD Pipeline Optimization",
                "Role": "DevOps Engineer",
                "Details": [
                    "Migrated from Jenkins to GitHub Actions",
                    "Implemented parallel test execution",
                    "Reduced pipeline duration from 45 to 12 minutes",
                    "Added security scanning with Trivy and OWASP ZAP"
                ],
                "Tech": ["GitHub Actions", "Docker", "Kubernetes", "Trivy", "OWASP ZAP"]
            },
            
            # Full Stack Projects
            {
                "Name": "Property Management System",
                "Role": "Full-stack Developer",
                "Details": [
                    "Developed React frontend with TypeScript",
                    "Built backend services using NestJS",
                    "Implemented PDF generation for contracts",
                    "Added role-based access control"
                ],
                "Tech": ["React", "TypeScript", "NestJS", "PostgreSQL", "Docker"]
            },
            {
                "Name": "Healthcare Appointment System",
                "Role": "Full-stack Developer",
                "Details": [
                    "Created patient portal with Next.js",
                    "Implemented calendar scheduling system",
                    "Added SMS/email notifications",
                    "Ensured HIPAA compliance for data security"
                ],
                "Tech": ["Next.js", "Node.js", "Twilio", "MongoDB", "AWS"]
            },
            
            # Specialized Projects
            {
                "Name": "Blockchain Supply Chain Tracker",
                "Role": "Blockchain Developer",
                "Details": [
                    "Developed smart contracts for supply chain tracking",
                    "Built React frontend for supply chain visualization",
                    "Integrated with IoT devices for real-time tracking",
                    "Implemented zero-knowledge proofs for sensitive data"
                ],
                "Tech": ["Solidity", "React", "Hardhat", "ZK-SNARKs", "IPFS"]
            },
            {
                "Name": "AR Furniture Visualization",
                "Role": "AR/VR Developer",
                "Details": [
                    "Developed ARKit/ARCore application for furniture visualization",
                    "Implemented 3D model rendering with Unity",
                    "Added physics for realistic placement",
                    "Integrated with e-commerce backend"
                ],
                "Tech": ["Unity", "C#", "ARKit", "ARCore", "Firebase"]
            },
            
            # Intern/Fresher Projects
            {
                "Name": "Campus Event Management System",
                "Role": "Full-stack Developer",
                "Details": [
                    "Built student portal for event registration",
                    "Implemented admin dashboard for event management",
                    "Added notification system",
                    "Deployed on university servers"
                ],
                "Tech": ["PHP", "MySQL", "JavaScript", "Bootstrap"]
            },
            {
                "Name": "Personal Finance Tracker",
                "Role": "Mobile Developer",
                "Details": [
                    "Developed Flutter app for expense tracking",
                    "Implemented data visualization charts",
                    "Added budget alerts",
                    "Integrated with bank APIs"
                ],
                "Tech": ["Flutter", "Dart", "Firebase", "REST API"]
            }
        ]
    
    def _save_cv_to_file(self, cv_data, filename=None):
        """
        Save a CV dictionary to a JSON file.
        
        Parameters:
        - cv_data (dict): The CV data to save.
        - filename (str): Optional. If None, uses the person's name.
        """
        if filename is None:
            full_name = cv_data.get("FullName", "cv").replace(" ", "_")
            filename = f"{full_name}.json"
        
        filepath = os.path.join(self.save_dir, filename)
        
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(cv_data, f, indent=2, ensure_ascii=False)
        
        print(f"CV saved to {filepath}")
    
    def _random_project_instance(self, template):
        start_year = random.randint(2023, 2024)
        end_year = random.randint(start_year, 2025)
        start_month = fake.month_name()
        end_month = fake.month_name()
        duration = f"{start_month} {start_year} – {end_month} {end_year}"
        return {
            "Name": template["Name"],
            "Role": template["Role"],
            "Duration": duration,
            "Details": template["Details"]
        }
    
    def _generate_education(self):
        degree_level = random.choice(self.degree_levels)
        major = random.choice(self.majors)
        institution = random.choice(self.institutions)
        
        if degree_level == "Bachelor":
            duration = f"{random.randint(2018, 2020)}-{random.randint(2022, 2024)}"
            gpa = round(random.uniform(2.5, 4.0), 2)
            
        elif degree_level == "Master":
            duration = f"{random.randint(2020, 2022)}-{random.randint(2022, 2024)}"
            gpa = round(random.uniform(3.0, 4.0), 2)
        else:  # PhD
            duration = f"{random.randint(2016, 2018)}-{random.randint(2022, 2024)}"
            gpa = round(random.uniform(3.5, 4.0), 2)

        
        education = {
            "Degree": f"{degree_level} of Science in {major}",
            "Institution": institution,
            "Duration": duration,
            "GPA": gpa
        }
        
        
        return education
    
    def generate_cv(self):
        full_name = fake.name()
        email = fake.email()
        phone = fake.phone_number()
        github = f"github.com/{fake.user_name()}"
        linkedin = f"linkedin.com/in/{fake.user_name()}"

        level = random.choice(self.levels)
        position = random.choice(self.positions)
        profile = f"I am a {random.choice(['motivated', 'passionate', 'experienced', 'highly skilled'])} {position} focusing on {random.choice(['scalable AI systems', 'robust software solutions', 'data pipelines', 'cloud infrastructure', 'machine learning models'])}."

        selected_projects = [self._random_project_instance(p) for p in random.sample(self.project_templates, 2)]

        cv_data = {
            "Level": level,
            "FullName": full_name,
            "Contact": {
                "Phone": phone,
                "Email": email,
                "GitHub": github,
                "LinkedIn": linkedin
            },
            "Profile": profile,
            "Education": self._generate_education(),
            "TechnicalSkills": {
                "Tools": random.sample(self.tools_pool, k=random.randint(2, 4)),
                "ProgrammingLanguages": random.sample(self.languages_pool, k=random.randint(1, 3)),
                "FrameworksLibraries": random.sample(self.frameworks_pool, k=random.randint(3, 5)),
                "DatabasesCloudServices": random.sample(self.databases_pool, k=random.randint(2, 4)),
            },
            "Languages": {
                "English": random.choice(self.language_levels),
                "German": random.choice(self.language_levels) if random.random() > 0.4 else "A1",
                "Japanese": random.choice(self.language_levels) if random.random() > 0.4 else "A1"
            },

            "Projects": selected_projects,
            "Leadership": [
                {
                    "Organization": random.choice(["GDSC", "IEEE", "ACM", "Toastmasters", "Code Club"]),
                    "Role": random.choice(["BackEnd Specialist", "AI Lead", "Technical Mentor", "Team Lead", "Chapter President"]),
                    "Duration": f"{random.randint(2020, 2023)}–{random.randint(2023, 2024)}",
                    "Activities": [random.choice([
                        "Hosted workshops and guided technical best practices.",
                        "Led a team of developers to build community projects.",
                        "Organized hackathons and coding competitions.",
                        "Mentored junior members in their technical growth."
                    ])]
                } if random.random() > 0.3 else None
            ],
            "References": [
                {
                    "Name": fake.name(),
                    "Institution": random.choice(self.institutions),
                    "Email": fake.email()
                } if random.random() > 0.5 else None
            ]
        }
        
        # Remove None values from lists
        cv_data["Leadership"] = [item for item in cv_data["Leadership"] if item is not None]
        cv_data["References"] = [item for item in cv_data["References"] if item is not None]
        
        return cv_data


if __name__ == "__main__":
    generator = CVGenerator()
    num_cvs = 10

    for _ in range(num_cvs):
        cv_data = generator.generate_cv()
        generator._save_cv_to_file(cv_data)