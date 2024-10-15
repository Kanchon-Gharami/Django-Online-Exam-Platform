# Django Online Exam Platform

A robust web-based platform built using the Django framework to enable remote examinations during the COVID-19 pandemic. It supports multi-user roles such as admins, teachers, and students, automating various aspects of the examination process, including scheduling, MCQ creation, and automatic grading.

## Features

- **User Roles**:
  - **Admin**: Manages the entire platform, including user accounts, roles, exams, and overall settings. Admins have access to all system functionalities, including creating teachers and students, assigning roles, and monitoring the system.
  - **Teacher**: Responsible for creating and managing exams, including adding multiple-choice questions (MCQs), assigning exams to students, and reviewing their results after submission. Teachers can also set time limits for exams and monitor ongoing student activities.
  - **Student**: Can view assigned exams, take exams within the allotted time, and check their results after completion. The platform also tracks the history of all exams the student has taken.

- **Remote Exam Functionality**:
  - Automated grading for MCQs, enabling teachers to focus on monitoring and reviewing student performance rather than manual grading.
  - Scheduled exams with customizable time limits.
  - User-friendly interface tailored for students and teachers to easily navigate through exams and results.

- **Security Features**:
  - **Role-based Access Control (RBAC)**: The platform ensures that each user role (Admin, Teacher, Student) has distinct permissions and access to specific features, ensuring a clear separation of responsibilities.
  - **Exam Integrity**: The platform supports features to maintain exam integrity, such as disallowing multiple submissions or editing answers after submission.
  - **Session Management**: Secure user sessions ensure that students remain logged in for the duration of the exam, preventing unauthorized access or session hijacking.
  - **Data Encryption**: Sensitive data such as passwords and exam results are securely stored and encrypted in the database to protect against data breaches.

## Installation

### Requirements
- Python 3.6+
- Django
- pip
- venv

### Setup Instructions
1. Clone the repository:
    ```bash
    git clone https://github.com/Kanchon-Gharami/Django-Online-Exam-Platform.git
    cd Django-Online-Exam-Platform
    ```
2. Create and activate a virtual environment:
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    ```
3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
4. Apply database migrations:
    ```bash
    python manage.py migrate
    ```

### Running the Application
Start the server:
```bash
python manage.py runserver
