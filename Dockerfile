FROM mcr.microsoft.com/playwright/python:v1.40.0-focal

WORKDIR /app

# Copy your project files
COPY . .

# Install Playwright package and your dependencies
RUN pip install playwright
RUN playwright install --with-deps
RUN pip install -r requirements.txt

# Run your tests or script
CMD ["pytest", "--numprocesses", "10", "--tracing=retain-on-failure"]