# Security Best Practices Implemented
- DEBUG set to False
- Browser protections enabled: XSS filter, NoSniff, and DENY for X-Frames
- CSRF and Session cookies restricted to HTTPS
- All forms protected with {% csrf_token %}
- ORM used for queries to prevent SQL injection
- Content Security Policy (CSP) enabled via django-csp
