# Ando Operations Dashboard

Live operations dashboard for daily prep and delivery metrics.
Hosted on GitHub Pages — no server, no licence, shareable via link.

---

## One-time setup (do this once)

### 1. Create a GitHub account
Go to [github.com](https://github.com) and sign up with your work email.

### 2. Create a new repository
- Click the **+** icon (top right) → **New repository**
- Name it: `ando-dashboard`
- Set to **Public**
- Click **Create repository**

### 3. Upload these files
- Click **Add file → Upload files**
- Drag in the entire `ando-dashboard` folder contents:
  - `index.html`
  - `convert.py`
  - `README.md`
  - `data/` folder (with `2026-06-29.json` inside)
- Click **Commit changes**

### 4. Enable GitHub Pages
- Go to **Settings → Pages**
- Under Source, select: **Deploy from branch**
- Branch: `main` / folder: `/ (root)`
- Click **Save**

Your dashboard will be live at:
`https://YOUR-USERNAME.github.io/ando-dashboard`
(takes ~1 minute to activate)

---

## Daily routine (every morning)

### Step 1 — Convert the CSV
Run this on your computer (requires Python 3):
```
python3 convert.py "Auro_Daily_Prep___Delivery_Metrics.csv"
```
This creates a file like `data/2026-06-30.json`.

### Step 2 — Upload to GitHub
- Go to your repo → `data/` folder
- Click **Add file → Upload files**
- Drop in the new `.json` file
- Click **Commit changes**

### Step 3 — Register the new file
Open `index.html`, find this section near the top of the `<script>` block:
```js
const DATA_FILES = [
  'data/2026-06-29.json',
  // add new lines here
];
```
Add a new line for each new date:
```js
const DATA_FILES = [
  'data/2026-06-29.json',
  'data/2026-06-30.json',
];
```
Commit `index.html` again. Dashboard updates within seconds.

---

## Sharing
Send teammates the URL:
`https://YOUR-USERNAME.github.io/ando-dashboard`

No login required. Works on desktop and mobile.

---

## Flags & thresholds (adjust in index.html)
| Condition | Flag |
|---|---|
| Prep time > 60 min | Red — Prep > 60 min |
| Prep time < 5 min | Red — Prep < 5 min |
| Delivery time < 5 min | Blue — Delivery < 5 min |

---

## Adding more metrics later
When your CSV includes cost-per-trip, order source platform, or cancellation status,
share the updated file and Claude will extend the dashboard automatically.
