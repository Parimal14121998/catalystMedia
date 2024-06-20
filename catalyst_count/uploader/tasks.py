from celery import shared_task
from .models import QueryBody
import csv

@shared_task
def process_csv(file_path):
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip the header row
        for row in reader:
            name, industry, year_founded, city, state, country, employees = row
            QueryBody.objects.create(
                name=name,
                industry=industry,
                year_founded=int(year_founded) if year_founded else None,
                city=city,
                state=state,
                country=country,
                employees=int(employees) if employees else None
            )
