FROM python:3.10.3-slim

RUN mkdir docker_im
WORKDIR /docker_im

COPY requirenments.txt .
RUN pip install -r requirenments.txt

COPY . .

CMD ["python", "main.py"]