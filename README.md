# Trainable AI Backend

## Getting Started

### Step 1: Set Up Python Environment

1. Install Python 3.8+ version

### Step 2: Add Docker

Ensure Docker is installed on your system. If not, download and install it from [Docker's official website](https://www.docker.com/).

### Step 3: Create container

Run the following command to build the docker image:

```bash
docker build . -t trainable-ai-backend
```

### Step 4: Start the Application

Run the following command to start the docker container:

```bash
docker container run --name trainable-ai-api -d -p 8000:8000 trainable-ai-backend
```

### Step 4: Access the Trainable API Container

After the setup is complete, run:

```bash
python run.py
```

This command opens a shell inside the `trainable-ai-api` Docker container, where you can if you want to perform any project-related commands.

## API Docs

You can access API Docs at [http://localhost:8000/docs](http://localhost:8000/docs).

---

That's it! You're all set up to work on the Trainable AI Backend.
