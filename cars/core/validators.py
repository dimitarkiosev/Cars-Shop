import datetime
from django.core import exceptions

def validate_only_letters(value):
    for x in value:
        if not x.isalpha():
            raise exceptions.ValidationError('Only letters!')


def validate_only_digits(value):
    for x in value:
        if not x.isdigit():
            raise exceptions.ValidationError('Only digits!')


def validate_file_max_size_1mb(fileobj):
    filesize = fileobj.file.size
    megabyte_limit = 1.0
    if filesize > (megabyte_limit * 1024 * 1024):
        raise exceptions.ValidationError(f'Max file size is {megabyte_limit}MB!')


def validate_file_max_size_2mb(fileobj):
    filesize = fileobj.file.size
    megabyte_limit = 2.0
    if filesize > (megabyte_limit * 1024 * 1024):
        raise exceptions.ValidationError(f'Max file size is {megabyte_limit}MB!')


def car_year_validator(value):
    if value < 1900 or value > datetime.datetime.now().year:
        raise exceptions.ValidationError(f'{value} is not a correct year!')