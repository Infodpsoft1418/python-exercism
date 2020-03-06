import re

# BLOCK ELEMENTS
HEADING_1 = re.compile("# (.*)")
HEADING_2 = re.compile("#{2} (.*)")
HEADING_6 = re.compile("#{6} (.*)")
LIST = re.compile(r"\* (.*)")
BLOCK = re.compile(r"<h|<ul|<p|<li")

# INLINE ELEMENTS
STRONG = re.compile("(.*)__(.*)__(.*)")
EMPHASIS = re.compile("(.*)_(.*)_(.*)")

# BLOCK HTML
start_list_html = "<ul>"
end_list_html = "</ul>"


def heading_html(level, line):
    return f"<h{level}>{line}</h{level}>"


def paragraph_html(line):
    return f"<p>{line}</p>"


def list_item_html(line):
    """Single list element."""
    return f"<li>{line}</li>"


# Inline HTML
def strong_html(line):
    return f"{line.group(1)}<strong>{line.group(2)}</strong>{line.group(3)}"


def emphasis_html(line):
    return f"{line.group(1)}<em>{line.group(2)}</em>{line.group(3)}"


def heading_parser(line):
    if HEADING_6.match(line):
        return heading_html(6, line[7:])
    elif HEADING_2.match(line):
        return heading_html(2, line[3:])
    elif HEADING_1.match(line):
        return heading_html(1, line[2:])
    return line


def inline_parser(line):
    is_bold = STRONG.match(line)
    if is_bold:
        line = strong_html(is_bold)
    is_emphasis = EMPHASIS.match(line)
    if is_emphasis:
        line = emphasis_html(is_emphasis)
    return line


def parse(markdown):
    output = ""
    in_list = False
    in_list_append = False
    for line in markdown.split("\n"):
        line = heading_parser(line)

        is_list = LIST.match(line)
        if is_list:
            line = inline_parser(is_list.group(1))
            line = list_item_html(line)
            if not in_list:
                in_list = True
                line = start_list_html + line
        else:
            if in_list:
                in_list_append = True
                in_list = False

        if not BLOCK.match(line):
            line = paragraph_html(line)
        line = inline_parser(line)

        if in_list_append:
            line = end_list_html + line
            in_list_append = False
        output += line
    if in_list:
        output += end_list_html
    return output
