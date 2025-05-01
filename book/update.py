import os

ROOT_DIR = "contents"
TOC_TXT_FILE = "toc.txt"
INTRO_LINE = "This section provides an overview of the topic."

def make_title(folder_name):
    return folder_name.replace('_', ' ').replace('-', ' ').title()

def write_index_md(path, title):
    index_path = os.path.join(path, "index.md")
    if not os.path.exists(index_path):
        with open(index_path, "w") as f:
            f.write(f"# {title}\n\n{INTRO_LINE}\n")

def build_toc_structure(root):
    toc_lines = ["format: jb-book", "root: contents/intro.md", ""]
    parts_dict = {}

    for dirpath, dirnames, filenames in os.walk(root):
        relpath = os.path.relpath(dirpath, root)
        parts = relpath.split(os.sep)

        if relpath == ".":
            continue
        if any(part.startswith(".") for part in parts):
            continue

        write_index_md(dirpath, make_title(parts[-1]))
        toc_path = os.path.join("contents", relpath, "index.md").replace("\\", "/")

        caption = make_title(parts[0])
        if caption not in parts_dict:
            parts_dict[caption] = []
        parts_dict[caption].append(f"      - file: {toc_path}")

    for caption, files in parts_dict.items():
        toc_lines.append(f"  - caption: {caption}")
        toc_lines.append("    chapters:")
        toc_lines.extend(files)
        toc_lines.append("")

    return toc_lines

def write_toc_txt(toc_lines):
    with open(TOC_TXT_FILE, "w") as f:
        f.write("\n".join(toc_lines))

if __name__ == "__main__":
    toc_lines = build_toc_structure(ROOT_DIR)
    write_toc_txt(toc_lines)
    print(f"TOC written to {TOC_TXT_FILE}")
