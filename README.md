# Sacred Experiments Browser (Dash)

A simple Dash web app to enter MongoDB credentials and list Sacred experiments (from the `runs` collection). Now with a pretty Bootstrap UI, a hideable connection panel, and saved credentials across refresh/sessions.

## Requirements

- Python 3.9+ recommended
- Pip

## Setup

1. Create and activate a virtual environment (recommended).
   - Windows (PowerShell):
     ```powershell
     python -m venv .venv
     .\.venv\Scripts\Activate.ps1
     ```
   - macOS/Linux:
     ```bash
     python3 -m venv .venv
     source .venv/bin/activate
     ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Run the app

```bash
python app.py
```

Open your browser to `http://127.0.0.1:8050/`.

## Usage

You can either:
- Paste a full MongoDB URI (e.g. `mongodb+srv://user:pass@cluster/yourdb?authSource=admin`), or
- Fill the individual fields: host, port, username/password (optional), and `authSource` if needed.

Specify the database name (defaults to `sacred`). Click Connect to see a list of experiment names detected in the `runs` collection under `experiment.name`.

If your Sacred data is not in `runs` or uses a different structure, update the query logic in `app.py` (`fetch_sacred_experiment_names`). 

### UI Notes

- The top Navbar has a “Connection” toggle to show/hide the connection form.
- Check “Save credentials locally” to persist connection settings in your browser (localStorage). They will survive refresh and future visits.
- Optionally check “Include password” to also store the password in the browser. Only enable this on trusted, personal devices.
- Use “Clear saved” to remove stored credentials at any time.

## Config

- Set `SACRED_DB_NAME` environment variable to change the default DB name:
  ```bash
  $env:SACRED_DB_NAME="my_sacred_db"  # PowerShell
  export SACRED_DB_NAME="my_sacred_db" # bash/zsh
  ```


