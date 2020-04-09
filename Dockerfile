FROM python:3.8
COPY . /school-system
WORKDIR /school-system
RUN pip install -r requirements.txt
ENV FLASK_ENV docker
ENTRYPOINT ["python"]
CMD ["app.py"]