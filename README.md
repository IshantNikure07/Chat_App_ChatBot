# Bubble Chatbot API

Bubble is a friendly, warm, and helpful AI assistant for the Bubble chatting/messaging app. It provides conversational answers using a local retrieval-augmented generation (RAG) pipeline powered by a Chroma Vector Store (containing FAQ context) and the Groq LLM (`llama-3.1-8b-instant`).

This repository is fully containerized using Docker and Docker Compose.

---

## Prerequisites

Make sure you have the following installed on your host system:
* [Docker](https://docs.docker.com/get-docker/) (v20.10 or higher)
* [Docker Compose](https://docs.docker.com/compose/install/) (v2.0 or higher)

---

## Configuration

Before starting the application, you need to configure the required environment variables.

1. Copy `.env.example` to `.env`:
   ```bash
   cp .env.example .env
   ```
2. Open `.env` and set your `GROQ_API_KEY`:
   ```env
   GROQ_API_KEY=gsk_your_actual_groq_api_key_here
   ```

---

## Running with Docker Compose (Recommended)

Docker Compose simplifies building, running, and managing the container lifecycle.

### 1. Build and Start the Application
Run the following command to build the image and start the service in detached mode:
```bash
docker compose up --build -d
```

### 2. View Logs
To check the application logs and ensure everything initialized successfully:
```bash
docker compose logs -f
```

### 3. Check Health Status
Verify that the container is healthy (using the built-in curl healthcheck):
```bash
docker compose ps
```

### 4. Stop the Application
To stop and remove the container:
```bash
docker compose down
```

---

## Running with Docker CLI

If you prefer using the raw Docker CLI:

### 1. Build the Image
```bash
docker build -t bubble-chatbot .
```

### 2. Run the Container
```bash
docker run -p 8000:8000 --env-file .env --name bubble_chatbot bubble-chatbot
```

---

## API Documentation and Testing

Once the application is running, the API will be available at `http://localhost:8000`.

### 1. Healthcheck / Status Endpoint
Verify the API is running:
* **Request**:
  ```bash
  curl http://localhost:8000/
  ```
* **Response**:
  ```json
  {"message": "Chatbot API running"}
  ```

### 2. Chat Endpoint
Ask the chatbot questions:
* **Request**:
  ```bash
  curl -X POST http://localhost:8000/chat \
    -H "Content-Type: application/json" \
    -d '{"message": "How do I add a friend?", "sender_id": "user_123"}'
  ```
* **Response**:
  ```json
  {
    "success": true,
    "answer": "To add a friend in Bubble, you can search for their username..."
  }
  ```

### 3. Interactive API Docs
Open your browser and navigate to:
* Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)
* Redoc: [http://localhost:8000/redoc](http://localhost:8000/redoc)
