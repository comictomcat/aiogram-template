# Set base image
FROM python:3.8.6-slim

# Set the working directory
WORKDIR /bot

# Copying the dependencies file
COPY requirements.txt .

# Installing dependencies
RUN pip install -r requirements.txt

# Copying files into working directory
COPY . /bot

# Running the bot
CMD [ "python", "-m", "app" ]