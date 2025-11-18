# Troubleshooting Guide

This guide helps you resolve common issues with the MAS Security module.

## Installation Issues

### Module Won't Install

**Symptoms:**
- Installation fails
- Error messages during installation
- Module doesn't appear in module list

**Solutions:**

1. **Check PHP Version:**
   - Required: PHP 7.4 or higher
   - Check: `phpinfo()` or server control panel
   - Update PHP if version is too old

2. **Verify CMSMS Version:**
   - Required: CMSMS 2.2.0 or higher
   - Check: Admin panel → System Information
   - Update CMSMS if needed

3. **Check File Permissions:**
   - Modules directory must be writable
   - Verify permissions: `chmod 755` or `775` on modules directory
   - Check ownership matches web server user

4. **Verify XML File:**
   - Ensure XML file is not corrupted
   - Re-download from releases if needed
   - Check file size matches expected size

5. **Clear Cache:**
   - Go to **Extensions → Site Admin → Clear Cache**
   - Try installation again

### Installation Incomplete

**Symptoms:**
- Module installs but features don't work
- Missing files or directories

**Solutions:**

1. **Reinstall Module:**
   - Uninstall module first
   - Clear cache
   - Reinstall from XML file

2. **Check File Structure:**
   - Verify all module files are present
   - Check `modules/MAS_Security/` directory
   - Compare with expected file list

## Display Issues

### Pages Not Displaying

**Symptoms:**
- VDP or acknowledgments page shows blank
- Module tag not working
- Error messages on page

**Solutions:**

1. **Verify Module Tag:**
   ```
   {cms_module module='MAS_Security' action='vdp'}
   ```
   - Check spelling: `MAS_Security` (case-sensitive)
   - Verify action name: `vdp` or `acknowledgments`
   - Ensure single quotes are used

2. **Check Page Status:**
   - Verify page is published
   - Check page is not in draft mode
   - Ensure page is active

3. **Clear Cache:**
   - **Extensions → Site Admin → Clear Cache**
   - Refresh browser cache (Ctrl+F5)

4. **Check Module Installation:**
   - Verify module is installed and active
   - Check module appears in module list
   - Reinstall if necessary

### Form Not Submitting

**Symptoms:**
- Form submission fails
- Error messages on submit
- No email notification received

**Solutions:**

1. **Check CSRF Token:**
   - Clear browser cache
   - Try submitting again
   - Check for JavaScript errors in browser console

2. **Verify Rate Limiting:**
   - Check if you've exceeded rate limit
   - Wait for rate limit window to reset
   - Adjust rate limit in settings if needed

3. **Check JavaScript:**
   - Ensure JavaScript is enabled
   - Check browser console for errors
   - Try different browser

4. **Verify Email Configuration:**
   - Check CMSMS email settings
   - Test email functionality
   - Verify security email address

## Email Issues

### Not Receiving Email Notifications

**Symptoms:**
- No email when form is submitted
- Emails going to spam
- Email errors in logs

**Solutions:**

1. **Check Email Settings:**
   - Verify CMSMS email configuration
   - Test email sending from CMSMS
   - Check spam/junk folders

2. **Verify Security Email:**
   - Check security email in module settings
   - Ensure email address is correct
   - Test with different email address

3. **Check Server Mail:**
   - Verify server can send email
   - Check mail server logs
   - Test with simple email first

4. **Email Provider Issues:**
   - Some providers block automated emails
   - Check email provider settings
   - Consider using dedicated email service

### Email Format Issues

**Symptoms:**
- Emails are malformed
- Missing information in emails
- Encoding problems

**Solutions:**

1. **Check Email Template:**
   - Verify email template is correct
   - Check for template errors
   - Review email content format

2. **Character Encoding:**
   - Ensure UTF-8 encoding
   - Check special characters
   - Verify email headers

## Configuration Issues

### Settings Not Saving

**Symptoms:**
- Changes don't persist
- Settings revert to defaults
- Configuration errors

**Solutions:**

1. **Check Permissions:**
   - Verify module directory is writable
   - Check file permissions
   - Ensure web server can write files

2. **Clear Cache:**
   - Clear CMSMS cache
   - Clear browser cache
   - Try saving again

3. **Check for Errors:**
   - Review error logs
   - Check browser console
   - Look for PHP errors

### Auto-Detection Not Working

