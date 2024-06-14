import django_setup

from managment.models import User, Task

while True:
    a = input("1 - Створити нового користувача\n2 - Створити новий таск\n3 - Призначити таск іншому користувачу\n4 - Змінити статус таску (в процесі, виконано, відкладено)\n5 - Вихід з програми")
    match a:
        case "1":
            User(name = input("Name: ")).save()
        case "2":
            name = input("Name: ")
            description = input("Description: ")
            status = input("Status (в процесі, виконано, відкладено): ")
            user_id = int(input("User ID: "))
            user = User.objects.get(id = user_id)
            Task(name = name, description = description, status = status, user = user).save()
        case "3":
            task_id = input("Task ID: ")
            new_user_id = input("New user ID: ")
            user = User.objects.get(id = new_user_id)
            task = Task.objects.get(id = task_id)
            task.user = user
            task.save()
        case "4":
            task_id = input("Task ID: ")
            new_status = input("Status (в процесі, виконано, відкладено): ")
            task = Task.objects.get(id = task_id)
            task.status = new_status
            task.save()
        case "5":
            break