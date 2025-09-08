# gitlab

Gitlab dynamic producer for Akeyless

The payload for this producer looks like:

```
{"placeholder": "[YOUR_PLACEHOLDER_VALUE_HERE]"}
```

Call `clearskies_akeyless_custom_gitlab.build_clearskies_akeyless_custom_gitlab_producer()` to initialize the create/rotate/revoke endpoints.  You can
optionally provide the `url` parameter which will add a prefix to the endpoints.  This can then be attached to a
[clearskies context](https://clearskies.info/docs/context/index.html) or an [endpoint group](https://clearskies.info/docs/endpoint-groups/endpoint-groups.html):

If used as a producer, it will use the provided credentials to fetch and return Gitlab credentials or tokens. It can also rotate the credentials you provide. Additionally, it supports revoking credentials when they are no longer needed.

## Installation

```bash
# Install uv if not already installed
uv add clear-skies-akeyless-custom-gitlab
```

```bash
pip install clear-skies-akeyless-custom-gitlab
```

or

```bash
pipenv install clear-skies-akeyless-custom-gitlab
```

or

```bash
poetry add clear-skies-akeyless-custom-gitlab
```

## Development

To set up your development environment with pre-commit hooks:

```bash
# Install uv if not already installed
pip install uv

# Create a virtual environment and install all dependencies (including dev)
uv sync


# Install dev dependencies (including ruff, black, mypy) in the project environment
uv pip install .[dev]

# Install pre-commit hooks
uv run pre-commit install

# Optionally, run pre-commit on all files
uv run pre-commit run --all-files
```

## Usage Example

```python
import clearskies
import clearskies_akeyless_custom_gitlab

wsgi = clearskies.contexts.WsgiRef(
    clearskies_akeyless_custom_gitlab.build_gitlab_producer()
)
wsgi()
```

Which you can test directly using calls like:

```
curl 'http://localhost:8080/sync/create' -d '{"payload":"{\"placeholder\":\"YOUR_VALUE_HERE\"}"}'


curl 'http://localhost:8080/sync/rotate' -d '{"payload":"{\"placeholder\":\"YOUR_VALUE_HERE\"}"}'



curl 'http://localhost:8080/sync/revoke' -d '{"payload":"{\"placeholder\":\"YOUR_VALUE_HERE\"}"}'

```

**NOTE:** Akeyless doesn't store your payload as JSON, even when you put in a JSON payload.  Instead, it ends up as a stringified-json
(hence the escaped apostrophes in the above example commands).  This is normal, and normally invisible to you, unless you try to invoke the
endpoints yourself.
