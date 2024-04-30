"""
Django command to pause and wait for the database to be available
"""
import time

from psycopg2 import OperationalError as Psycopg2Error
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Django command to pause and wait for the
    database to be available"""
    def handle(self, *args, **options):
        """
        Entrypoint to pause and wait for the database to be available
        """
        self.stdout.write(self.style.WARNING('Waiting for database...'))

        db_up = False
        while not db_up:
            try:
                self.check(databases=['default'])
                db_up = True
            except (Psycopg2Error, OperationalError):
                self.stdout.write(
                    self.style.WARNING('Database waiting for connection ...')
                )
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS('Database is ready !'))
