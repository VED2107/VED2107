# API Documentation

## Overview

The VED Portfolio API is built with Next.js Route Handlers and Server Actions. All endpoints follow RESTful conventions and return JSON responses.

## Base URL

- **Development**: `http://localhost:3000/api`
- **Production**: `https://ved.exe.snowbros.me/api`

## Authentication

Most API endpoints require authentication via Supabase JWT tokens.

```
Authorization: Bearer <supabase_access_token>
```

## Response Format

All responses follow a consistent format:

### Success
```json
{
  "success": true,
  "data": { ... },
  "message": "Operation successful"
}
```

### Error
```json
{
  "success": false,
  "error": {
    "code": "ERROR_CODE",
    "message": "Human-readable error message"
  }
}
```

## Endpoints

### Health Check

```
GET /api/health
```

Returns the API health status. No authentication required.

**Response:**
```json
{
  "status": "ok",
  "timestamp": "2026-06-23T00:00:00.000Z",
  "version": "1.0.0"
}
```

---

### Auth

#### Get Current User
```
GET /api/auth/me
```

Returns the authenticated user's profile.

**Response:**
```json
{
  "success": true,
  "data": {
    "id": "uuid",
    "email": "user@example.com",
    "name": "User Name",
    "avatar_url": "https://...",
    "created_at": "2026-01-01T00:00:00.000Z"
  }
}
```

---

### Projects

#### List Projects
```
GET /api/projects
```

**Query Parameters:**
| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `page` | number | 1 | Page number |
| `limit` | number | 10 | Items per page |
| `category` | string | — | Filter by category |

**Response:**
```json
{
  "success": true,
  "data": {
    "projects": [...],
    "total": 25,
    "page": 1,
    "limit": 10
  }
}
```

#### Get Project
```
GET /api/projects/:id
```

**Response:**
```json
{
  "success": true,
  "data": {
    "id": "uuid",
    "title": "Project Name",
    "description": "Project description",
    "tech_stack": ["Next.js", "TypeScript"],
    "github_url": "https://github.com/...",
    "live_url": "https://...",
    "created_at": "2026-01-01T00:00:00.000Z"
  }
}
```

---

### Contact

#### Send Message
```
POST /api/contact
```

**Request Body:**
```json
{
  "name": "John Doe",
  "email": "john@example.com",
  "subject": "Collaboration inquiry",
  "message": "I'd like to discuss..."
}
```

**Response:**
```json
{
  "success": true,
  "message": "Message sent successfully"
}
```

---

## Rate Limiting

API endpoints are rate-limited using Redis token buckets:

| Tier | Requests | Window |
|------|----------|--------|
| Public | 60 | 1 minute |
| Authenticated | 200 | 1 minute |
| Admin | 1000 | 1 minute |

When rate limited, the API returns:
```
HTTP 429 Too Many Requests
```

## Error Codes

| Code | HTTP Status | Description |
|------|-------------|-------------|
| `AUTH_REQUIRED` | 401 | Authentication required |
| `FORBIDDEN` | 403 | Insufficient permissions |
| `NOT_FOUND` | 404 | Resource not found |
| `VALIDATION_ERROR` | 422 | Invalid request data |
| `RATE_LIMITED` | 429 | Too many requests |
| `INTERNAL_ERROR` | 500 | Internal server error |

## SDK / Client Usage

```typescript
// Using fetch
const response = await fetch('/api/projects', {
  headers: {
    'Authorization': `Bearer ${token}`,
    'Content-Type': 'application/json',
  },
});
const data = await response.json();
```
