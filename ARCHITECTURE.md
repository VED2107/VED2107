# Architecture

## Overview

VED Portfolio is built with a modern, scalable architecture using Next.js and TypeScript. This document outlines the system design, key decisions, and technical patterns used throughout the project.

## Tech Stack

| Layer | Technology | Purpose |
|-------|-----------|---------|
| Frontend | Next.js 14, React 18, TypeScript | UI rendering, routing, SSR/SSG |
| Styling | Tailwind CSS | Utility-first CSS framework |
| Database | Supabase (PostgreSQL) | Data persistence, auth |
| AI Services | OpenAI GPT | Content generation, analysis |
| Deployment | Vercel | Hosting, CI/CD, edge functions |
| Monitoring | Sentry | Error tracking, performance |
| Analytics | PostHog | Product analytics |
| Cache | Upstash Redis | Rate limiting, session cache |

## Directory Structure

```
src/
├── app/                    # Next.js App Router pages
│   ├── (auth)/             # Auth-related routes
│   ├── (dashboard)/        # Dashboard routes
│   ├── api/                # API route handlers
│   └── layout.tsx          # Root layout
├── components/             # Reusable UI components
│   ├── ui/                 # Base UI primitives
│   ├── forms/              # Form components
│   └── layouts/            # Layout components
├── hooks/                  # Custom React hooks
├── lib/                    # Utility libraries
│   ├── supabase/           # Supabase client config
│   ├── openai/             # OpenAI integration
│   └── utils.ts            # Shared utilities
├── types/                  # TypeScript type definitions
└── styles/                 # Global styles
```

## Key Architecture Decisions

### 1. Next.js App Router
- Server Components by default for optimal performance
- Server Actions for form mutations
- Route handlers for API endpoints
- Streaming SSR for improved TTFB

### 2. Database Design
- PostgreSQL via Supabase for relational data
- Row Level Security (RLS) for data access control
- Migrations managed via Supabase CLI

### 3. Authentication
- Supabase Auth with Google OAuth
- JWT-based session management
- Middleware-based route protection

### 4. API Design
- RESTful route handlers in `/app/api/`
- Server Actions for form submissions
- Rate limiting via Redis token buckets

## Data Flow

```
User Action → React Component → Server Action / API Route
    → Business Logic → Database / AI Service → Response → UI Update
```

## Security

- Environment variables for all secrets
- RLS policies on all database tables
- CSRF protection via Next.js defaults
- Input validation with Zod schemas
- Rate limiting on API endpoints

## Performance

- Static generation where possible
- Image optimization via Next.js `<Image>`
- Code splitting with dynamic imports
- Edge caching via Vercel CDN
- Redis caching for expensive operations

## Scaling Strategy

| Users | Infrastructure |
|-------|---------------|
| 0–100 | Single Supabase instance, Vercel hobby |
| 100–1K | Redis caching, Vercel Pro |
| 1K–10K | CDN, read replicas, queue system |
| 10K+ | Microservices, dedicated AI pipelines |

## Contributing

See [CONTRIBUTING.md](./CONTRIBUTING.md) for development guidelines.
