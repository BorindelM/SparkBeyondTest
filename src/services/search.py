import os
from db import db

class wordsearch_service:
        
        

    def save_document_words(self, filename, text):
        
        database_conn = db.database_save()
        word_count = {}
        for line in text.splitlines():

            for word in line.split():
                word = word.decode('ascii')
                if word in word_count:
                    word_count[word] += 1
                else:
                    word_count[word] = 1

        inserted = []
        for k,v in word_count.items():
            inserted.append([filename, k, v])
        database_conn.insert_word_count(inserted)


    def get_most_used_word(self, documents):
        database_conn = db.database_save()

        return database_conn.get_most_frecvent_word(documents)
    
    def get_documents(self):
        database_conn = db.database_save()

        return database_conn.get_file_names()

        

