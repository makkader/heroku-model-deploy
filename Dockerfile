FROM python:3.8


# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt
COPY ./server.py /app/main.py
COPY ./airline-sklearn.pkl /app/airline-sklearn.pkl



WORKDIR /app

RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["main.py" ]

