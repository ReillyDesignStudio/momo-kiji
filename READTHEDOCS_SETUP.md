# ReadTheDocs Setup Guide

The documentation is now configured and pushed to GitHub. To enable it at https://momo-kiji.readthedocs.io, follow these steps:

## Step 1: Import the Project on ReadTheDocs

1. Go to: https://readthedocs.org
2. Sign in with your GitHub account (or create a ReadTheDocs account)
3. Click **Import a Project**
4. Select **Import Manually**
5. Fill in:
   - **Project name:** momo-kiji
   - **Project URL:** https://github.com/ReillyDesignStudio/momo-kiji
   - **Repository type:** Git
   - **Documentation type:** Sphinx documentation

6. Click **Create Project**

## Step 2: Configure Build Settings

1. Go to **Admin** → **Advanced Settings**
2. Set:
   - **Python version:** 3.11
   - **Use system packages:** OFF
   - **Install your project:** ✓ Checked

3. Click **Save**

## Step 3: Trigger Initial Build

1. Go to **Builds**
2. Click **Build Version** → Select **latest**
3. Wait for build to complete (usually 2-3 minutes)
4. Check the build log for errors

## Step 4: Custom Domain (Optional)

To use `momo-kiji.readthedocs.io` instead of the default:

1. Go to **Admin** → **Domains**
2. Add custom domain if needed
3. ReadTheDocs usually auto-assigns `momo-kiji.readthedocs.io`

## Step 5: Configure GitHub Integration

To auto-build on GitHub push:

1. Go to **Admin** → **Integrations**
2. Click **Add Integration**
3. Choose **GitHub incoming webhook**
4. Authorize with GitHub
5. Select the `momo-kiji` repository
6. Save

Now documentation rebuilds automatically whenever you push to GitHub!

## Step 6: Add Build Badge (Optional)

Add to README.md:

```markdown
[![Documentation Status](https://readthedocs.org/projects/momo-kiji/badge/?version=latest)](https://momo-kiji.readthedocs.io/?badge=latest)
```

## Verification

Once live, you should see:

- Documentation at: https://momo-kiji.readthedocs.io
- Build history showing successful builds
- Auto-rebuild triggering on GitHub pushes

## Troubleshooting

### Build Fails

Check the build logs for errors:

1. **Missing dependencies?** Update `requirements.txt`
2. **Python version issue?** Change in Advanced Settings
3. **Import errors?** Ensure `conf.py` paths are correct

Common fixes:

```bash
# Rebuild locally to test
cd docs
make clean
make html
```

### Documentation Not Updating

1. Check **Builds** tab for failed builds
2. Manually trigger a rebuild
3. Check GitHub webhook is configured

### Custom Domain Not Working

1. Verify domain is added in ReadTheDocs Admin
2. Check DNS CNAME records if using custom domain
3. Wait up to 24 hours for DNS propagation

## What's Documented

The documentation includes:

- **Introduction** — What momo-kiji is and why it exists
- **Installation** — Setup for development
- **Quickstart** — Compile your first model in 5 minutes
- **How It Works** (stub, to be expanded)
- **API Reference** (stub, to be expanded)
- **Examples** (stub, to be expanded)
- **Contributing** — How to contribute
- **Community** — Discord, code of conduct
- **Security** — Reporting vulnerabilities

## Future Enhancements

As development continues, add:

- API reference (auto-generated from docstrings)
- Architecture deep-dive
- Research papers and findings
- Performance benchmarks
- Optimization guides
- Common patterns and use cases

## Status

✅ **Documentation structure:** Complete
✅ **ReadTheDocs configuration:** Ready
⏳ **ReadTheDocs import:** Manual (follow steps above)
⏳ **Auto-build:** Pending GitHub integration setup
⏳ **Full documentation:** Evolving with Phase 2 development

## Questions?

- Check ReadTheDocs docs: https://docs.readthedocs.io
- Ask in Discord: https://discord.gg/DHRbKbzr
- Open GitHub issue: https://github.com/ReillyDesignStudio/momo-kiji/issues
