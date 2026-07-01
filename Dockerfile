FROM mcr.microsoft.com/playwright/python:v1.60.0-noble
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["pytest", "web/tests/", "--alluredir=allure-results"]