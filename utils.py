import os

def get_directory_tree(path, show_hidden=False, max_depth=None, current_depth=0, prefix='', is_last_root=True):
    lines = []
    abs_path = os.path.abspath(path)
    root_name = os.path.basename(abs_path) + '/'

    if current_depth == 0:
        lines.append(root_name)

    if max_depth is not None and current_depth > max_depth:
        return ''.join(lines)

    try:
        entries = sorted(os.listdir(path))
    except PermissionError:
        lines.append(f"{prefix}{'└── ' if is_last_root else '├── '}[Permission Denied]\n")
        return ''.join(lines)

    if not show_hidden:
        entries = [e for e in entries if not e.startswith('.')]

    count = len(entries)
    for idx, entry in enumerate(entries):
        full_path = os.path.join(path, entry)
        is_last = (idx == count - 1)

        connector = '└── ' if is_last else '├── '
        lines.append(f"{prefix}{connector}{entry}{'/' if os.path.isdir(full_path) else ''}\n")

        if os.path.isdir(full_path):
            new_prefix = prefix + ('    ' if is_last else '│   ')
            subtree = get_directory_tree(
                full_path,
                show_hidden=show_hidden,
                max_depth=max_depth,
                current_depth=current_depth + 1,
                prefix=new_prefix,
                is_last_root=is_last
            )
            lines.append(subtree)

    return ''.join(lines)

qwer = get_directory_tree(path="./")
print(qwer)