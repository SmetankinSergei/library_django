FROM python:3.11

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED = 1

WORKDIR /app_dir

COPY ./requirements.txt /app_dir


RUN pip install -r /app_dir/requirements.txt

COPY . /app_dir

#EXPOSE 8000
#
#CMD ["python", "manage.py", "migrate"]
#CMD ["python", "manage.py", "runserver", "0.0.0.0.8000"]
