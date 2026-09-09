# Contributing

```bash
uv sync --group dev
make test
make lint
make type-check
```

Rules the tests enforce:

- The plugin never fails a run. A recorder error is logged and dropped.
- One file per task, written when the task finishes.
- Records carry paths, digests and the command line, nothing else.
- A semantic change to the record shape is a new format version, never
  an edit. See Reading records in the README.

Keep commits brief, one change each. Put the reasoning in the pull
request. Docstrings are one line, two at most.
