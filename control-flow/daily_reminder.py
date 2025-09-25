task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
timebound = input("Is it time-bound? (yes/no):").lower()

match priority:
    case "high":
        if timebound == 'yes':
            print(f"{priority} is a high priority task that requires immediate attention today!")
        else:
            print(f"{priority} is a low priority task. Consider completing it when you have free time.")
    case "medium":
        if timebound == "yes":
            print(f"{priority} is a high priority task that requires immediate attention today!")
        else:
            print(f"{priority} is a low priority task. Consider completing it when you have free time.")
    case "low":
        if timebound == "yes":
            print(f"{priority} is a high priority task that requires immediate attention today!")
        else:
            print(f"{priority} is a low priority task. Consider completing it when you have free time.")


