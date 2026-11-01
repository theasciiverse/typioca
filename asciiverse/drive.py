#!/usr/bin/env python3
"""drive.py SOCKET SESSION: types a typioca test in a tmux pane like a person.

Picks "Word count run" (25 common words) from the menu, reads the words
off the screen and types them at about 75 words per minute with a seeded
rhythm: a few typos, each fixed with backspace. typioca drops keys that
arrive in one burst, so every key goes on its own. When the results are up
it waits, goes back to the menu with ctrl+q and quits with ctrl+c. Run by
record-preview.sh while asciinema records the pane."""
import random, re, subprocess, sys, time

SOCK, S = sys.argv[1], sys.argv[2]
rng = random.Random(11)

def tmux(*a): return subprocess.run(["tmux", "-L", SOCK, *a], capture_output=True, text=True).stdout
def key(*k): tmux("send-keys", "-t", S, *k)
def lit(s): tmux("send-keys", "-l", "-t", S, s)
def pane(): return tmux("capture-pane", "-p", "-t", S).split("\n")

time.sleep(2.5)
key("Down"); time.sleep(1.2)
key("Enter"); time.sleep(2)
lines = [l.strip() for l in pane()]
words = " ".join(l for l in lines
                 if l and "ctrl+r" not in l and not re.fullmatch(r"\d+s", l)).split()

for wi, w in enumerate(words):
    for c in w:
        if rng.random() < 0.025 and c.isalpha():
            lit(rng.choice("asdfghjklqwertyuiop"))
            time.sleep(rng.uniform(0.12, 0.25))
            key("BSpace")
            time.sleep(rng.uniform(0.1, 0.2))
        lit(c)
        time.sleep(rng.uniform(0.06, 0.16))
    if wi < len(words) - 1:
        lit(" ")
        time.sleep(rng.uniform(0.08, 0.22))
time.sleep(8)
key("C-q"); time.sleep(2)
key("C-c")
