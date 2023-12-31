from db import database_save



t= [
    ["doc1", "maciuca", 10],
    ["doc1", "masina", 3],
    ["doc1", "at", 34],
    ["doc2", "cat", 123],
    ["doc2", "atunci", 3],
    ["doc3", "facere", 4],
    ["doc3", "auzi", 1],
    ["doc4", "maciuca", 2],
    ["doc5", "maciuca", 7],
    ["doc6", "maciuca", 33],
]
y = [
    ["toc1", "maciuca", 10],
]
z = [
]


x = database_save()

# x.make_sure_table_exists()
# x.insert_word_count(t)
# x.insert_word_count(y)
# x.insert_word_count(z)
x.get_most_frecvent_word(["doc1", "doc6"])
x.get_file_names()