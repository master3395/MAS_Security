# Usage Guide

This guide explains how to use all features of the MAS Security module.

## Module Actions

The module provides several actions that can be used in content pages:

### Vulnerability Disclosure Policy (VDP)

**Action:** `vdp`

**Usage:**
```
{cms_module module='MAS_Security' action='vdp'}
```

**Purpose:** Displays the Vulnerability Disclosure Policy page with a secure submission form.

**Page Setup:**
1. Create a content page with alias: `vulnerability-disclosure`
2. Add the module tag above
3. Publish the page

**Features:**
- Secure form with CSRF protection
- Rate limiting (3 submissions per hour per IP)
- Input validation and sanitization
- Honeypot bot protection
- Email notification to security team
- Automatic logging of submissions

### Security Acknowledgments

**Action:** `acknowledgments`

**Usage:**
```
{cms_module module='MAS_Security' action='acknowledgments'}
```

**Purpose:** Displays a public page listing security researchers who have responsibly disclosed vulnerabilities.

**Page Setup:**
1. Create a content page with alias: `security-acknowledgments`
2. Add the module tag above
3. Publish the page

**Display:**
- Lists acknowledgments by year (newest first)
- Shows researcher name/handle
- Displays vulnerability description
- Shows disclosure date
- Indicates disclosure type (public/private/coordinated)
- Optional credit links to researcher profiles

## Admin Interface

Access the admin interface via **Extensions → MAS Security**

### Settings Tab

Configure module settings:

- **Security Email:** Email address for vulnerability reports
- **Rate Limiting:** Adjust submission rate limits
- **Donations:** Enable/disable donations tab
- **Domain/Site Name:** Auto-detected, can be overridden

### Vulnerability Reports Tab

View and manage vulnerability reports:

**Features:**
- **View All Reports:** See all submitted vulnerability reports
- **Filter Reports:** Filter by status (all/resolved/unresolved)
- **Mark as Resolved:** Update report status when vulnerability is fixed
- **View Details:** See full report information including:
  - Reporter information
  - Vulnerability description
  - Submission timestamp
  - IP address
  - Status

**Workflow:**
1. Review new reports regularly
2. Investigate reported vulnerabilities
3. Mark as resolved when fixed
4. Add to acknowledgments if appropriate

### Acknowledgments Tab

Manage security acknowledgments:

**Features:**
- **View Acknowledgments:** See all current acknowledgments
- **Edit Acknowledgments:** Use in-browser editor with PHP syntax highlighting
- **Add New Entries:** Add acknowledgments directly from admin
- **Validate Syntax:** PHP syntax is validated before saving

**Editing Acknowledgments:**

1. Click **"Edit Acknowledgments"** button
2. Edit the PHP array structure in the editor
3. Syntax highlighting helps with formatting
4. Click **Save** - syntax is validated automatically
5. Changes appear on public acknowledgments page immediately

**Data Format:**
```php
$acknowledgments = array(
    '2025' => array(
        array(
            'name' => 'Researcher Name or Handle',
            'vulnerability' => 'Brief description',
            'date' => 'YYYY-MM-DD',
            'disclose' => 'public'|'private'|'coordinated',
            'credit_link' => 'Optional URL' // or null
        ),
        // ... more entries
    ),
    // ... more years
);
```

### Security Logs Tab

View security event logs:

**Information Logged:**
- Form submissions
- Rate limit violations
- Security events
- Admin actions
- Timestamps and IP addresses

**Use Cases:**
- Monitor for suspicious activity
- Track submission patterns
- Debug issues
- Security auditing

## Managing Vulnerability Reports

### Receiving Reports

When a researcher submits a vulnerability:

1. **Email Notification:** You receive an email with report details
2. **Admin Notification:** Report appears in Vulnerability Reports tab
3. **Log Entry:** Event is logged in Security Logs

### Processing Reports

**Best Practice Workflow:**

1. **Acknowledge Receipt (24 hours):**
   - Respond to researcher via email
   - Confirm receipt of report
   - Set initial timeline expectations

2. **Investigate (1-7 days):**
   - Review and verify the vulnerability
   - Assess severity and impact
   - Plan remediation

3. **Remediate (timeline varies):**
   - Fix the vulnerability
   - Test the fix
   - Deploy to production

4. **Mark as Resolved:**
   - Update report status in admin
   - Notify researcher
   - Add to acknowledgments if appropriate

### Adding to Acknowledgments

After resolving a vulnerability:

1. Go to **Acknowledgments** tab
2. Click **"Edit Acknowledgments"**
3. Add entry following the data format
4. Save changes
5. Entry appears on public page

## Best Practices

### Response Times

- **Initial Response:** Within 24-48 hours
- **Status Updates:** Weekly during investigation
- **Resolution:** As per your VDP timeline

### Communication

- Be professional and courteous
- Thank researchers for responsible disclosure
- Provide clear timelines
- Keep researchers informed of progress

### Recognition

- Always acknowledge researchers who help improve security
- Add to acknowledgments page promptly
- Consider additional recognition (bounties, credits, etc.)

### Security

- Never share sensitive details publicly until fixed
- Coordinate disclosure with researchers
- Follow responsible disclosure timelines
- Keep security logs reviewed

## Common Tasks

### Adding a New Acknowledgment

1. Go to **Extensions → MAS Security → Acknowledgments**
2. Click **"Edit Acknowledgments"**
3. Add new entry to appropriate year array
4. Follow the data format structure
5. Save changes

### Viewing Report Details

1. Go to **Extensions → MAS Security → Vulnerability Reports**
2. Click on a report to view details
3. Review all information
4. Take appropriate action

### Checking Security Logs

1. Go to **Extensions → MAS Security → Security Logs**
2. Review recent events
3. Look for patterns or issues
4. Take action if needed

## Related Guides

- [Installation Guide](installation.md) - Setting up the module
- [Configuration Guide](configuration.md) - Configuring settings
- [Security Guide](security.md) - Security features
- [Acknowledgments Guide](acknowledgments.md) - Managing acknowledgments
- [Troubleshooting Guide](troubleshooting.md) - Solving issues

## Support

For usage questions:

- Review other guides in the documentation
- Check the [Troubleshooting Guide](troubleshooting.md)
- Contact support: info [at] newstargeted [dot] com

