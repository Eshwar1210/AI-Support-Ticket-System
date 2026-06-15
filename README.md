# AI-Powered Support Ticket Analysis System

## Overview

This project is an AI-powered support ticket analysis system built using Python, FastAPI, Pandas, and Groq Llama 3. The application allows users to query support ticket data using natural language, detect anomalies in ticket records, and access insights through REST API endpoints.

---

## Features

* Natural language querying of support ticket data
* Automated anomaly detection
* REST API built with FastAPI
* Support for ticket analytics and operational insights

---

## System Architecture

```text
User Request
     │
     ▼
  FastAPI
     │
     ▼
Query Engine
     │
     ▼
 Groq Llama 3
     │
     ▼
 Ticket Dataset
```

---

## Project Structure

```text
project/
│
├── main.py
├── query_engine.py
├── anomaly.py
├── support_tickets.xlsx
├── requirements.txt
├── .env
└── README.md
```

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Eshwar1210/AI-Support-Ticket-System.git
cd project
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure Environment Variables

Create a `.env` file in the project root directory:

```env
GROQ_API_KEY=your_api_key_here
```

---

## Running the Application

Start the FastAPI server:

```bash
python -m uvicorn main:app --reload
```

API documentation will be available at:

```text
http://127.0.0.1:8000/docs
```

---

## API Endpoints

| Method | Endpoint   | Description                     |
| ------ | ---------- | ------------------------------- |
| GET    | /health    | Health check endpoint           |
| POST   | /query     | Natural language query endpoint |
| GET    | /anomalies | Detect anomalous tickets        |

---

## Example Query

### Request

```json
{
  "question": "How many tickets are currently open?"
}
```

### Response

```json
{
  "answer": "The dataset contains 42 open tickets."
}
```

---

## Design Decisions

* FastAPI was chosen for its simplicity, performance, and automatic API documentation.
* Pandas was used for efficient data loading and analysis.
* Groq Llama 3 was selected to enable natural language interaction with ticket data.

---

## Known Limitations

* Dataset is loaded into memory.
* Anomaly detection is rule-based.
* Query accuracy depends on LLM responses.

---

## Author

AI Engineer Assessment Submission
