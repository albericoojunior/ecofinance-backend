
FROM dhi.io/python:3-debian13-sfw-ent-dev

WORKDIR /app
COPY requirements.txt ./
RUN python3 -m pip install -r requirements.txt
COPY . .

EXPOSE 8000

CMD ["python", "run.py"]
