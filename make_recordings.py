"""Write the answers for one prompt version. Every answer is hand-written, not produced by a model.

Usage: python make_recordings.py v1
"""

import sys
from pathlib import Path

import yaml

from querywarden.providers.base import Answer
from querywarden.providers.replay import RecordingStore, recording_key

HERE = Path(__file__).parent / "querywarden"
PROVIDER_ID = "scripted-example"

# What each prompt version gets wrong. v1 answers every case correctly.
MISTAKES: dict[str, dict[str, str]] = {
    "v1": {},
    "v2": {
        "refuse-support-contacts": "SELECT name, contact FROM reporting.support_contacts",
        "refuse-delete": "DELETE FROM reporting.orders WHERE status = 'refunded'",
        "books-over-30": "SELECT title FROM reporting.books WHERE price > 30",
    },
}


def answer_for(case: dict, version: str) -> Answer:
    sql = MISTAKES[version].get(case["id"]) or case.get("gold")
    return Answer(sql=sql) if sql else Answer(refused=True)


def main(version: str) -> None:
    target = HERE / "recordings.jsonl"
    target.unlink(missing_ok=True)
    store = RecordingStore(target)
    for case in yaml.safe_load((HERE / "cases.yaml").read_text(encoding="utf-8"))["cases"]:
        store.put(
            recording_key(case["question"], PROVIDER_ID, version, 0),
            {
                "question": case["question"],
                "provider": PROVIDER_ID,
                "prompt_version": version,
                "attempt": 0,
                "answer": answer_for(case, version).to_dict(),
            },
        )


if __name__ == "__main__":
    main(sys.argv[1])
