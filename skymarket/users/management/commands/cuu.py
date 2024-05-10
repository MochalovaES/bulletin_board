from django.core.management import BaseCommand
from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.create(
            email='mochalova.es@mail.ru',
            first_name='Ekaterina',
            last_name='Mochalova',
            phone=None,
            role='user',
            is_active=True
        )

        user.set_password('12345qwerty')
        user.save()
