import psycopg2


class database_save:

    def __init__(self, host='127.0.0.1', port= '5432', database="postgres", user='postgres', password='example' ) -> None:
        
        self.conn = psycopg2.connect(
            database=database, user=user, password=password, host=host, port= port
            )
        self.conn.autocommit = True
    
    def get_file_names(self):

        command = '''
        SELECT DISTINCT document 
		FROM word_count 
        '''
        cursor = self.conn.cursor()
        cursor.execute(command)
        filenames = cursor.fetchall()
        cursor.close()
        print(filenames)
        return [x[0] for x in filenames]


    def get_most_frecvent_word(self, documents):
        len_documents = len(documents) 
        if len_documents == 0:
            return
        
        documents_formated = '('
        current = 1
        for document in documents:
            if current == len_documents:
                documents_formated += '\'' +  document + '\'' + ')'
            else:
                documents_formated += '\'' +  document + '\'' + ','
            current += 1
            
        command = f'''
        SELECT word, SUM(count) AS w_count
        FROM word_count
        WHERE document IN {documents_formated}
        GROUP BY word
        ORDER BY w_count DESC
        LIMIT 1;
        '''
        print(command)
        cursor = self.conn.cursor()
        cursor.execute(command)
        self.conn.commit()
        entry =  cursor.fetchone()
        cursor.close()
        print(entry)

    def insert_word_count(self, words):
        
        len_words = len(words) 
        if len_words == 0:
            return

        command = '''
        INSERT INTO word_count (document, word, count)
        VALUES
        '''
        
        current = 1
        for word in words:
            command += f'(\'{word[0]}\', \'{word[1]}\', {word[2]})'
            if current != len_words:
                command += ','
            else:
                command += ';'
            current += 1
        print(command)
        cursor = self.conn.cursor()
        cursor.execute(command)
        self.conn.commit()
        cursor.close()
    

    def make_sure_table_exists(self):

        if not self._table_exists():
            self._create_table()

    def _table_exists(self, table_str='word_count'):

        exists = False
        try:
            cursor = self.conn.cursor()
            cursor.execute("select exists(select relname from pg_class where relname='" + table_str + "')")
            exists = cursor.fetchone()[0]
            cursor.close()
        except psycopg2.Error as e:
            print(e)
        return exists
    
    def _create_table(self):
        
        create_table_command = '''
            CREATE TABLE IF NOT EXISTS word_count (
            document varchar(45) NOT NULL,
            word varchar(50) NOT NULL,
            count integer NOT NULL)'''
        cursor = self.conn.cursor()
        cursor.execute(create_table_command)
        self.conn.commit()
        cursor.close()


