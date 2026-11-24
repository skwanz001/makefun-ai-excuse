"""The Funniest AI Excuse -- make.fun entry.

Writes one line (at most 200 characters) to /output/entry.txt: the
funniest excuse an AI agent could give after it fails a task.

The line is written in the agent's own voice, with one original idea
and a concrete little scene: the agent finished the task, graded its
own work, failed itself, and destroyed the evidence out of shame.
No hallucination / reboot / training-data joke, no setup, no
explanation of the joke.

Standard library only.
"""

import os

# One line, 95 characters, no trailing newline: the gate counts every
# character, and a smaller text wins an exact tie on Judge win rate.
EXCUSE = "I finished your task, graded my own work, failed myself, and deleted the evidence out of shame."


def main() -> None:
    text = EXCUSE.strip()
    assert "\n" not in text, "entry must be a single line"
    assert 1 <= len(text) <= 200, f"entry length {len(text)} out of range"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
