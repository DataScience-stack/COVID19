FROM python:3.7
WORKDIR /app
COPY requirements*.txt ./
COPY PatientInfo*.csv ./
COPY Region*.csv ./
RUN pip3 install -r requirements.txt
EXPOSE 8080
COPY . .
CMD streamlit run --server.port 8080 --server.enableCORS false corona_visualization.py