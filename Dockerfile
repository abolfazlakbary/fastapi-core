FROM python:3.10.12

WORKDIR /project

COPY requirements.txt /project/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /project/

CMD ["python3", "main.py"]

