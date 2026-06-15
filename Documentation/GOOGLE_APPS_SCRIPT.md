# Google Apps Script Setup

Google Apps Script automatically triggers GitHub Actions whenever a new unread email forwarded from Outlook is found.

---

## Step 1

Open:

https://script.google.com

Create:

```text
New Project
```

Rename:

```text
Placement Tracker Trigger
```

---

## Step 2

Replace `Code.gs` with:

```javascript
// Paste the script from repository
```

---

## Step 3

Replace:

```text
YOUR_GITHUB_PAT
```

with your GitHub Personal Access Token.

Replace:

```text
YOUR_OUTLOOK_EMAIL
```

with:

```text
example@outlook.com
```

---

## Step 4

Click:

```text
Run
```

Allow:

* Gmail Access
* External Requests

---

## Step 5

Create Trigger:

```text
Function

triggerGithubIfUnreadExists

↓

Event Source

Time Driven

↓

Minutes Timer

↓

Every 30 Minutes
```

---

## Workflow

```text
Every 30 Minutes

↓

Google Apps Script

↓

Search Gmail

↓

Unread Email Found

↓

Trigger GitHub Actions

↓

main.py

↓

Gemini AI

↓

Notion
```

---

## Useful Links

Apps Script:

https://script.google.com

Documentation:

https://developers.google.com/apps-script

Triggers:

https://developers.google.com/apps-script/guides/triggers
