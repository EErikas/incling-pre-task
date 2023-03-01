FROM python:3.9.15-alpine
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
RUN python manage.py makemigrations 
RUN chmod +x start.sh
CMD [ "./start.sh" ]