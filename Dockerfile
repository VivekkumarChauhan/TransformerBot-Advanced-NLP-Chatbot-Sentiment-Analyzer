# Use official python image as a parent image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the requirements.txt and install dependencies
COPY chatbot/requirements.txt ./chatbot/requirements.txt
COPY sentiment_analysis/requirements.txt ./sentiment_analysis/requirements.txt
RUN pip install --upgrade pip && \
    pip install -r chatbot/requirements.txt && \
    pip install -r sentiment_analysis/requirements.txt

# Copy the entire project directory to the container
COPY . .

# Command to run both Flask and Streamlit apps
CMD ["sh", "-c", "streamlit run sentiment_analysis/app.py & python chatbot/app.py"]
