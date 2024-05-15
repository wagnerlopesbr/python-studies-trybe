FROM python:3-alpine3.17

# Set the working directory in the container to /src
WORKDIR /src

# Copy the dependencies file (*requirements.txt) to the working directory (./ = /src/)
COPY src/*requirements.txt ./
# Install the dependencies; --no-cache-dir is used to not cache the downloaded packages
RUN pip install --no-cache-dir -r requirements.txt

# environment variable to set the flask environment
ARG FLASK_ENV
# Install the development dependencies if the FLASK_ENV is set to dev; "fi" is used to end the if statement
RUN if ["$FLASK_ENV" = "dev"]; then pip install --no-cache-dir -r requirements-dev.txt; fi

# Copy the source code to the working directory
COPY ./src .

# command to run on container start
CMD ["python3", "app.py"]
