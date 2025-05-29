

task = input("Enter your task: ")

Priority = input("Priority (high/medium/low): ").lower()

time_bound = input("Is it time-bound? (yes/no): ").lower()


match Priority:
    case "high":
        message = "is a high priority task"
    case "medium":
        message = "is a medium priority task"
    case "low":
        message = "is a low priority task"

if time_bound == "yes":
    message += " that requires immediate attention today!"
    print(f"Reminder: '{task}' {message}")
elif time_bound == "no":
    message += ". Consider completing it when you have free time."
    print(f"Note: {task} {message}")
