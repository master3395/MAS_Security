# Configuration Guide

This guide covers all configuration options available in the MAS Security module.

## Accessing Configuration

Navigate to **Extensions → MAS Security → Settings** tab in your CMSMS admin panel.

## Automatic Configuration

The module automatically detects and configures the following settings:

### Security Email

The module attempts to detect your security email in this order:

1. **Admin User Email:** Uses the email address of the first admin user (user_id = 1)
2. **Domain-based Fallback:** If no admin email is found, constructs: `security@yourdomain.com`

**Manual Override:** You can manually set the security email in the Settings tab if needed.

### Domain Detection

The module automatically extracts your domain from:

1. CMSMS `root_url` configuration setting
2. HTTP_HOST server variable (fallback)

This is used for:
- Constructing security email addresses
- Generating links in email notifications
- Displaying site information

### Site Name

Uses CMSMS `sitename` configuration or falls back to domain name.

## Manual Configuration Options

### Rate Limiting

**Default:** 3 submissions per hour per IP address

**Configuration:**
- Adjust the rate limit in the module's rate limiting system
- Lower values = stricter (fewer submissions allowed)
- Higher values = more lenient (more submissions allowed)

**Recommendations:**
- **Low traffic sites:** 3-5 per hour
- **Medium traffic sites:** 5-10 per hour
- **High traffic sites:** 10-20 per hour

**Note:** Rate limiting helps prevent abuse and spam submissions.

### Donations Tab

**Optional Feature:** Enable or disable the donations tab in the admin interface.

**To Enable/Disable:**
1. Go to **Extensions → MAS Security → Settings**
2. Toggle the donations tab option
3. Save settings

**Purpose:** Allows users to support module development through donations.

## Email Configuration

### Notification Settings

The module sends email notifications when:

- A new vulnerability report is submitted
- A report status changes
- Security events occur (configurable)

**Email Recipients:**
- Primary: Security email address (auto-detected or manually set)
- Additional: Can be configured in module settings (if supported)

### Email Content

Email notifications include:

- Reporter information (name, email, if provided)
- Vulnerability details
- Submission timestamp
- IP address (for security tracking)
- Direct link to view report in admin panel

## Security Settings

All security features are enabled by default:

### CSRF Protection

- **Status:** Always enabled
- **Purpose:** Prevents Cross-Site Request Forgery attacks
- **Action:** No configuration needed - works automatically

### Input Sanitization

- **Status:** Always enabled
- **Purpose:** Sanitizes all user input before processing
- **Action:** No configuration needed - works automatically

### Honeypot Protection

- **Status:** Always enabled
- **Purpose:** Detects and blocks automated bot submissions
- **Action:** No configuration needed - works automatically

### Event Logging

- **Status:** Always enabled
- **Purpose:** Logs all security-related events
- **Location:** View logs in **Extensions → MAS Security → Security Logs**

## Advanced Configuration

### Custom Templates

You can customize the module's display by editing template files:

1. Navigate to your CMSMS templates directory
2. Locate MAS_Security template files
3. Edit templates to match your site's design
4. **Note:** Backup templates before editing

### Database Configuration

The module uses CMSMS's database connection automatically. No additional database configuration is required.

### File Permissions

Ensure proper file permissions:

- **Modules directory:** Readable by web server
- **Logs directory:** Writable by web server (if custom logging is used)
- **Data files:** Writable by web server (for acknowledgments data)

## Configuration Best Practices

1. **Use Dedicated Security Email:**
   - Create `security@yourdomain.com` email address
   - Monitor this email regularly
   - Set up email forwarding if needed

2. **Set Appropriate Rate Limits:**
   - Balance between security and usability
   - Monitor logs to adjust if needed
   - Consider your site's traffic patterns

3. **Regular Review:**
   - Review security logs weekly
   - Check vulnerability reports promptly
   - Update acknowledgments regularly

4. **Keep Module Updated:**
   - Check for module updates regularly
   - Review changelog for new features
   - Test updates in staging environment first

## Troubleshooting Configuration

### Email Not Sending

1. Verify CMSMS email configuration
2. Check security email address is correct
3. Review server mail logs
4. Test with a simple email first

### Domain Detection Issues

1. Verify CMSMS `root_url` setting is correct
2. Check HTTP_HOST server variable
3. Manually set domain if auto-detection fails

### Rate Limiting Too Strict/Loose

1. Adjust rate limit values in settings
2. Monitor security logs for patterns
3. Adjust based on legitimate traffic patterns

## Related Guides

- [Installation Guide](installation.md) - Initial setup
- [Usage Guide](usage.md) - Using module features
- [Security Guide](security.md) - Security features details
- [Troubleshooting Guide](troubleshooting.md) - Common issues

## Support

For configuration assistance:

- Review the [Troubleshooting Guide](troubleshooting.md)
- Check module documentation
- Contact support: info [at] newstargeted [dot] com

