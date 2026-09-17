# 🐛 FastAPI Issue Tracker

A lightweight REST API for tracking issues — built with **FastAPI** and backed by simple JSON file storage. Create, update, and manage issues with priorities and statuses, no database required.

## ✨ Features

- 📋 Full CRUD for issues — create, read, update, delete
- 🏷️ Priority levels (`low`, `medium`, `high`) and status tracking (`open`, `in progress`, `closed`)
- ✅ Request validation via Pydantic models
- ⏱️ Response timing middleware (`X-Process-Time` header on every response)
- 🌐 CORS enabled out of the box
- 💾 Zero-setup JSON file storage — no database to configure

## 🛠️ Tech Stack

| Component | Technology |
|---|---|
| Framework | [FastAPI](https://fastapi.tiangolo.com/) |
| Server | [Uvicorn](https://www.uvicorn.org/) |
| Validation | [Pydantic](https://docs.pydantic.dev/) |
| Storage | JSON file (`Data/issues.json`) |

## 📁 Project Structure

```
FASTAPI-ISSUE-TRACKER/
├── app/
│   ├── middleware/
│   │   └── timer.py        # Request timing middleware
│   └── routes/
│       ├── issues.py        # Issue CRUD endpoints
│       ├── schemas.py       # Pydantic models & enums
│       └── storage.py       # JSON read/write helpers
├── Data/
│   └── issues.json          # Issue data store (auto-created)
├── main.py                  # App entrypoint
└── requirements.txt
```

## 🚀 Getting Started

### Prerequisites

- Python 3.13+

### Installation

```bash
# Clone the repository
git clone <your-repo-url>
cd FASTAPI-ISSUE-TRACKER

# Create and activate a virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Run the server

```bash
uvicorn main:app --reload
```

The API will be available at **http://127.0.0.1:8000**, with interactive docs at **http://127.0.0.1:8000/docs**.

## 📡 API Reference

Base path: `/api/v1/issues`

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/issues` | List all issues |
| `POST` | `/create` | Create a new issue |
| `GET` | `/{issue_id}` | Get a single issue by ID |
| `PUT` | `/update/{issue_id}` | Update an existing issue |
| `DELETE` | `/{issue_id}` | Delete an issue |

### Create an issue

```bash
curl -X POST http://127.0.0.1:8000/api/v1/issues/create \
  -H "Content-Type: application/json" \
  -d '{
        "title": "Login button unresponsive",
        "description": "Clicking login does nothing on Safari",
        "priority": "high"
      }'
```

**Response**

```json
{
  "id": "b3f1c2e4-...",
  "title": "Login button unresponsive",
  "description": "Clicking login does nothing on Safari",
  "priority": "high",
  "status": "open"
}
```

### Update an issue

```bash
curl -X PUT http://127.0.0.1:8000/api/v1/issues/update/{issue_id} \
  -H "Content-Type: application/json" \
  -d '{ "status": "in progress" }'
```

### Delete an issue

```bash
curl -X DELETE http://127.0.0.1:8000/api/v1/issues/{issue_id}
```

## 📝 Issue Model

| Field | Type | Notes |
|---|---|---|
| `id` | `string` | UUID, auto-generated |
| `title` | `string` | 3–50 characters |
| `description` | `string` | 10–100 characters on create |
| `priority` | `low \| medium \| high` | Defaults to `low` |
| `status` | `open \| in progress \| closed` | Defaults to `open` |

## 📄 License

This project is available for personal and educational use.
