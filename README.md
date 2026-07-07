# DevOps Insight

## Overview
DevOps Insight is a tool designed to provide real-time insights into CI/CD pipeline performance, helping DevOps teams optimize their workflows.

## Features
- Dashboard for pipeline performance metrics
- Integration with popular CI/CD tools like Jenkins and GitHub Actions
- Alerts and notifications for performance anomalies
- Collaboration features for cross-team visibility and feedback

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/finggu-devops-insight.git
   cd finggu-devops-insight
   ```
2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Set up environment variables for database and email configuration.
5. Run the migrations:
   ```bash
   python manage.py migrate
   ```
6. Start the development server:
   ```bash
   python manage.py runserver
   ```

## Usage
Access the dashboard at `http://127.0.0.1:8000/`.