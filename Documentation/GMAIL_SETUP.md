# Gmail Setup

This project uses Gmail as the automation mailbox.

## Why Gmail?

The original placement emails are received in Outlook.

These emails are forwarded to Gmail because:

* Gmail API is easier to use.
* Google OAuth setup is straightforward.
* Google Apps Script integrates directly with Gmail.
* Gmail search filters make automation easier.

---

## Step 1

Open Outlook.

Create a forwarding rule.

Forward all placement emails to:

```text
your-personal-gmail@gmail.com
```

---

## Step 2

Verify that forwarded emails arrive in Gmail.

---

## Step 3

Keep forwarded emails unread.

The automation searches:

```text
is:unread from:YOUR_OUTLOOK_EMAIL
```

Only unread emails trigger GitHub Actions.

---

## Useful Links

Gmail API:

https://developers.google.com/gmail/api

Python Quickstart:

https://developers.google.com/gmail/api/quickstart/python
