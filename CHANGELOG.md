# Changelog

All notable changes to the MAS Security module will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2025-11-18

### Added

#### Vulnerability Disclosure Policy
- Professional VDP page with secure submission form
- Secure form processing with comprehensive validation
- Public-facing vulnerability disclosure policy page

#### Security Acknowledgments
- Public acknowledgments page to recognize security researchers
- Display acknowledgments by year (newest first)
- Support for researcher names, vulnerability descriptions, dates, and disclosure types
- Optional credit links to researcher profiles

#### Secure Form Processing
- CSRF protection for all form submissions
- Rate limiting (default: 3 submissions per hour per IP)
- Input validation and sanitization
- Honeypot fields for bot detection

#### Email Notifications
- Automatic email alerts to security team on report submission
- Configurable security email address
- Email notifications include full report details

#### Security Event Logging
- Comprehensive logging of all security-related activities
- Timestamp and IP address tracking
- Admin interface for viewing logs
- Event categorization

#### Admin Interface
- Complete admin interface for managing reports, acknowledgments, and settings
- Vulnerability Reports tab for viewing and managing submissions
- Acknowledgments tab with in-browser editor
- Settings tab for configuration
- Security Logs tab for event monitoring

#### Report Management
- View all vulnerability reports
- Filter reports by status (all/resolved/unresolved)
- Mark reports as resolved
- View detailed report information

#### In-Browser Editor
- Edit acknowledgments directly from admin interface
- PHP syntax highlighting
- Automatic syntax validation
- Immediate updates to public page

#### Dynamic Configuration
- Automatically detects domain from CMSMS configuration
- Auto-detects admin email address
- Constructs security email if not found
- Uses CMSMS site name or domain

#### Portable Design
- Module can be easily exported and installed on any CMSMS site
- No hardcoded paths or dependencies
- Clean URL support without .php extensions

#### Security Best Practices
- Input sanitization on all user input
- Secure email sending via CMSMS mailer
- Event logging for security auditing
- Comprehensive error handling

#### Additional Features
- Optional donations tab to support module development
- PHP 7.4-8.6 compatibility
- CMSMS 2.2+ full integration
- Smart templating with Smarty
- Clean, responsive design

### Technical Details

- **PHP Compatibility:** 7.4, 8.0, 8.1, 8.2, 8.3, 8.4, 8.5, 8.6
- **CMSMS Compatibility:** 2.2.0 and higher
- **Database:** Uses CMSMS database connection
- **Templating:** Smarty templates for all displays
- **Security:** CSRF tokens, rate limiting, input sanitization, honeypot protection

### Initial Release

This is the initial release of the MAS Security module, providing a complete Vulnerability Disclosure Policy and Security Acknowledgments system for CMS Made Simple.

---

## Release Notes Format

Future releases will follow this format:

### [Version] - YYYY-MM-DD

#### Added
- New features

#### Changed
- Changes to existing functionality

#### Deprecated
- Features that will be removed in future versions

#### Removed
- Removed features

#### Fixed
- Bug fixes

#### Security
- Security improvements and fixes

---

For detailed information about each version, see the [GitHub Releases](https://github.com/yourusername/MAS_Security/releases) page.

