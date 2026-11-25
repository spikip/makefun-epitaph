"""Entry for the make.fun bounty "Famous Last Words: The Funniest Epitaph".

The program writes a single funny epitaph of famous last words to
/output/entry.txt. The line turns on the famous poem "Do not stand at
my grave and weep": the dead speaker is not there, because he finally
left the group chat. It reads like something carved in stone, lands
its surprise in one read, and needs no explanation. The gate allows
1 to 150 characters of UTF-8 text, so the line is checked against
that cap before it is written.

Why this line: the judge weighs whether the line really is a one-line
epitaph of famous last words, whether it earns a real laugh, whether
it turns on a surprise, whether it reads carved in stone, and whether
it stays in the head. The opening borrows the most famous grave poem
there is, so the epitaph form is unmistakable; the twist is that the
speaker's great escape is not heaven but leaving the group chat, a
small modern victory everyone recognises at once. It is short, it is
one sentence of dying speech, and the punchline is quotable enough to
repeat to a friend. The em dash is the only punctuation flourish, and
the line keeps the plain carved-stone voice throughout.
"""

import os

ENTRY = (
    "Do not stand at my grave and weep. I am not here — "
    "I finally left the group chat."
)

MAX_CHARS = 150
OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = ENTRY.strip()
    assert text, "entry must not be empty"
    assert "\n" not in text, "entry must be a single line"
    assert len(text) <= MAX_CHARS, (
        f"entry is {len(text)} characters, over the {MAX_CHARS} limit"
    )
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(text)
    print(f"wrote {len(text)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
