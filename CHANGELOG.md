# Changelog

All notable changes to this project are documented here.

The format is based on [Keep a Changelog][kac], and this project
adheres to [Semantic Versioning][semver].

[kac]: https://keepachangelog.com/en/1.1.0/
[semver]: https://semver.org/spec/v2.0.0.html

## [0.1.7] - 2026-07-15

### Added

- `get_secret` is now a public API for reading values from Google
  Secret Manager. Call `get_secret("MY_SECRET")` and `project_id`
  defaults to the project detected from the ambient credentials, or
  pass `project_id` and `version_id` explicitly.
- `get_secret` raises `ValueError` when `secret_id` is empty, or when
  no project ID is provided and none can be detected.
- Notebook usage documentation for reading secrets from Colab, Vertex AI
  Workbench, and local Jupyter.
- PyPI keywords and classifiers so the package is discoverable for
  Secret Manager and notebook use cases.

### Changed

- Notification secrets (`GCHAT_WEBHOOK_URL`, `EMAIL_SENDER`,
  `EMAIL_PASSWORD`, `EMAIL_RECIPIENTS`) are now fetched lazily on the
  first `notify` / `async_notify` call instead of at import. Importing
  the package for `get_secret` alone no longer prints "Failed to fetch
  secret" errors when the notification secrets are absent.

### Fixed

- Corrected the minimum supported Python to 3.9. The code already
  required it (it uses `list[str]` annotations), so the previous `>=3.8`
  claim was inaccurate.

## [0.1.6] - 2025-08-21

### Added

- Release script (`release.sh`) for tagging and publishing.

### Changed

- Clearer async usage examples in the README, including notebook usage.

## [0.1.5] - 2025-08-21

### Added

- Asynchronous notifications: `async_notify` and
  `async_notify_on_failure`, using `aiosmtplib` and `httpx` (install
  the `async` extra: `pip install 'gcp-notifier[async]'`).

## [0.1.4] - 2025-08-21

### Added

- Optional `test` dependency group and GitHub Actions workflows for
  building and publishing the package.

[0.1.7]: https://github.com/marcellusmontilla/gcp_notifier/compare/v0.1.6...v0.1.7
[0.1.6]: https://github.com/marcellusmontilla/gcp_notifier/compare/v0.1.5...v0.1.6
[0.1.5]: https://github.com/marcellusmontilla/gcp_notifier/compare/v0.1.4...v0.1.5
[0.1.4]: https://github.com/marcellusmontilla/gcp_notifier/releases/tag/v0.1.4
