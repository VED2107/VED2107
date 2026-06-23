# Contributing to VED Portfolio

Thank you for your interest in contributing! This document provides guidelines and instructions for contributing.

## Code of Conduct

- Be respectful and inclusive
- Provide constructive feedback
- Focus on code quality and user experience
- Ask questions if something is unclear

## Getting Started

### Prerequisites
- Node.js >= 18.0.0
- npm >= 9.0.0
- Git

### Setup

```bash
# Clone the repository
git clone https://github.com/VED2107/VED2107.git
cd VED2107

# Install dependencies
npm install

# Create environment file
cp .env.example .env.local

# Start development server
npm run dev
```

## Development Workflow

### Branch Naming
- `feature/feature-name` — New features
- `fix/bug-name` — Bug fixes
- `docs/doc-name` — Documentation
- `refactor/task-name` — Code refactoring
- `chore/task-name` — Maintenance tasks

### Before Committing

```bash
# Format code
npm run format

# Lint code
npm run lint

# Type check
npm run type-check

# Run tests
npm run test
```

### Commit Messages

Follow conventional commit format:

```
<type>(<scope>): <subject>

<body>

<footer>
```

**Types:**
- `feat` — New feature
- `fix` — Bug fix
- `docs` — Documentation
- `style` — Code style changes
- `refactor` — Code refactoring
- `perf` — Performance improvements
- `test` — Test additions/changes
- `chore` — Maintenance
- `ci` — CI/CD changes

## Pull Request Process

1. Create a feature branch
2. Make changes and commit
3. Push to GitHub
4. Create a Pull Request
5. Ensure all checks pass

## Code Style Guide

### TypeScript
- Use strict mode
- Define types for all functions
- Avoid `any` type
- Use interfaces for object shapes

### React Components
- Functional components only
- Use hooks for state management
- Prop types should be typed
- Use meaningful variable names

## Testing

- Write tests for new features
- Maintain > 80% code coverage
- Use meaningful test descriptions
- Mock external dependencies

## Documentation

- Update README.md for user-facing changes
- Add comments for complex logic
- Keep CHANGELOG.md updated
- Document API endpoints

## Performance

- Monitor bundle size
- Optimize images and assets
- Use code splitting where appropriate
- Avoid unnecessary re-renders

## Questions?

- Check existing issues and discussions
- Create a GitHub Discussion for questions
- Email: VEDCHAUHAN2107@gmail.com

## License

By contributing, you agree that your contributions will be licensed under the MIT License.
