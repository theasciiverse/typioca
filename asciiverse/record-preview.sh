#!/bin/sh
# Records the 100x30 catalog preview, asciiverse/typioca.cast
# (hub/RECORDING.md): from the menu a word count run (25 common words)
# typed by asciiverse/drive.py at about 75 words per minute, a few typos
# fixed on the way, then the results and back to the menu. asciinema
# records a tmux pane (own socket, no status line, no user config) that
# drive.py reads and types into. Needs asciinema 3 and tmux.
#   asciiverse/record-preview.sh ./typioca
set -eu
binary=$(cd "$(dirname "$1")" && pwd)/$(basename "$1")
here=$(cd "$(dirname "$0")" && pwd)
out=$here/typioca.cast
home=$(mktemp -d)
trap 'tmux -L avrec kill-server 2>/dev/null; rm -rf "$home"' EXIT
mkdir "$home/bin" && cp "$binary" "$home/bin/typioca"
cd "$home"  # nothing in the recording names a local path
unset XDG_CONFIG_HOME XDG_CACHE_HOME
export HOME="$home" PATH="$home/bin:$PATH" TERM=xterm-256color COLORTERM=truecolor LANG=C.UTF-8
tmux -L avrec -f /dev/null new-session -d -s rec -x 100 -y 30 "typioca" \; set -g status off
python3 -I "$here/drive.py" avrec rec &
drive=$!
asciinema rec --headless --overwrite -q \
  --window-size 100x30 --idle-time-limit 2 \
  --capture-env "TERM,COLORTERM,LANG" --title "typioca" \
  --command "tmux -L avrec attach -t rec" "$out"
wait "$drive"
