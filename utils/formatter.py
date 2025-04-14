# utils/formatter.py

def print_section_header(title):
    print("\n" + "=" * len(title))
    print(title)
    print("=" * len(title) + "\n")

def format_output(title, content):
    print_section_header(title)
    print(content if content else "No results found.")

def highlight_line(line, keyword):
    return line.replace(keyword, f"\033[93m{keyword}\033[0m")  # yellow highlight
