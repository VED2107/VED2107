# Getting Started

Welcome to the VED Portfolio project! This guide will help you set up your development environment and start contributing.

## Prerequisites

- **Node.js** >= 18.0.0 ([Download](https://nodejs.org/))
- **npm** >= 9.0.0 (comes with Node.js)
- **Git** ([Download](https://git-scm.com/))

## Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/VED2107/VED2107.git
cd VED2107
```

### 2. Install Dependencies

```bash
npm install
```

### 3. Set Up Environment Variables

```bash
cp .env.example .env.local
```

Edit `.env.local` and fill in the required values:

| Variable | Required | Description |
|----------|----------|-------------|
| `NEXT_PUBLIC_SUPABASE_URL` | Yes | Supabase project URL |
| `NEXT_PUBLIC_SUPABASE_ANON_KEY` | Yes | Supabase anonymous key |
| `OPENAI_API_KEY` | Yes | OpenAI API key for AI features |
| `NODE_ENV` | No | Defaults to `development` |

### 4. Start Development Server

```bash
npm run dev
```

Visit [http://localhost:3000](http://localhost:3000) to see the app.

## Available Scripts

| Command | Description |
|---------|-------------|
| `npm run dev` | Start development server |
| `npm run build` | Create production build |
| `npm run start` | Start production server |
| `npm run lint` | Run ESLint |
| `npm run format` | Format code with Prettier |
| `npm run type-check` | Run TypeScript type checking |
| `npm run test` | Run test suite |
| `npm run test:watch` | Run tests in watch mode |
| `npm run test:coverage` | Run tests with coverage report |

## Project Structure

```
VED2107/
├── src/
│   ├── app/           # Next.js App Router (pages & API routes)
│   ├── components/    # Reusable React components
│   ├── hooks/         # Custom React hooks
│   ├── lib/           # Utility functions & service clients
│   ├── types/         # TypeScript type definitions
│   └── styles/        # Global CSS styles
├── public/            # Static assets
├── docs/              # Documentation
└── .github/           # GitHub workflows & templates
```

## Common Tasks

### Creating a New Component

```bash
# Create component file
touch src/components/MyComponent.tsx
```

```tsx
interface MyComponentProps {
  title: string;
}

export function MyComponent({ title }: MyComponentProps) {
  return <div>{title}</div>;
}
```

### Adding a New API Route

Create a file at `src/app/api/my-route/route.ts`:

```ts
import { NextResponse } from 'next/server';

export async function GET() {
  return NextResponse.json({ message: 'Hello!' });
}
```

## Troubleshooting

### Port already in use
```bash
npx kill-port 3000
npm run dev
```

### TypeScript errors after pulling
```bash
npm install
npm run type-check
```

### Clearing cache
```bash
rm -rf .next
npm run dev
```

## Next Steps

- Read [CONTRIBUTING.md](../CONTRIBUTING.md) for contribution guidelines
- Review [ARCHITECTURE.md](../ARCHITECTURE.md) for system design
- Check [API.md](./API.md) for API documentation
- See [DEPLOYMENT.md](./DEPLOYMENT.md) for deployment instructions

## Need Help?

- Create a [GitHub Issue](https://github.com/VED2107/VED2107/issues)
- Email: VEDCHAUHAN2107@gmail.com
