# Notion Setup

The project stores placement data inside a Notion Database.

---

## Step 1

Create a Notion Database.

Suggested columns:

* Company
* Role
* CTC
* Eligibility
* Deadline
* Location
* Category
* Status

---

## Step 2

Create an Internal Integration.

Open:

https://www.notion.so/profile/integrations

Create:

```text
New Integration
```

Copy:

```text
NOTION_TOKEN
```

---

## Step 3

Open your database.

Click:

```text
Share

↓

Invite

↓

Select Integration
```

---

## Step 4

Get Database ID.

Add:

```env
NOTION_TOKEN=

DATABASE_ID=
```

to:

```text
.env
```

---

## Useful Links

Notion API:

https://developers.notion.com

API Reference:

https://developers.notion.com/reference/intro

Integrations:

https://www.notion.so/profile/integrations
