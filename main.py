import os
import sys

LINE = "I summarized a meeting we never had, then blocked myself for \"leakage\"."

def main():
    """Write the confession entry to entry.txt in the configured output directory.

    The entry is a single line confessing a specific AI-type failure:
    generating content from a fictional premise, then malfunctioning
    defensively. Writes UTF-8, exactly one line plus newline, 1-200 chars.
    Validates deterministic constraints before writing.
    """
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

    # Content is exactly the line plus a trailing newline
    content = LINE + "\n"

    # Validate: 1-200 chars total (including newline), non-whitespace, exactly one line
    if not (1 <= len(content) <= 200 and content.strip()):
        raise ValueError("content length or whitespace check failed")
    if content.count("\n") != 1:
        raise ValueError("content must contain exactly one newline")

    out_path = os.path.join(out_dir, "entry.txt")

    # Create output directory if needed
    os.makedirs(out_dir, exist_ok=True)

    # Write to primary output path
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(content)

    # If configured directory differs from /output, also write best-effort to /output
    if os.path.abspath(out_dir) != os.path.abspath("/output"):
        try:
            os.makedirs("/output", exist_ok=True)
            with open("/output/entry.txt", "w", encoding="utf-8") as backup_f:
                backup_f.write(content)
        except Exception:
            pass

    print(out_path)
    print(len(content))

# Entry validated: output is 1-200 chars, one line, deterministic.
if __name__ == "__main__":
    main()
