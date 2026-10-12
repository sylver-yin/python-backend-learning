programming_glossary = {
    "string": "String is a type of variable that lets you assign text with variable so you can use it in your code.",
    "tuple": "Tuple is a variation of list that can't be changed by methods, but can be modified with variable.",
    "list": "List lets you to store the variables inside of it and can be modified with variables",
    "constant": "Constant is the value that will never change throughout the programm's lifespan until you do it manually",
    "comments": "With comments you can create a piece of text inside of your code that IDE will ignore, but it may help your or your colleagues.",
    "set": "Set is a collection in which every item must be unique",
    "dictionary": "Dictionary is a variation of list which contains key and value instead of just variable",
    "IDE": "Workspace application for programmers that includes all essentials tools",
    "slices": "Slices are needed to use just some parts of the list that you need instead of using it whole",
    "loop": "Loop is an action that lets you to perform a certain action through all the list or it's slice with the 'for ... in ...:' statement",
}

for term, explanation in programming_glossary.items():
    print(f"\n{term.title()}: {explanation}")
