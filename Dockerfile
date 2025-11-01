FROM mcr.microsoft.com/playwright/python:v1.40.0-focal

WORKDIR /app

ENV PYTHONPATH=/app

# Install python deps first to leverage Docker cache
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy project
COPY . .

# Ensure Playwright browsers are installed (no-op if already present)
RUN python -m playwright install --with-deps || true

# Run your tests or script
CMD ["pytest", "-n", "10", "--tracing=retain-on-failure"]


