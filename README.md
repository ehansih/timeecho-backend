<div align="center">

# ⏳ TimeEcho Backend

FastAPI AI image-to-video pipeline — living memory app backend.

![Python](https://img.shields.io/badge/python-3.10+-blue?logo=python) ![FastAPI](https://img.shields.io/badge/FastAPI-green?logo=fastapi) ![Last Commit](https://img.shields.io/github/last-commit/ehansih/timeecho-backend)

</div>

---

# TimeEcho Backend

FastAPI backend for TimeEcho — an AI-powered time-aware living memory platform.

## Tech Stack
- **Framework**: FastAPI (Python)
- **AI**: Claude API (Anthropic)
- **Media**: Cloudinary
- **Database**: PostgreSQL

## Features
- AI image-to-video pipeline
- Memory indexing and retrieval by time context
- REST API with async support
- Cloudinary media management

## Getting Started

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

### Environment Variables
```env
ANTHROPIC_API_KEY=your_key
CLOUDINARY_URL=cloudinary://...
DATABASE_URL=postgresql://...
```

## API Docs
Swagger UI available at `/docs` when running locally.

## Related
- [TimeEcho Frontend](https://github.com/ehansih/timeecho-frontend) — Next.js frontend

## Author
**Harsh Vardhan Singh Chauhan** — [github.com/ehansih](https://github.com/ehansih)
