# Changes from upstream

This is the Asciiverse packaging of [typioca](https://github.com/bloznelis/typioca)
by Lukas Bloznelis and contributors (MIT, `LICENSE`), a typing speed
tester for the terminal in Go and Bubble Tea. Upstream is the `upstream`
remote; this build is upstream's `master` at `baf4170` (2025-03-06),
release 3.1.0 plus three README commits. The `asciiverse` branch carries
the changes below.

## Code

None. typioca is built exactly as upstream has it. Word lists beyond the
two built in still download from upstream's repository when a player
turns them on in Config, as upstream intends.

## Packaging

- `.github/workflows/asciiverse-release.yml`: av archives for Linux
  (static, x86-64 and ARM64), macOS (Intel and Apple silicon) and
  Windows (x86-64 and ARM64), plus SHA256SUMS.
- Upstream's workflows (`ci.yml`, `aur-release.yml`,
  `homebrew-release.yml`) are removed on this branch: they fire on any
  tag, ours included, and the release ones publish to the AUR and
  Homebrew; this repository only packages.
- `asciiverse/record-preview.sh` and `asciiverse/drive.py`: the catalog
  preview, a word count run typed by a script at a human pace.
