from django.core.management.base import BaseCommand, CommandError  # noqa: D100

from portal.users.management.commands._create_user import add_user_options, create_user


class Command(BaseCommand):  # noqa: D101
    help = "Creates a student user in portal"

    def add_arguments(self, parser):  # noqa: D102
        add_user_options(parser)

    def handle(self, *args, **options):  # noqa: D102
        try:
            user = create_user(user_type="student", **options)
        except Exception as e:
            raise CommandError(f"Could not create student: {e}")

        self.stdout.write(self.style.SUCCESS(f"Successfully created student {user}"))
