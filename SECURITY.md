# Security Policy

## Supported Versions

| Version | Supported          |
|---------|--------------------|
| 1.x.x   | :white_check_mark: |

## Reporting a Vulnerability

If you discover a security vulnerability, please report it responsibly.

### How to Report

1. **Do NOT** create a public GitHub issue for security vulnerabilities
2. Email **VEDCHAUHAN2107@gmail.com** with:
   - Description of the vulnerability
   - Steps to reproduce
   - Potential impact
   - Suggested fix (if any)

### What to Expect

- **Acknowledgement**: Within 48 hours
- **Initial Assessment**: Within 1 week
- **Resolution Timeline**: Depends on severity
  - Critical: 24–72 hours
  - High: 1 week
  - Medium: 2 weeks
  - Low: Next release cycle

### Severity Levels

| Level | Description | Example |
|-------|------------|---------|
| Critical | Active exploitation possible | RCE, auth bypass, data breach |
| High | Significant risk | SQL injection, XSS, CSRF |
| Medium | Moderate risk | Information disclosure, misconfig |
| Low | Minor risk | Missing headers, verbose errors |

## Security Best Practices

This project follows these security practices:

- **Authentication**: Supabase Auth with JWT tokens
- **Authorization**: Row Level Security (RLS) policies
- **Data Protection**: Environment variables for secrets, no hardcoded credentials
- **Input Validation**: Server-side validation on all inputs
- **Dependencies**: Regular dependency audits via `npm audit`
- **HTTPS**: Enforced via Vercel deployment
- **Headers**: Security headers configured in `next.config.js`

## Responsible Disclosure

We appreciate security researchers who follow responsible disclosure practices. Contributors who report valid security issues will be acknowledged in our security advisories.

## Contact

- Email: VEDCHAUHAN2107@gmail.com
- GitHub: [@VED2107](https://github.com/VED2107)
