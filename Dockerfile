FROM python:3.7-slim
WORKDIR ./
COPY ./requirement.txt ./requirement.txt
RUN pip install -r requirement.txt
COPY ./sc_microservice_1.py ./sc_microservice_1.py
CMD ["python3","./sc_microservice_1.py"]
