# Generate Human Resoure Dataset - Benefits
# Source code: Chatgpt with modifications

import pandas as pd
import numpy as np
import random

# Set random seed for reproducibility
np.random.seed(42)

# Create 500 rows
num_rows = 500

# Sample data pools

departments = ["Engineering", "Marketing", "Sales", "HR", "Finance", "IT"]
work_arrangements = ["On-site", "Hybrid", "WFH"]
genders = ["Male", "Female"]
retirement_plans = ["401(k)", "Roth", "Safe Harbor", "Simple", "None"]
health_insurance = ["Standard", "Premium", "None"]
dental_insurance = ["Standard", "Premium", "None"]
life_insurance = ["Standard", "None"]
marital_statuses = ["Single", "Married", "Divorced"]

# Job titles by department
job_titles = {
    "Engineering": ["Software Engineer", "Lead Engineer", "DevOps Engineer"],
    "Marketing": ["Marketing Manager", "Brand Strategist", "Content Specialist"],
    "Sales": ["Sales Associate", "Account Executive", "Sales Manager"],
    "HR": ["HR Manager", "Recruiter", "HR Coordinator"],
    "Finance": ["Financial Analyst", "Finance Manager", "Accountant"],
    "IT": ["Systems Administrator", "IT Support", "Network Engineer"]
}

# Generate the dataset
data = []

for i in range(num_rows):
    age = np.random.randint(20, 70)
    if age >= 20 and age <=30:
        age_grp = '20 - 30'
    elif age >= 31 and age <= 40:
        age_grp = '31 - 40'
    elif age >= 41 and age <= 50:
        age_grp = '41 - 50'
    elif age >= 51 and age <= 61:
        age_grp = '51 - 60'
    elif age >=61 and age <=70:
        age_grp = '61 - 70'
    else:
        age_grp = 'Unknown'
            
    department = random.choice(departments)
    gender = random.choice(genders)
    salary = np.random.randint(50000, 150000)
    plan = random.choice(retirement_plans)
    contribution = np.random.choice([0, 4, 5, 6, 7, 8, 9, 10]) if plan != "None" else 0
    savings = round(salary * (contribution / 100) * np.random.uniform(1, 10), 2) if contribution > 0 else 0
    data.append([
        f"E{str(i+1).zfill(5)}",  # Employee ID
        #np.random.randint(22, 61),
        age,
        age_grp,
        random.choice(genders),
        random.choice(work_arrangements),
        department,
        random.choice(job_titles[department]),
        salary,
        plan,
        contribution,
        savings,
        random.choice(health_insurance),
        random.choice(dental_insurance),
        random.choice(life_insurance),
        np.random.randint(12, 26),  # PTO days
        random.choice(marital_statuses)
    ])

# Define column names
columns = [
    "Employee ID", "Age", "Age_Group","Gender", "Work Arrangement", "Department", "Job Title",
    "Salary ($)", "Retirement Plan", "Contribution (%)", "Retirement Savings ($)",
    "Health Insurance", "Dental Insurance", "Life Insurance", "PTO Allocated (Days)", "Marital Status"
]

# Create DataFrame and export to CSV
df = pd.DataFrame(data, columns=columns)
df.to_csv("mock_hr_dataset_500.csv", index=False)

print("Dataset saved as mock_hr_dataset_500.csv")
