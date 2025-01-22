from user import User
from projects import Project
from task import Task
from advice_provider import AdviceProvider  # Changed here
from document_manager import Document
from security_manager import Security
from progress_analyzer import ProgressAnalyzer
from alert_manager import AlertManager
from error_log import ErrorLog




def main():
    # Create and save a new user
    user = User(user_id=None, username="janedoe", email="janedoe@example.com", role="Employee", preferences="{}", created_at=datetime.now(), last_login=datetime.now(), is_active=True)
    user.save()

    # Create and save a project
    project = Project(project_id=None, project_name="Project Y", description="A critical project", start_date=datetime.now(), end_date=datetime.now(), owner_id=user.userID, status="Ongoing", created_at=datetime.now())
    project.save()

    # Create a task
    task = Task(task_id=None, project_id=project.projectID, assigned_to=user.userID, task_name="Design", description="Design UI for the project", due_date=datetime.now(), status="In Progress", progress_percentage=50, created_at=datetime.now())
    task.save()

    # Provide advice using the modified class
    advice = AdviceProvider(user_id=user.userID, context="UI Design", advice_text="Follow the company design guidelines", created_at=datetime.now())
    advice.save()

    # Create and save an alert
    alert_manager = AlertManager(user_id=user.userID, message="Task completion due soon", is_read=False, created_at=datetime.now())
    alert_manager.save()

    # Analyze project progress
    progress_analyzer = ProgressAnalyzer()
    print(progress_analyzer.analyze_progress(project.projectID))

        # Retrieve and display advice
    retrieved_advice = AdviceProvider.get_advice_by_user(user.userID)
    for adv in retrieved_advice:
        print(f"Advice: {adv.adviceText}, Context: {adv.context}")

if __name__ == "__main__":
    main()
