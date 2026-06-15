# GitHub Actions Setup

This project uses GitHub Actions to run automatically in the cloud.

---

## Required Secrets

Open:

```text
Repository

↓

Settings

↓

Secrets and Variables

↓

Actions
```

Create:

### ENV_FILE

Paste contents of:

```text
.env
```

---

### GMAIL_CREDENTIALS

Paste contents of:

```text
credentials.json
```

---

### GMAIL_TOKEN

Paste contents of:

```text
token.json
```

---

## Workflow

The workflow:

* Installs dependencies
* Creates `.env`
* Creates `credentials.json`
* Creates `token.json`
* Runs:

```bash
python main.py
```

---

## Useful Links

GitHub Actions:

https://docs.github.com/en/actions

Workflow Syntax:

https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions

GitHub Secrets:

https://docs.github.com/en/actions/security-guides/using-secrets-in-github-actions

Personal Access Token:

https://github.com/settings/tokens
