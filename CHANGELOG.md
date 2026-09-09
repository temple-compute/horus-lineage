# Changelog

## 0.2.0 - unreleased

Breaking: records now go under the workflow's run directory,
`<run-directory>/.horus-lineage/<run>/`, instead of `~/.horus-lineage/`.
Set `HORUS_LINEAGE_DIR` to an absolute path to keep the old location.
`HORUS_LINEAGE_DIR=@run` now names the default.

Breaking: the HTML report is gone, with `HORUS_LINEAGE_REPORT` and the
`horus-lineage report` command. Recording and `conformance` are
unchanged.

- Test that a YAML workflow is copied into the run directory.
- Remove the workflows, so the hosting organisation supplies its own
  CI, release and scanning.
- Remove the ADRs. The record format is described in the README.
- Add SECURITY.md, CONTRIBUTING.md, dependabot and an issue template.

## 0.1.0 - 2026-09-03

First release: four recording middlewares, `conformance`, and the
optional `report` behind `HORUS_LINEAGE_REPORT`.
