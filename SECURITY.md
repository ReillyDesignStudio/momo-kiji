# Security Policy

## Reporting a Vulnerability

**Do not open a public GitHub issue for security vulnerabilities.**

If you discover a security vulnerability in momo-kiji, please email:

📧 **robert.reilly@reillydesignstudio.com**

**Include:**
- Description of the vulnerability
- Steps to reproduce
- Potential impact
- Any suggested fixes

## Response Timeline

- **24 hours:** Acknowledge receipt
- **72 hours:** Provide initial assessment
- **7 days:** Patch release or mitigation plan
- **30 days:** Public disclosure (unless circumstances require different timeline)

## Supported Versions

| Version | Status | Supported Until |
|---------|--------|-----------------|
| 1.0.x   | Current | March 2027 |
| 0.9.x   | Legacy | Sept 2026 |
| < 0.9   | Unsupported | EOL |

Security updates are issued for supported versions only.

## Security Best Practices

When using momo-kiji:

1. **Keep updated:** Regularly update to latest version
   ```bash
   pip install --upgrade momo-kiji
   ```

2. **Review generated code:** Always review ANE compilation output
   - Don't blindly deploy generated code
   - Test locally first

3. **Model safety:** Be careful with untrusted models
   - Models can execute arbitrary code during loading
   - Only load models from trusted sources

4. **API keys:** Never hardcode credentials
   - Use environment variables
   - Use secure vaults (1Password, AWS Secrets Manager, etc.)

## Responsible Disclosure

We follow responsible disclosure principles:

- We will acknowledge receipt within 24 hours
- We commit to good-faith effort to resolve
- We will credit you publicly (unless you prefer anonymity)
- We will not disclose details until fix is released
- We thank you for helping keep momo-kiji secure

## Security Contact

**Maintainer:** Robert Reilly  
**Email:** robert.reilly@reillydesignstudio.com  
**GitHub:** [@rdreilly58](https://github.com/rdreilly58)

---

Thank you for helping keep momo-kiji safe! 🔒
