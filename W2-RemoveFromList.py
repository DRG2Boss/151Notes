books = ["Python Crash Course", "Game Programming", "Code Complete", "Clean Code", "The Pragmatic Program"]

books.remove("Python Crash Course")
# This will remove the exact entry we specify.
books.pop(-3)
# This will remove indicated entry from the list but the ORIGINAL list will be unaltered. Use "del var(-3)" to alter.
print(books)
