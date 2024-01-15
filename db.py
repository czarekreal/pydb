import os

class files:

    def read_file(path):

        #check if type of content is right
        if type(path) != str:
            raise Exception('Wrong type!')

        #check for file
        if not os.path.exists(path=path):
            raise Exception("File doesn't exists!")

        #create file handler
        file = open(path,'r')

        #read file content and close handler
        content = file.read()
        file.close()

        return content
    
    def create_file(path):

        #check for file
        if os.path.exists(path=path):
            raise Exception('File exists!')
        else:

            #create file handler
            file = open(path,'w')

            #close file handler
            file.close()
    
    def write_to_file(path, content, wipe, at_end):
        
        #check if type of content is right
        if type(content) != str or type(wipe) != bool or type(path) != str or type(at_end) != bool:
            raise Exception('Wrong type!')

        #check for file
        if not os.path.exists(path=path):
            raise Exception("File doesn't exists!")
        
        #create file handler
        file = open(path,'r')

        #read file, close handler and create new one
        old_content = file.read()
        file.close()
        file = open(path,'w')

        #add old content if wipe is true
        if not wipe:
            if at_end:
                content = old_content + content
            else:
                content = content + old_content

        #write content to file and close handler
        file.write(content)
        file.close()

class database:

    def create_db(name):

        #check type
        if type(name) != str:
            raise Exception('Name can only be a string')
        
         #check for db path
        if os.path.exists(name):
            raise Exception("Database exists!")
        
        os.mkdir(name)

    def get_db(name,content,create_on_error):

        #check type
        if type(name) != str:
            raise Exception('Name can only be a string')
        
        #check for db path
        if not os.path.exists(name):
            raise Exception("Database doesn't exists!")
        
        #check for db content
        if not os.path.exists(f'{name}\\{content}'):
            if create_on_error:
                database.create_db(name=name)
            else:
                raise Exception("Database reference doesn't exists!")
        
        #get database content
        cont = files.read_file(f"{name}\\{content}")
        return cont
    
    def add_to_db(name,content,data,create_on_error):

        #check type
        if type(name) != str:
            raise Exception('Name can only be a string')
        
        #check for db path
        if not os.path.exists(name):
            if create_on_error:
                database.create_db(name=name)
            else:
                raise Exception("Database doesn't exists!")
        
        #check for db content
        if os.path.exists(f'{name}\\{content}'):
            raise Exception("Database reference exists!")
        
        files.create_file(f'{name}\\{content}')
        files.write_to_file(f'{name}\\{content}',data,True,True)