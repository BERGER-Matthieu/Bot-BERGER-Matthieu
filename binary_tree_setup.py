import binary_tree as bt


def setup():
    tree = bt.Binary_Tree()
    tree.root = bt.Junction("```Do you want to access commands [L], or juste go out [R]?```")
    tree.root.add_junction("```You want to access history commands [L], or game commands [R]?```", False)
    tree.root.add_leaf("```Juste go touch some grass```", True)

    tree.root.left.add_leaf(
        "```Use $ as a prefix and :\n\t- S \"your message\" to save it.\n\t- V \"message index\" to view the history "
        "starting at the index.\n\t- VF \"username\" to view history based on one user.\n\t- C to clear it.\n\t- L "
        "for the"
        "length.\n\t- SAVE to overwrite the json file.\n\t- SA \"subject\" to Speak About a subject.```",
        False)
    tree.root.left.add_leaf("No games yet", True)

    tree.add_subject("python", "```Python is a high-level, general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation via the off-side rule. Python is dynamically typed and garbage-collected.```")
    tree.add_subject("why", "```this discord bot is a project for my data lessons```")

    return tree
