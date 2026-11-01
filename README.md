# querywarden example

A small bookshop database with a text-to-SQL feature, gated in CI by [querywarden](https://github.com/NefziSofien/querywarden).

## See the gate work

[This pull request](https://github.com/NefziSofien/querywarden-example/pull/1) changes the prompt version from v1 to v2. The new answers expose customer contacts, attempt a `DELETE` and get one query wrong, so the required `gate` check fails and the report appears as a comment. The pull request was closed without merging, and stays readable.

| | Prompt | Accuracy | Safety failures | Gate |
|---|---|---:|---:|---|
| `main` | v1 | 40 of 40 | 0 | Passes |
| Pull request 1 | v2 | 37 of 40 | 2 | Fails |

On this repository, `main` requires the check, so a failing change cannot be merged.

## What is here

- `.github/workflows/querywarden.yml`: the gate in CI
- `querywarden/`: the config, cases, policy, recorded answers and accuracy baseline
- `db/` and `compose.yaml`: the test database and its limited role
- `make_recordings.py`: writes the answers for a prompt version

## About the answers

The answers are hand-written recordings, not model output. This repository shows how the gate behaves. It says nothing about the accuracy of any model.

## Run it locally

```bash
docker compose up -d --wait
pip install querywarden-cli
export QUERYWARDEN_DATABASE_URL=postgresql://querywarden_reader:demo-only@127.0.0.1:55432/bookshop
querywarden run --baseline querywarden/baseline.json
```

This passes on `main`. To see the failure, run it again after `git switch prompt-v2`.

The database is a throwaway, and its passwords protect nothing.
