FROM python:3.8


COPY . /usr/src/app

WORKDIR /usr/src/app

RUN pip install --no-cache -r requirements.txt

CMD ["python", "carbon_tool/manage.py", "runserver", "0.0.0.0:8000"]


