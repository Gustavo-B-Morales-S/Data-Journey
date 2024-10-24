# Use a lighter version of the base Python image
FROM python:3.12.4-slim

# Set environment variable to disable pip caching (reduces image size)
ENV PIP_NO_CACHE_DIR=1 \
      POETRY_NO_INTERACTION=1

# Installs system dependencies required for Poetry and Streamlit
# Clears the apt-get cache, removing unnecessary files
RUN apt update && apt install -y --no-install-recommends \
      url \
      build-essential \
      && rm -rf /var/lib/apt/lists/*

# Copy only dependency files to avoid unnecessary recapping
COPY pyproject.toml poetry.lock /source/

# Change the working directory
WORKDIR /source

# Install Poetry without storing temporary cache files
# Disable the creation of virtual environments and install only main dependencies
RUN pip install --no-cache-dir poetry \
      && poetry config virtualenvs.create false \
      && poetry install --only main --no-dev

# Copy the application source code
COPY . /source

# Expose port 8501 to Streamlit
EXPOSE 8501

ENTRYPOINT [
    "poetry",
    "run",
    "streamlit",
    "run",
    "app/app.py",
    "--server.port=8501",
    "--server.address=0.0.0.0"
]
