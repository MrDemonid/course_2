import re


class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def restore_tree(log_path: str) -> BinaryTreeNode:
    pattern = re.compile(
        r"Посетили узел (\d+), левый потомок: (None|\d+), правый потомок: (None|\d+)(?: #.*)?"
    )

    nodes = {}
    root = None

    with open(log_path, encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            match = pattern.fullmatch(line)
            if not match:
                raise ValueError(f"Неверный формат строки лога: {line}")

            node_val, left_val, right_val = match.groups()
            node_val = int(node_val)
            left_val = None if left_val == 'None' else int(left_val)
            right_val = None if right_val == 'None' else int(right_val)

            # Создаём или берём существующий узел
            if node_val not in nodes:
                nodes[node_val] = BinaryTreeNode(node_val)
            current = nodes[node_val]

            if root is None:
                root = current

            if left_val is not None:
                if left_val not in nodes:
                    nodes[left_val] = BinaryTreeNode(left_val)
                current.left = nodes[left_val]

            if right_val is not None:
                if right_val not in nodes:
                    nodes[right_val] = BinaryTreeNode(right_val)
                current.right = nodes[right_val]

    return root


def print_tree(node, prefix="", is_left=True):
    if node is None:
        return

    if node.right:
        new_prefix = prefix + ("│   " if is_left else "    ")
        print_tree(node.right, new_prefix, False)

    print(prefix + ("└── " if is_left else "┌── ") + str(node.value))

    if node.left:
        new_prefix = prefix + ("    " if is_left else "│   ")
        print_tree(node.left, new_prefix, True)



if __name__ == "__main__":
    root = restore_tree('tree_log.txt')
    print_tree(root)

# │   ┌── 3
# └── 1
#     │   ┌── 5
#     └── 2
#         └── 4
