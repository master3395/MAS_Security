# Development Guide

This guide is for developers who want to contribute to or extend the MAS Security module.

## Module Structure

### Directory Structure

```
MAS_Security/
├── action.acknowledgments.php
├── action.adminsavesettings.php
├── action.default.php
├── action.vdp.php
├── action.admin.php
├── function.admin_acknowledgments.php
├── function.admin_default.php
├── function.admin_reports.php
├── function.admin_settings.php
├── function.admin_logs.php
├── function.vdp_submit.php
├── function.rate_limit.php
├── function.security_log.php
├── function.email_notification.php
├── templates/
│   ├── vdp.tpl
│   ├── acknowledgments.tpl
│   └── admin_*.tpl
├── lang/
│   └── en_US.php
├── acknowledgments-data.php
└── moduleinfo.php
```

### Key Files

**Action Files:**
- Handle public-facing module actions
- Process form submissions
- Display templates

**Function Files:**
- Contain business logic
- Handle security features
- Process data

**Templates:**
- Smarty templates for display
- Separate templates for each action
- Admin interface templates

## Development Requirements

### Environment

- **PHP:** 7.4 - 8.6
- **CMSMS:** 2.2.0 or higher
- **Database:** MySQL/MariaDB (via CMSMS)
- **Server:** Apache, Nginx, or LiteSpeed

### Tools

- Code editor with PHP syntax support
- Git for version control
- Local CMSMS installation for testing
- Browser developer tools

## Coding Standards

### PHP Standards

- Follow PSR-12 coding standards
- Use meaningful variable names
- Add comments for complex logic
- Keep functions focused and small
- Maximum 500 lines per file (split into modules if needed)

### Security Standards

- **Always sanitize input:** Use `htmlspecialchars()`, `filter_var()`, etc.
- **Always validate input:** Check format, length, type
- **Use prepared statements:** For all database queries
- **Escape output:** When displaying user data
- **CSRF protection:** On all forms
- **Rate limiting:** On all user submissions
- **Error handling:** Never expose sensitive information

### CMSMS Standards

- Follow CMSMS module development guidelines
- Use CMSMS API functions
- Leverage CMSMS templating (Smarty)
- Use CMSMS language system
- Follow CMSMS naming conventions

## Key Functions

### Rate Limiting

**File:** `function.rate_limit.php`

**Purpose:** Prevent abuse by limiting submissions per IP

**Usage:**
```php
if (!rate_limit_check($ip_address, $limit, $window)) {
    // Rate limit exceeded
    return false;
}
```

### Security Logging

**File:** `function.security_log.php`

**Purpose:** Log security events for auditing

**Usage:**
```php
security_log('event_type', 'description', $additional_data);
```

### Email Notifications

**File:** `function.email_notification.php`

**Purpose:** Send security email notifications

**Usage:**
```php
send_security_notification($to, $subject, $message, $data);
```

### Input Sanitization

**Purpose:** Sanitize all user input

**Usage:**
```php
$clean_input = sanitize_input($user_input);
```

## Extending the Module

### Adding New Actions

1. Create action file: `action.newaction.php`
2. Add template: `templates/newaction.tpl`
3. Update module info if needed
4. Document in help text

### Adding New Features

1. Create function file: `function.new_feature.php`
2. Add to appropriate action/function
3. Update templates if needed
4. Add admin interface if required
5. Update documentation

### Custom Templates

1. Copy template from `templates/` directory
2. Modify as needed
3. Place in your theme's template directory
4. CMSMS will use your custom template

## Testing

### Testing Checklist

- [ ] Install module successfully
- [ ] All actions display correctly
- [ ] Forms submit properly
- [ ] Email notifications work
- [ ] Rate limiting functions
- [ ] CSRF protection works
- [ ] Admin interface accessible
- [ ] Acknowledgments editable
- [ ] Security logs working
- [ ] No PHP errors or warnings
- [ ] Works on different PHP versions
- [ ] Works on different CMSMS versions

### Testing Environment

- Test on multiple PHP versions (7.4, 8.0, 8.1, 8.2, 8.3, 8.4, 8.5, 8.6)
- Test on different CMSMS versions (2.2+)
- Test on different servers (Apache, Nginx, LiteSpeed)
- Test with different configurations

## Contributing

### Before Contributing

1. Review existing code structure
2. Check coding standards
3. Understand security requirements
4. Test your changes thoroughly

### Contribution Process

1. **Fork Repository:**
   - Create your fork
   - Clone to local machine

2. **Create Branch:**
   - Create feature branch
   - Use descriptive branch name

3. **Make Changes:**
   - Follow coding standards
   - Add comments where needed
   - Test thoroughly

4. **Commit Changes:**
   - Write clear commit messages
   - One logical change per commit
   - Reference issues if applicable

5. **Submit Pull Request:**
   - Describe changes clearly
   - Explain why changes were made
   - Reference any related issues

### Code Review

All contributions will be reviewed for:

- Code quality and standards
- Security best practices
- Functionality and testing
- Documentation updates
- Compatibility

## Security Considerations

### For Developers

- **Never commit secrets:** No passwords, API keys, etc.
- **Sanitize all input:** Always validate and sanitize
- **Escape all output:** Prevent XSS attacks
- **Use prepared statements:** Prevent SQL injection
- **Test security features:** Verify protections work
- **Review code:** Have security-focused review

### Reporting Security Issues

If you find a security vulnerability:

1. **Do NOT** create a public issue
2. **Do NOT** disclose publicly
3. Contact: info [at] newstargeted [dot] com
4. Provide detailed information
5. Allow time for fix before disclosure

## Documentation

### Updating Documentation

When adding features:

1. Update relevant guide files
2. Update module help text
3. Update README if needed
4. Add examples if applicable
5. Update changelog

### Documentation Standards

- Clear and concise
- Include examples
- Cover all use cases
- Keep up to date
- Follow markdown standards

## Version Control

### Git Workflow

- Use meaningful commit messages
- One feature per branch
- Keep branches up to date
- Clean up merged branches

### Version Numbering

Follow semantic versioning:
- **Major:** Breaking changes
- **Minor:** New features (backward compatible)
- **Patch:** Bug fixes

### Release Process

1. Update version numbers
2. Update changelog
3. Create release tag
4. Build release package
5. Create GitHub release
6. Update documentation

## Resources

### CMSMS Documentation

- [CMSMS Developer Documentation](https://docs.cmsmadesimple.org/)
- [CMSMS Module Development](https://docs.cmsmadesimple.org/development/)
- [CMSMS API Reference](https://docs.cmsmadesimple.org/api/)

### PHP Resources

- [PHP Manual](https://www.php.net/manual/)
- [PSR Standards](https://www.php-fig.org/psr/)

### Security Resources

- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [Security Best Practices](https://cheatsheetseries.owasp.org/)

## Support

For development questions:

- Review CMSMS documentation
- Check module code examples
- Contact: info [at] newstargeted [dot] com

## License

Contributions are welcome and will be licensed under the same MIT License as the module.

---

**Thank you for contributing to MAS Security!**

