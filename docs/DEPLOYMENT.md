# Deployment Guide

## Overview

This project is deployed on **Vercel** with automatic deployments from the `main` branch. This guide covers setup, configuration, and deployment procedures.

## Deployment Platforms

| Environment | Platform | Branch | URL |
|-------------|----------|--------|-----|
| Production | Vercel | `main` | https://ved.exe.snowbros.me |
| Preview | Vercel | PR branches | Auto-generated |
| Development | Local | Any | http://localhost:3000 |

## Prerequisites

- [Vercel account](https://vercel.com/signup)
- [Vercel CLI](https://vercel.com/docs/cli) (optional)
- GitHub repository connected to Vercel

## Initial Setup

### 1. Connect to Vercel

```bash
# Install Vercel CLI
npm i -g vercel

# Login
vercel login

# Link project
vercel link
```

### 2. Configure Environment Variables

In the Vercel dashboard, add these environment variables:

| Variable | Environment | Required |
|----------|-------------|----------|
| `NEXT_PUBLIC_SUPABASE_URL` | All | Yes |
| `NEXT_PUBLIC_SUPABASE_ANON_KEY` | All | Yes |
| `SUPABASE_SERVICE_ROLE_KEY` | Production, Preview | Yes |
| `OPENAI_API_KEY` | Production, Preview | Yes |
| `NEXT_PUBLIC_ENABLE_ANALYTICS` | Production | No |
| `NEXT_PUBLIC_ENABLE_SENTRY` | Production | No |

### 3. Configure GitHub Actions

Add these secrets to your GitHub repository (`Settings → Secrets → Actions`):

- `VERCEL_TOKEN` — Vercel API token
- `VERCEL_ORG_ID` — Vercel organization ID
- `VERCEL_PROJECT_ID` — Vercel project ID

## Deployment Process

### Automatic Deployment

Every push to `main` triggers an automatic deployment:

```
Push to main → GitHub Actions CI → Lint → Type Check → Build → Test → Deploy to Vercel
```

### Manual Deployment

```bash
# Preview deployment
vercel

# Production deployment
vercel --prod
```

### Rollback

```bash
# List recent deployments
vercel ls

# Promote a previous deployment
vercel promote <deployment-url>
```

## CI/CD Pipeline

The GitHub Actions workflow (`.github/workflows/ci.yml`) runs on every push and PR:

1. **Lint** — ESLint code quality checks
2. **Type Check** — TypeScript compilation
3. **Build** — Next.js production build
4. **Test** — Jest test suite
5. **Deploy** — Vercel deployment (main branch only)

## Build Configuration

### next.config.js

```javascript
/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: true,
  images: {
    domains: ['your-domain.com'],
  },
  headers: async () => [
    {
      source: '/(.*)',
      headers: [
        { key: 'X-Frame-Options', value: 'DENY' },
        { key: 'X-Content-Type-Options', value: 'nosniff' },
        { key: 'Referrer-Policy', value: 'origin-when-cross-origin' },
      ],
    },
  ],
};

module.exports = nextConfig;
```

## Monitoring

### Error Tracking
- **Sentry** captures runtime errors in production
- Configure via `SENTRY_DSN` environment variable

### Analytics
- **PostHog** tracks user behavior
- Configure via `NEXT_PUBLIC_POSTHOG_KEY`

### Performance
- **Vercel Analytics** monitors Core Web Vitals
- Enable in Vercel dashboard under `Analytics`

## Troubleshooting

### Build Failures

```bash
# Test build locally
npm run build

# Check for type errors
npm run type-check

# Check for lint errors
npm run lint
```

### Environment Variables Not Working

- Verify variables are set in the correct Vercel environment
- Variables prefixed with `NEXT_PUBLIC_` are exposed to the browser
- Redeploy after changing environment variables

### DNS Issues

- Verify domain is configured in Vercel project settings
- Check DNS propagation at [whatsmydns.net](https://www.whatsmydns.net/)

## Security Checklist

- [ ] All secrets in environment variables (not committed)
- [ ] HTTPS enforced
- [ ] Security headers configured
- [ ] Rate limiting enabled
- [ ] Error messages don't leak implementation details
- [ ] Dependencies audited (`npm audit`)

## Contact

For deployment issues, contact:
- Email: VEDCHAUHAN2107@gmail.com
- GitHub: [@VED2107](https://github.com/VED2107)
