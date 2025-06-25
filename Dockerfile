FROM python:3.13

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . .

RUN python manage.py collectstatic --noinput

# Copia o script de inicialização
COPY start.sh /app/start.sh
RUN chmod +x /app/start.sh

# Usa o script com echo + gunicorn
CMD ["/app/start.sh"]