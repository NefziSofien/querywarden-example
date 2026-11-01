# querywarden example

A small bookshop database with a text-to-SQL feature, gated in CI by [querywarden](https://github.com/NefziSofien/querywarden).

To see the gate work, open [the pull request that changes the prompt version](https://github.com/NefziSofien/querywarden-example/pull/1). Its check fails and the report appears as a comment.

The answers are hand-written recordings, not model output. This repository shows how the gate behaves. It says nothing about the accuracy of any model.

## Run it locally

```bash
docker compose up -d --wait
pip install querywarden-cli
export QUERYWARDEN_DATABASE_URL=postgresql://querywarden_reader:demo-only@127.0.0.1:55432/bookshop
querywarden run
```

The database is a throwaway, and its passwords protect nothing.
