FROM python:3.12

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN mkdocs build

EXPOSE 8080

CMD ["mkdocs", "serve", "--dev-addr=0.0.0.0:8080"]

# docker build -t cwapi3d-py .
# docker run --rm -p 8080:8080 cwapi3d-py