**Symptoms:**
- Domain not detected correctly
- Email not auto-detected
- Site name incorrect

**Solutions:**

1. **Manual Configuration:**
   - Set values manually in settings
   - Override auto-detection
   - Save settings

2. **Check CMSMS Config:**
   - Verify `root_url` setting
   - Check `sitename` setting
   - Review CMSMS configuration

3. **Server Variables:**
   - Check HTTP_HOST variable
   - Verify server configuration
   - Review PHP settings

## Acknowledgments Issues

### Acknowledgments Not Displaying

**Symptoms:**
- Page shows empty
- No acknowledgments listed
- Error on page

**Solutions:**

1. **Check Data File:**
   - Verify `acknowledgments-data.php` exists
   - Check file permissions
   - Verify file is readable

2. **Verify Data Format:**
   - Check PHP syntax is correct
   - Verify array structure
   - Look for syntax errors

3. **Clear Cache:**
   - Clear CMSMS cache
   - Refresh page
   - Check again

### Can't Edit Acknowledgments

**Symptoms:**
- Editor won't open
- Changes won't save
- Syntax errors

**Solutions:**

1. **Check Permissions:**
   - Verify file is writable
   - Check directory permissions
   - Ensure web server can write

2. **Fix Syntax Errors:**
   - Review PHP syntax
   - Check for missing commas
   - Verify array structure
   - Use syntax highlighting in editor

3. **Browser Issues:**
   - Try different browser
   - Clear browser cache
   - Check JavaScript is enabled

## Security Issues

### Rate Limiting Too Strict

**Symptoms:**
- Legitimate submissions blocked
- Users can't submit forms
- Too many rate limit violations

**Solutions:**

1. **Adjust Rate Limit:**
   - Go to module settings
   - Increase rate limit value
   - Save settings

2. **Review Logs:**
   - Check security logs
   - Identify patterns
   - Adjust accordingly

### CSRF Errors

**Symptoms:**
- Form submissions rejected
- CSRF token errors
- Security warnings

**Solutions:**

1. **Clear Browser Data:**
   - Clear cookies
   - Clear cache
   - Try again

2. **Check Session:**
   - Verify session is working
   - Check session configuration
   - Ensure cookies are enabled

3. **Time Issues:**
   - Check server time is correct
   - Verify timezone settings
   - CSRF tokens expire after time

## Performance Issues

### Slow Loading

**Symptoms:**
- Pages load slowly
- Admin interface is slow
- Timeouts

**Solutions:**

1. **Clear Cache:**
   - Clear CMSMS cache
   - Clear opcode cache if using
   - Refresh

2. **Check Database:**
   - Review database performance
   - Check for slow queries
   - Optimize if needed

3. **Server Resources:**
   - Check server resources
   - Review memory usage
   - Check PHP limits

## Getting Help

### Before Contacting Support

1. **Review Documentation:**
   - Check relevant guides
   - Review this troubleshooting guide
   - Search for similar issues

2. **Check Logs:**
   - Review error logs
   - Check security logs
   - Look for error messages

3. **Test Basic Functionality:**
   - Verify module is installed
   - Check basic features work
   - Test in different browser

### Contacting Support

When contacting support, provide:

- **CMSMS Version:** From system information
- **PHP Version:** From phpinfo or server panel
- **Error Messages:** Exact error messages
- **Steps to Reproduce:** What you did before error
- **Logs:** Relevant log entries
- **Screenshots:** If applicable

**Contact:** info [at] newstargeted [dot] com

## Related Guides

- [Installation Guide](installation.md) - Installation help
- [Configuration Guide](configuration.md) - Configuration issues
- [Usage Guide](usage.md) - Usage questions
- [Security Guide](security.md) - Security concerns

## Common Error Messages

### "Module not found"

**Cause:** Module not installed or name misspelled

**Solution:** Verify module is installed and check module tag spelling

### "Action not found"

**Cause:** Incorrect action name in module tag

**Solution:** Use `action='vdp'` or `action='acknowledgments'`

### "Permission denied"

**Cause:** File permission issues

**Solution:** Check file and directory permissions

### "Syntax error"

**Cause:** PHP syntax error in acknowledgments data

**Solution:** Review and fix PHP syntax in editor

---

**Remember:** Most issues can be resolved by clearing cache and checking basic configuration. Always start with the simplest solutions first.

