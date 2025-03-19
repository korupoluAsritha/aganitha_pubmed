# Use the official Python image with version 3.13
FROM python:3.13-slim

# Set the working directory inside the container
WORKDIR /app

# Install Poetry
RUN pip install poetry

# Copy pyproject.toml and poetry.lock to install dependencies
COPY pyproject.toml poetry.lock ./

# Install dependencies
RUN poetry config virtualenvs.create false
RUN poetry install --no-root --no-interaction --no-ansi



# Copy the entire project to the container
COPY . .

# Expose port for the Flask server (if you extend it later)
EXPOSE 5000

# Command to run the CLI application
ENTRYPOINT ["python", "src/cli/main.py"]

# Run tests
CMD ["pytest", "tests"]
