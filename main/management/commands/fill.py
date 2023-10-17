from django.core.management import BaseCommand

from main.models import Student


class Command(BaseCommand):

    def handle(self, *args, **options):
        student_list = [
            {
                "first_nami": "Savva",
                "last_name": "Shishkin",
                "avatar": "students/Снимок_экрана_от_2023-10-12_19-01-44.png",
                "is_active": True
            },
            {
                "first_nami": "Kristina",
                "last_name": "Shishkina",
                "avatar": "students/Снимок_экрана_от_2023-10-16_22-31-23.png",
                "is_active": True
            },
            {
                "first_nami": "Savva",
                "last_name": "Shishkin",
                "avatar": "students/Снимок_экрана_от_2023-10-12_19-01-44_n4jQJlj.png",
                "is_active": True
            }
        ]
        students_for_create = []
        for student_item in student_list:
            students_for_create.append(
                Student(**student_item)
            )
        Student.objects.bulk_create(students_for_create)

