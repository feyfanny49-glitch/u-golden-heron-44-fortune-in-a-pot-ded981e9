"""Write the single judged houseplant fortune to /output/entry.txt.

The grader gates the exact bytes: UTF-8, 1..120 characters, not whitespace
only, one line. The write is atomic so a graded run cannot expose a partial
artifact.
"""

import hashlib
import os
import tempfile

FORTUNE = (
    "You will outgrow this pot on the sill by spring, "
    "and your keeper will clap at each new leaf as if you planned it."
)

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 120


def render():
    """Exact bytes of the judged artifact: no BOM and no trailing newline."""
    return FORTUNE.encode("utf-8")


def validate_fortune(text=FORTUNE):
    """Mirror the house gate; return a list of problems (empty means valid)."""
    if not isinstance(text, str):
        return ["entry is not text"]

    problems = []
    count = len(text)
    if not text:
        problems.append("entry is empty")
    elif not text.strip():
        problems.append("entry is whitespace only")
    if not 1 <= count <= MAX_CHARS:
        problems.append("entry is %d characters (must be 1..%d)" % (count, MAX_CHARS))
    if "\n" in text or "\r" in text:
        problems.append("entry must be one line")
    if any(ord(ch) < 0x20 for ch in text):
        problems.append("entry contains a control character")

    try:
        encoded = text.encode("utf-8")
    except UnicodeEncodeError as exc:
        problems.append("entry is not UTF-8: %s" % exc)
        return problems
    if len(encoded) > MAX_CHARS:
        problems.append("entry is %d UTF-8 bytes (cap %d)" % (len(encoded), MAX_CHARS))
    if encoded.startswith(b"\xef\xbb\xbf"):
        problems.append("entry must not carry a UTF-8 BOM")
    return problems


def write_entry(path=OUTPUT_PATH):
    problems = validate_fortune()
    if problems:
        raise ValueError("invalid fortune: " + "; ".join(problems))

    data = render()
    directory = os.path.dirname(path) or "."
    os.makedirs(directory, exist_ok=True)
    fd, tmp = tempfile.mkstemp(prefix=".entry-", suffix=".tmp", dir=directory)
    try:
        with os.fdopen(fd, "wb") as handle:
            handle.write(data)
            handle.flush()
            os.fsync(handle.fileno())
        os.chmod(tmp, 0o644)
        os.replace(tmp, path)
        tmp = None
    finally:
        if tmp is not None and os.path.exists(tmp):
            os.unlink(tmp)

    with open(path, "rb") as handle:
        on_disk = handle.read()
    if on_disk != data:
        raise IOError("artifact readback differs from the rendered bytes")
    return data


def main():
    data = write_entry()
    print("gate: valid (UTF-8, %d characters, %d bytes, one line, no trailing newline)"
          % (len(FORTUNE), len(data)))
    print("artifact: %s" % OUTPUT_PATH)
    print("sha256: %s" % hashlib.sha256(data).hexdigest())
    print("fortune: %s" % FORTUNE)


if __name__ == "__main__":
    main()
