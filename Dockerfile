FROM python
WORKDIR /home/myapp
COPY requeriments.txt .
RUN pip install -r requeriments.txt
COPY . .
EXPOSE 5050
CMD ["python", "sample_app.py"]
