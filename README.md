# Kardboard

**A terminal Kanban board backed entirely by local Markdown files in a .kardboard directory, keeping task management frictionless and git-native.**

External project management tools force you out of your editor, require messy web UI clicks, and fragment your project context away from your source code. Kardboard removes the context switch of heavy issue trackers by keeping every task, note, and column state right inside your repository as plain text.

## Example

<!-- A real command and its REAL pasted output. Run it first. -->

## Install

```bash
pip install -e ".[dev]"
```

## Usage

<!-- The 2-4 commands people actually need, one line each. -->

## How it works

<!-- 3-6 bullets: what it checks, computes or produces. -->

## Limitations

- Single-user: the board is a set of local files; there is no multi-user editing or locking.
- No authentication: anyone with access to the directory can read and modify the board.
- Local-only: everything lives in `.kardboard/` inside your working tree; there is no server component.
- No remote sync: Kardboard does not push, pull, or merge boards across machines — use git for that.

## Development

```bash
pip install -e ".[dev]"
pytest -q
ruff check .
```

## License

MIT -- see [LICENSE](LICENSE).
