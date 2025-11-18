# Security Guide

This guide details all security features and best practices for the MAS Security module.

## Built-in Security Features

All security features are enabled by default and work automatically. No configuration is required for basic security.

### CSRF Protection

**What it is:** Cross-Site Request Forgery (CSRF) protection prevents unauthorized form submissions from external sites.

**How it works:**
- Each form includes a unique CSRF token
- Token is validated on form submission
- Invalid or missing tokens are rejected
- Tokens expire after a set time period

**Status:** Always enabled, cannot be disabled

**Protection Level:** High - Prevents CSRF attacks effectively

### Rate Limiting

**What it is:** Limits the number of form submissions per IP address within a time window.

**Default Settings:**
- **Limit:** 3 submissions per hour per IP
- **Window:** 1 hour rolling window
- **Action on Exceed:** Submission is blocked

**Configuration:**
- Adjustable in module settings
- Can be made stricter or more lenient
- Applies per IP address

**Protection Level:** Medium-High - Prevents abuse and spam

**Best Practices:**
- Monitor logs to adjust limits
- Balance between security and usability
- Consider legitimate use cases

### Input Sanitization

**What it is:** All user input is sanitized and validated before processing.

**Process:**
1. Input is received from form
2. Sanitized to remove malicious content
3. Validated against expected format
4. Processed only if valid

**Protection Against:**
- XSS (Cross-Site Scripting) attacks
- SQL injection attempts
- Malformed data
- Encoding attacks

**Status:** Always enabled, cannot be disabled

**Protection Level:** High - Essential security layer

### Honeypot Protection

**What it is:** Hidden form fields that detect automated bot submissions.

**How it works:**
- Invisible fields added to forms
- Legitimate users never see or fill them
- Bots often fill all fields automatically
- Submissions with honeypot fields filled are rejected

**Status:** Always enabled, cannot be disabled

**Protection Level:** Medium - Effective against basic bots

**Limitations:**
- Advanced bots may bypass
- Used in combination with other protections

### Email Security

**Features:**
- Secure email sending via CMSMS mailer
- No sensitive data in email subjects
- Encrypted connections when possible
- Proper email headers

**Best Practices:**
- Use dedicated security email address
- Monitor email delivery
- Use SPF/DKIM records for email domain
- Consider encrypted email for sensitive reports

### Event Logging

**What is logged:**
- All form submissions
- Rate limit violations
- Security events
- Admin actions
- Timestamps and IP addresses

**Purpose:**
- Security auditing
- Incident investigation
- Pattern detection
- Compliance requirements

**Access:**
- View logs in admin interface
- **Extensions → MAS Security → Security Logs**
- Logs are stored securely

**Retention:**
- Logs are kept according to CMSMS settings
- Consider backup and archival policies

## Security Best Practices

### For Administrators

1. **Regular Monitoring:**
   - Review security logs weekly
   - Check for suspicious patterns
   - Monitor rate limit violations

2. **Prompt Response:**
   - Respond to reports within 24-48 hours
   - Investigate vulnerabilities quickly
   - Keep researchers informed

3. **Access Control:**
   - Limit admin access to trusted users
   - Use strong passwords
   - Enable two-factor authentication if available

4. **Updates:**
   - Keep CMSMS updated
   - Update module when new versions are released
   - Review security advisories

5. **Backup:**
   - Regular backups of database
   - Backup module data files
   - Test restore procedures

### For Website Owners

1. **Security.txt File:**
   - Create `/security.txt` file
   - Include contact information
   - Link to VDP page
   - Link to acknowledgments page

2. **Clear Communication:**
   - Maintain clear VDP
   - Set realistic timelines
   - Communicate expectations

3. **Recognition:**
   - Acknowledge researchers promptly
   - Maintain acknowledgments page
   - Consider bug bounty programs

4. **Incident Response:**
   - Have a response plan
   - Know who to contact
   - Document procedures

### For Security Researchers

1. **Responsible Disclosure:**
   - Follow the VDP guidelines
   - Provide clear vulnerability details
   - Allow reasonable time for fixes
   - Coordinate public disclosure

2. **Report Quality:**
   - Include detailed descriptions
   - Provide proof of concept if possible
   - Suggest remediation if known
   - Be professional and courteous

## Security Considerations

### Module Security

The module itself is designed with security in mind:

- **Input Validation:** All inputs validated
- **Output Escaping:** All outputs properly escaped
- **SQL Injection Protection:** Uses parameterized queries
- **XSS Protection:** Content sanitized before display
- **Access Control:** Admin functions protected
- **Error Handling:** Errors don't leak sensitive information

### Server Security

Ensure your server is properly secured:

- **PHP Version:** Use supported PHP versions (7.4-8.6)
- **Server Updates:** Keep server software updated
- **Firewall:** Configure appropriate firewall rules
- **SSL/TLS:** Use HTTPS for all connections
- **File Permissions:** Set correct file permissions

### CMSMS Security

Follow CMSMS security best practices:

- **CMSMS Updates:** Keep CMSMS updated
- **Module Updates:** Update modules regularly
- **Admin Security:** Secure admin access
- **Database Security:** Use strong database passwords
- **Backup Strategy:** Regular backups

## Threat Mitigation

### Common Threats

**Spam Submissions:**
- Mitigated by: Rate limiting, honeypot fields
- Monitor: Security logs for patterns
- Action: Adjust rate limits if needed

**Automated Attacks:**
- Mitigated by: Honeypot fields, CSRF tokens
- Monitor: Logs for bot patterns
- Action: Review and block if necessary

**Malicious Input:**
- Mitigated by: Input sanitization, validation
- Monitor: Logs for unusual input
- Action: Review and investigate

**Unauthorized Access:**
- Mitigated by: CMSMS access control, CSRF protection
- Monitor: Admin access logs
- Action: Review access patterns

## Compliance and Standards

The module helps with:

- **Responsible Disclosure:** Facilitates proper vulnerability reporting
- **Security Transparency:** Public acknowledgments page
- **Audit Trail:** Comprehensive event logging
- **Best Practices:** Follows security industry standards

## Security Updates

Stay informed about:

- Module security updates
- CMSMS security advisories
- PHP security updates
- Server security patches

## Reporting Security Issues

If you find a security issue in the module itself:

1. **Do NOT** disclose publicly immediately
2. Contact: info [at] newstargeted [dot] com
3. Provide detailed information
4. Allow time for fix before disclosure
5. Follow responsible disclosure practices

## Related Guides

- [Installation Guide](installation.md) - Secure installation
- [Configuration Guide](configuration.md) - Security settings
- [Usage Guide](usage.md) - Secure usage
- [Troubleshooting Guide](troubleshooting.md) - Security issues

## Support

For security-related questions:

- Review security documentation
- Check security logs
- Contact security team: info [at] newstargeted [dot] com

**Important:** For urgent security issues, contact support immediately.

