FROM python:3.12


WORKDIR /app
COPY . .


RUN pip install -r requirements.txt

CMD ["python", "manage.py", "runserver", "0.0.0.0:3333"]

EXPOSE 3333