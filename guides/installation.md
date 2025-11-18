# Installation Guide

This guide will walk you through installing and setting up the MAS Security module on your CMSMS website.

## Prerequisites

Before installing, ensure you have:

- **CMSMS Version:** 2.2.0 or higher
- **PHP Version:** 7.4 - 8.6
- **Admin Access:** You must be logged in as an administrator

## Step 1: Download the Module

### Option A: GitHub Releases (Recommended)

1. Visit the [GitHub Releases Page](https://github.com/yourusername/MAS_Security/releases)
2. Download the latest release:
   - `MAS_Security.zip` - Module installation package
   - `MAS_Security-1.0.0.xml` - Module definition file

### Option B: Direct Download

1. Use the [download page](download.html) to download both files with a single click

## Step 2: Install via Module Manager

1. Log in to your CMSMS admin panel
2. Navigate to **Extensions → Module Manager**
3. Click **Upload Module** or **Install Module**
4. Upload the `MAS_Security-1.0.0.xml` file
5. Wait for the installation to complete
6. You should see "MAS_Security" appear in your module list

## Step 3: Configure Settings

1. Navigate to **Extensions → MAS Security → Settings** tab
2. Verify the following auto-detected settings:
   - **Security Email:** Automatically detected from admin user or domain
   - **Domain:** Automatically extracted from CMSMS configuration
   - **Site Name:** Uses CMSMS site name or domain
3. Adjust settings if needed:
   - **Rate Limiting:** Default is 3 requests per hour per IP (adjustable)
   - **Donations Tab:** Enable/disable if desired

## Step 4: Create VDP Page

Create a content page for the Vulnerability Disclosure Policy:

1. Go to **Content → Pages → Add New Content**
2. Set the page **Alias** to: `vulnerability-disclosure`
3. Add the following module tag in the page content:
   ```
   {cms_module module='MAS_Security' action='vdp'}
   ```
4. Save and publish the page
5. Your VDP page will be accessible at: `https://yourdomain.com/vulnerability-disclosure`

## Step 5: Create Acknowledgments Page

Create a content page for Security Acknowledgments:

1. Go to **Content → Pages → Add New Content**
2. Set the page **Alias** to: `security-acknowledgments`
3. Add the following module tag in the page content:
   ```
   {cms_module module='MAS_Security' action='acknowledgments'}
   ```
4. Save and publish the page
5. Your acknowledgments page will be accessible at: `https://yourdomain.com/security-acknowledgments`

## Step 6: (Optional) Create security.txt File

For better security researcher discoverability, create a `/security.txt` file:

1. Create or edit the file: `/security.txt` in your website root
2. Add the following content:
   ```
   Contact: mailto:security@yourdomain.com
   Policy: https://yourdomain.com/vulnerability-disclosure
   Acknowledgments: https://yourdomain.com/security-acknowledgments
   ```
3. Replace `yourdomain.com` with your actual domain
4. Replace `security@yourdomain.com` with your security email address

## Step 7: Verify Installation

1. Visit your VDP page to ensure it loads correctly
2. Visit your acknowledgments page to verify it displays
3. Test the VDP form submission (use a test email)
4. Check your security email inbox for notification
5. Verify the admin interface:
   - Go to **Extensions → MAS Security**
   - Check that all tabs are accessible (Settings, Vulnerability Reports, Acknowledgments, Security Logs)

## Troubleshooting

If you encounter issues during installation:

1. **Module won't install:**
   - Verify PHP version is 7.4 or higher
   - Check file permissions on the modules directory
   - Ensure CMSMS version is 2.2.0 or higher

2. **Pages not displaying:**
   - Verify the module tag syntax is correct
   - Check that the page is published
   - Clear CMSMS cache: **Extensions → Site Admin → Clear Cache**

3. **Email notifications not working:**
   - Verify email settings in CMSMS configuration
   - Check spam/junk folders
   - Review security email setting in module settings

For more detailed troubleshooting, see the [Troubleshooting Guide](troubleshooting.md).

## Next Steps

After installation:

1. Review the [Configuration Guide](configuration.md) for advanced settings
2. Read the [Usage Guide](usage.md) to learn how to use all features
3. Check the [Security Guide](security.md) to understand security features
4. Learn about [Managing Acknowledgments](acknowledgments.md)

## Support

If you need help with installation:

- Check the [Troubleshooting Guide](troubleshooting.md)
- Review the [Usage Guide](usage.md)
- Contact support: info [at] newstargeted [dot] com

