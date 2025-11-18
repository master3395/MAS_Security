# MAS Security Module

[![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)](https://github.com/yourusername/MAS_Security/releases)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![CMSMS](https://img.shields.io/badge/CMSMS-2.2%2B-orange.svg)](https://www.cmsmadesimple.org/)

Complete Vulnerability Disclosure Policy (VDP) and Security Acknowledgments system for CMS Made Simple (CMSMS). Provides secure forms for responsible vulnerability reporting, CSRF protection, rate limiting, email notifications, and comprehensive security event logging.

## Quick Start

1. **Download the Module**
   - [Download Latest Release](https://github.com/yourusername/MAS_Security/releases/latest) - Get both ZIP and XML files with one click
   - Or use the [Direct Download](download.html) page

2. **Install via CMSMS Module Manager**
   - Extensions → Module Manager → MAS Security → Install

3. **Follow the [Installation Guide](guides/installation.md)** for detailed setup instructions

## Features

- **Vulnerability Disclosure Policy (VDP)** - Professional VDP page with secure submission form
- **Security Acknowledgments** - Public acknowledgments page to recognize security researchers
- **CSRF Protection** - Built-in CSRF token validation for all form submissions
- **Rate Limiting** - Configurable rate limiting (default: 3 submissions per hour per IP)
- **Email Notifications** - Automatic email alerts to security team on report submission
- **Security Event Logging** - Comprehensive logging of all security-related activities
- **Admin Interface** - Complete admin interface for managing reports and acknowledgments
- **In-Browser Editor** - Edit acknowledgments directly from admin with PHP syntax highlighting
- **Honeypot Protection** - Bot detection via hidden honeypot fields
- **Dynamic Configuration** - Automatically detects domain and admin email settings

## Documentation

Navigate to the appropriate guide for detailed information:

| Guide | Description |
|-------|-------------|
| [Installation Guide](guides/installation.md) | Step-by-step installation and initial setup |
| [Configuration Guide](guides/configuration.md) | Module configuration and settings |
| [Usage Guide](guides/usage.md) | How to use module features and actions |
| [Security Guide](guides/security.md) | Security features and best practices |
| [Acknowledgments Guide](guides/acknowledgments.md) | Managing security acknowledgments |
| [Troubleshooting Guide](guides/troubleshooting.md) | Common issues and solutions |
| [Development Guide](guides/development.md) | For developers and contributors |
| [Releases Guide](guides/releases.md) | How to create and manage GitHub releases |

## Requirements

- **CMSMS Version:** 2.2.0 or higher
- **PHP Version:** 7.4 - 8.6
- **Server:** Apache, Nginx, or LiteSpeed (OpenLiteSpeed/LiteSpeed Enterprise)

## Download

### Option 1: GitHub Releases (Recommended)

Visit the [Releases Page](https://github.com/yourusername/MAS_Security/releases) to download:

- `MAS_Security.zip` - Module installation package
- `MAS_Security-1.0.0.xml` - Module definition file

### Option 2: Direct Download

Use the [download page](download.html) to download both files with a single click.

## Installation

1. Download the latest release files (ZIP and XML)
2. Log in to your CMSMS admin panel
3. Navigate to **Extensions → Module Manager**
4. Click **Upload Module** or use **Install Module**
5. Upload the `MAS_Security-1.0.0.xml` file
6. Follow the [Installation Guide](guides/installation.md) for complete setup

## Support

- **Author:** master3395
- **Email:** info [at] newstargeted [dot] com
- **Website:** [https://newstargeted.com](https://newstargeted.com)

## License

This module is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Changelog

See [CHANGELOG.md](CHANGELOG.md) for version history and changes.

---

**Note:** This module follows security-first development practices. All security features are enabled by default to ensure maximum protection for your CMSMS installation.
