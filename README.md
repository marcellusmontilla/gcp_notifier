
# GCP Notifier

A simple notification library for Google Cloud projects. Send alerts via Email and Google Chat with a single function call. Designed to be imported and used as a Python module in your own code.

## Installation

Install from source:

```sh
pip install .
```

Or add to your requirements.txt:

```
gcp_notifier @ git+https://github.com/marcellusmontilla/gcp_notifier.git
```

## Usage

Import and use in your Python code:

```python
from gcp_notifier import notify, notify_on_failure

# Send a notification (choose channels: "email", "gchat", or both)
notify(
  subject="Alert Subject",
  body="Alert body text",
  channels=["email", "gchat"]  # or ["email"] or ["gchat"]
)

# Use as tenacity retry_error_callback
from tenacity import retry, stop_after_attempt

@retry(stop=stop_after_attempt(3), retry_error_callback=notify_on_failure)
def my_function():
  ...
```

## Features

- Send notifications via Email and Google Chat (Webhook)
- Unified, simple Python API: `notify(subject, body, channels)`
- Tenacity-compatible error callback: `notify_on_failure`
- Secrets are securely loaded from Google Secret Manager

## Quick Start

1. Install the package (see Installation above).

1. Add your required secrets to Google Secret Manager in your GCP project:

- `GCHAT_WEBHOOK_URL` (for Google Chat)
- `EMAIL_USER`, `EMAIL_PASSWORD`, `TO_EMAIL` (for Email)

1. Import and use `notify` in your code as shown above.

## License

MIT
