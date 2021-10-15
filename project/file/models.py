import csv
import io
from time import time

from django.db import models
from project.person.models import Person

# Logging Django
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)


def import_data_create(pk):
    initial = time()
    logger.debug('File receive.')

    file = File.objects.get(pk=pk).file
    content = file.read().decode('UTF-8')
    io_string = io.StringIO(content)
    next(io_string)

    for column in csv.reader(io_string, delimiter=',', quotechar='"'):
        _, created = Person.objects.update_or_create(
            nome=column[0],
        )
        logger.debug(f'Import {column[0]}')

    end = time()
    time_delta = end - initial

    if time_delta < 60:
        logger.debug(f'Processed File in {round(time_delta, 2)} seconds.')
    else:
        logger.debug(f'Processed File in {round(time_delta / 60, 2)} minutes.')


def import_data_bulk(pk):
    initial = time()
    logger.debug('File receive.')

    csv_file = File.objects.get(pk=pk).file
    content = io.TextIOWrapper(csv_file)
    data = csv.DictReader(content)
    list_data = list(data)

    objs = [
        Person(nome=row['name'])
        for row in list_data
    ]

    Person.objects.bulk_create(objs)

    end = time()
    time_delta = end - initial

    if time_delta < 60:
        logger.debug(f'Processed File in {round(time_delta, 2)} seconds.')
    else:
        logger.debug(f'Processed File in {round(time_delta / 60, 2)} minutes.')


METHOD_IMPORT = [
    ('create', 'Create'),
    ('bulk', 'Bulk_Create'),
]


class File(models.Model):
    file = models.FileField()
    method = models.CharField(choices=METHOD_IMPORT, max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)
    uploaded_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.method == 'create':
            import_data_create(self.pk)
        else:
            import_data_bulk(self.pk)

    def __str__(self):
        return str(self.file)
