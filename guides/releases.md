# Releases Guide

This guide explains how to create and manage GitHub releases for the MAS Security module.

## Overview

GitHub Releases allow you to package and distribute your module with both the ZIP and XML files, making it easy for users to download and install.

## Prerequisites

- GitHub repository set up
- Both `MAS_Security.zip` and `MAS_Security-1.0.0.xml` files ready
- Git installed and configured
- GitHub account with repository access

## Creating a Release

### Step 1: Prepare Release Files

Ensure you have:

1. **ZIP File:** `MAS_Security.zip`
   - Contains all module files
   - Properly structured for CMSMS installation
   - Tested and verified

2. **XML File:** `MAS_Security-1.0.0.xml`
   - Module definition file
   - Version number matches release
   - All metadata correct

### Step 2: Update Version Information

Before creating a release:

1. **Update Version Numbers:**
   - Update version in XML file
   - Update version in module code if needed
   - Update version in README.md

2. **Update Changelog:**
   - Add new version entry to CHANGELOG.md
   - Document all changes
   - Include date and author

3. **Commit Changes:**
   ```bash
   git add .
   git commit -m "Prepare release v1.0.0"
   git push
   ```

### Step 3: Create Git Tag

Tag the release in Git:

```bash
# Create annotated tag
git tag -a v1.0.0 -m "Release version 1.0.0"

# Push tag to GitHub
git push origin v1.0.0
```

**Tag Naming Convention:**
- Use semantic versioning: `v1.0.0`, `v1.1.0`, `v2.0.0`
- Match version in XML file
- Use `v` prefix

### Step 4: Create GitHub Release

1. **Navigate to Releases:**
   - Go to your GitHub repository
   - Click **"Releases"** in the right sidebar
   - Or go to: `https://github.com/yourusername/MAS_Security/releases`

2. **Create New Release:**
   - Click **"Draft a new release"** or **"Create a new release"**
   - Or click **"Tags"** and find your tag, then click **"Add release notes"**

3. **Fill Release Information:**
   - **Tag:** Select your tag (e.g., `v1.0.0`)
   - **Title:** `MAS Security v1.0.0` or `Release v1.0.0`
   - **Description:** Add release notes from CHANGELOG.md

4. **Attach Release Assets:**
   - Click **"Attach binaries"** or drag and drop files
   - Attach `MAS_Security.zip`
   - Attach `MAS_Security-1.0.0.xml`
   - Both files will be available for download

5. **Publish Release:**
   - Click **"Publish release"**
   - Release is now live and downloadable

## Release Notes Template

Use this template for release notes:

```markdown
## MAS Security v1.0.0

### Features
- Feature 1 description
- Feature 2 description

### Improvements
- Improvement 1
- Improvement 2

### Bug Fixes
- Fixed issue 1
- Fixed issue 2

### Installation
1. Download `MAS_Security.zip` and `MAS_Security-1.0.0.xml`
2. Install via CMSMS Module Manager
3. Follow the [Installation Guide](https://github.com/yourusername/MAS_Security/blob/main/guides/installation.md)

### Documentation
- [Installation Guide](https://github.com/yourusername/MAS_Security/blob/main/guides/installation.md)
- [Configuration Guide](https://github.com/yourusername/MAS_Security/blob/main/guides/configuration.md)
- [Usage Guide](https://github.com/yourusername/MAS_Security/blob/main/guides/usage.md)

### Requirements
- CMSMS 2.2.0+
- PHP 7.4-8.6

### Support
For support, contact: info [at] newstargeted [dot] com
```

## Release Best Practices

### Version Numbering

Follow semantic versioning:

- **Major (X.0.0):** Breaking changes
- **Minor (0.X.0):** New features, backward compatible
- **Patch (0.0.X):** Bug fixes, backward compatible

**Examples:**
- `1.0.0` - Initial release
- `1.0.1` - Bug fix release
- `1.1.0` - New feature release
- `2.0.0` - Major update with breaking changes

### Release Frequency

- **Major Releases:** As needed for breaking changes
- **Minor Releases:** When adding new features
- **Patch Releases:** As soon as bugs are fixed

### Testing Before Release

Always test before releasing:

- [ ] Install from ZIP file
- [ ] Install from XML file
- [ ] All features work correctly
- [ ] No PHP errors or warnings
- [ ] Documentation is up to date
- [ ] Version numbers are consistent
- [ ] Files are properly structured

### Release Checklist

Before publishing:

- [ ] Version numbers updated everywhere
- [ ] Changelog updated
- [ ] Files tested and verified
- [ ] Documentation updated
- [ ] Release notes written
- [ ] Git tag created
- [ ] Files attached to release
- [ ] Release published

## Managing Releases

### Updating a Release

If you need to update a release:

1. **Fix the Issue:**
   - Make necessary changes
   - Update version number
   - Test thoroughly

2. **Create New Release:**
   - Follow same process
   - Use new version number
   - Document what was fixed

**Note:** Don't modify existing releases. Create a new release instead.

### Deprecating a Release

If a release has security issues:

1. **Mark as Deprecated:**
   - Update release notes
   - Add deprecation notice
   - Recommend upgrading

2. **Create New Release:**
   - Fix security issues
   - Release new version
   - Notify users to upgrade

## Download Options

Users can download releases in two ways:

### Option 1: GitHub Releases Page

1. Visit releases page
2. Click on release version
3. Download both files individually
4. Or download source code zip

### Option 2: Direct Download Script

Use the `download.html` page to download both files with one click.

## Automation (Optional)

### GitHub Actions

You can automate releases with GitHub Actions:

1. Create `.github/workflows/release.yml`
2. Automate version bumping
3. Automate file packaging
4. Automate release creation

### Scripts

Create scripts to:

- Update version numbers
- Package ZIP file
- Generate changelog
- Create git tags

## Troubleshooting

### Release Not Appearing

**Problem:** Release created but not visible

**Solution:**
- Check if release is published (not draft)
- Verify tag was pushed to GitHub
- Refresh the releases page

### Files Not Attaching

**Problem:** Can't attach files to release

**Solution:**
- Check file sizes (GitHub has limits)
- Verify file formats are correct
- Try uploading one at a time
- Check browser compatibility

### Version Mismatch

**Problem:** Version in XML doesn't match release

**Solution:**
- Update XML file version
- Update all version references
- Create new release with correct version

## Related Guides

- [Installation Guide](installation.md) - For users installing from releases
- [Development Guide](development.md) - For developers creating releases
- [Configuration Guide](configuration.md) - Module configuration

## Support

For release-related questions:

- Review GitHub documentation
- Check this guide
- Contact: info [at] newstargeted [dot] com

---

**Remember:** Always test releases thoroughly before publishing. Once published, releases are public and users will download them.

