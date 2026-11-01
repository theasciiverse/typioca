# typioca (Asciiverse packaging)

Lukas Bloznelis's typioca (Go, Bubble Tea, MIT), packaged for the
Asciiverse catalog (id `typioca`, kind `game`, genre `typing`). Not our
code: no code changes so far; list any in PATCHES.md.

- `upstream` is github.com/bloznelis/typioca (branch `master`); ours is
  branch `asciiverse`, `origin` github.com/theasciiverse/typioca.
- Build: `CGO_ENABLED=0 go build -trimpath -tags netgo -o typioca .`
  (Go from go.mod, 1.22+).
- Release: tag `v<upstream version>+<upstream commit date>-av.<n>` (first
  `v3.1.0+20250306-av.1`) and push it; `.github/workflows/asciiverse-release.yml`
  cross-builds Linux, macOS and Windows on one runner. Upstream's
  workflows are removed because they fire on any tag and publish to the
  AUR and Homebrew.
- typioca keeps its config and results in ~/.cache/typioca (configdir's
  LocalCache) and reads user config from ~/.config/typioca.
- Preview: `asciiverse/record-preview.sh ./typioca` (asciinema 3, tmux):
  drive.py picks a word count run, reads the words from the pane and
  types them one key at a time (typioca drops keys sent in one burst);
  about 34 s with the results.
