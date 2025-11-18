# Acknowledgments Guide

This guide explains how to manage security acknowledgments in the MAS Security module.

## Overview

The Security Acknowledgments page publicly recognizes security researchers who have responsibly disclosed vulnerabilities. This encourages responsible disclosure and builds trust with the security community.

## Accessing Acknowledgments

**Public Page:**
- URL: `https://yourdomain.com/security-acknowledgments`
- Displays all acknowledgments in a user-friendly format

**Admin Interface:**
- Navigate to **Extensions → MAS Security → Acknowledgments** tab
- View, edit, and manage acknowledgments

## Adding Acknowledgments

### Method 1: Admin Interface (Recommended)

**Steps:**

1. Go to **Extensions → MAS Security → Acknowledgments**
2. Click **"Edit Acknowledgments"** button
3. The in-browser editor opens with PHP syntax highlighting
4. Add your acknowledgment entry following the format
5. Click **Save** - syntax is validated automatically
6. Changes appear on the public page immediately

**Advantages:**
- Syntax highlighting helps prevent errors
- Automatic syntax validation
- No file editing required
- Immediate updates

### Method 2: Direct File Editing

**Steps:**

1. Edit the file: `modules/MAS_Security/acknowledgments-data.php`
2. Add entries to the `$acknowledgments` array
3. Follow the data structure format
4. Save the file
5. Changes appear on public page

**Note:** Use this method only if you're comfortable editing PHP files directly.

## Data Structure Format

Acknowledgments are stored in a nested array structure:

```php
$acknowledgments = array(
    '2025' => array(
        array(
            'name' => 'Researcher Name or Handle',
            'vulnerability' => 'Brief vulnerability description',
            'date' => '2025-01-15',
            'disclose' => 'coordinated',
            'credit_link' => 'https://example.com/researcher-profile'
        ),
        array(
            'name' => 'Another Researcher',
            'vulnerability' => 'XSS in contact form',
            'date' => '2025-02-20',
            'disclose' => 'public',
            'credit_link' => null
        ),
    ),
    '2024' => array(
        // ... more entries
    ),
);
```

### Field Descriptions

**`name`** (required)
- Researcher's name or handle
- Example: `'Security Researcher'` or `'@researcher_handle'`

**`vulnerability`** (required)
- Brief description of the vulnerability
- Keep it concise but descriptive
- Example: `'Cross-Site Scripting (XSS) in contact form'`

**`date`** (required)
- Date when vulnerability was disclosed/resolved
- Format: `'YYYY-MM-DD'`
- Example: `'2025-01-15'`

**`disclose`** (required)
- Disclosure type, one of:
  - `'public'` - Publicly disclosed
  - `'private'` - Privately disclosed
  - `'coordinated'` - Coordinated disclosure
- Example: `'coordinated'`

**`credit_link`** (optional)
- URL to researcher's profile, website, or social media
- Use `null` if no link available
- Example: `'https://twitter.com/researcher'` or `null`

## Best Practices

### When to Add Acknowledgments

Add acknowledgments when:

- Vulnerability has been fixed and verified
- Researcher has given permission (if required)
- You want to recognize their contribution
- Disclosure timeline allows public acknowledgment

### What to Include

**Do Include:**
- Researcher name or handle
- Brief, non-sensitive vulnerability description
- Disclosure date
- Appropriate disclosure type
- Credit link if researcher provides one

**Don't Include:**
- Sensitive technical details
- Exploit code or proof of concepts
- Internal remediation details
- Personal information without permission

### Disclosure Types

**Public:**
- Vulnerability was publicly disclosed
- No coordination required
- Already known to public

**Private:**
- Researcher disclosed privately
- You fixed before public disclosure
- Researcher requested private acknowledgment

**Coordinated:**
- Worked together on disclosure timeline
- Agreed on public disclosure date
- Best practice for responsible disclosure

### Organization Tips

1. **Chronological Order:**
   - List newest entries first within each year
   - Years in descending order (newest first)

2. **Grouping:**
   - Group by year for easy navigation
   - Consider grouping by severity if desired

3. **Consistency:**
   - Use consistent formatting
   - Follow the same structure for all entries
   - Keep descriptions concise

## Editing Acknowledgments

### Using Admin Interface

1. Go to **Extensions → MAS Security → Acknowledgments**
2. Click **"Edit Acknowledgments"**
3. Make your changes in the editor
4. Syntax highlighting helps identify structure
5. Click **Save**
6. Syntax is validated - fix any errors if shown
7. Changes are live immediately

### Common Edits

**Adding a New Entry:**
```php
array(
    'name' => 'New Researcher',
    'vulnerability' => 'Description',
    'date' => '2025-03-01',
    'disclose' => 'coordinated',
    'credit_link' => null
),
```

**Updating an Entry:**
- Find the entry in the array
- Modify the fields as needed
- Save changes

**Removing an Entry:**
- Delete the entire array entry
- Ensure proper comma placement
- Save changes

## Display on Public Page

The public acknowledgments page displays:

- **Total Count:** Number of acknowledgments
- **By Year:** Grouped by year (newest first)
- **Researcher Info:** Name and optional credit link
- **Vulnerability:** Brief description
- **Date:** Disclosure date
- **Type:** Disclosure type indicator

**Formatting:**
- Clean, readable layout
- Responsive design
- Easy to scan and navigate

## Examples

### Example 1: Basic Acknowledgment

```php
array(
    'name' => 'Security Researcher',
    'vulnerability' => 'SQL Injection in user profile',
    'date' => '2025-01-15',
    'disclose' => 'coordinated',
    'credit_link' => null
),
```

### Example 2: With Credit Link

```php
array(
    'name' => '@security_expert',
    'vulnerability' => 'XSS vulnerability in search function',
    'date' => '2025-02-20',
    'disclose' => 'coordinated',
    'credit_link' => 'https://twitter.com/security_expert'
),
```

### Example 3: Public Disclosure

```php
array(
    'name' => 'Bug Hunter',
    'vulnerability' => 'CSRF in admin panel',
    'date' => '2025-03-10',
    'disclose' => 'public',
    'credit_link' => 'https://bugbounty.example.com/hunter'
),
```

## Troubleshooting

### Syntax Errors

**Problem:** PHP syntax error when saving

**Solution:**
- Check for missing commas
- Verify array structure
- Ensure proper quotes (single or double, matching)
- Check for typos in field names
- Use syntax highlighting in editor

### Entry Not Appearing

**Problem:** Added entry but not showing on public page

**Solution:**
- Clear CMSMS cache
- Verify entry is in correct year array
- Check for syntax errors
- Ensure page is published
- Verify module tag is correct

### Formatting Issues

**Problem:** Display looks incorrect

**Solution:**
- Check data structure format
- Verify all required fields are present
- Review template if customizing
- Clear cache

## Related Guides

- [Installation Guide](installation.md) - Setting up acknowledgments page
- [Usage Guide](usage.md) - Using the admin interface
- [Configuration Guide](configuration.md) - Module configuration
- [Troubleshooting Guide](troubleshooting.md) - Solving issues

## Support

For help with acknowledgments:

- Review this guide
- Check the [Usage Guide](usage.md)
- Contact support: info [at] newstargeted [dot] com

