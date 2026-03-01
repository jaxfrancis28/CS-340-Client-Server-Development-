# Example Python Code to Insert a Document 
from pymongo import MongoClient
from bson.objectid import ObjectId


class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    # Update __init__ to take arguments for connection details
    def __init__(self, USER, PASS, HOST, PORT, DB, COL):
        # Initializing the MongoClient. This helps to access the MongoDB
        # databases and collections. This is hard-wired to use the aac
        # database, the animals collection, and the aac user.
        #
        # You must edit the password below for your environment.
        #
        # Connection Variables
        USER = 'aacuser'
        PASS = 'JaxJax28' # !! Update this with your actual MongoDB password !!
        HOST = 'localhost'
        PORT = 27017
        DB = 'aac'
        COL = 'animals'
        #
        # Initialize Connection
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]

    # Complete this create method to implement the C in CRUD.
    def create(self, data):
        """ Inserts a document into the animals collection. """
        if data is not None and isinstance(data, dict):
            try:
                result = self.collection.insert_one(data)
                return result.acknowledged
            except Exception as e:
                print(f"An error occurred during creation: {e}")
                return False
        else:
            raise Exception("Nothing to save, because data parameter is empty or not a dictionary")

    # Complete this read method to implement the R in CRUD.
    def read(self, query):
        """ Queries documents from the collection based on the provided query dictionary. """
        if query is not None and isinstance(query, dict):
            try:
                # find() returns a cursor, which can be iterated over
                cursor = self.collection.find(query)
                # Convert cursor to a list of dictionaries to return all results
                return list(cursor)
            except Exception as e:
                print(f"An error occurred during reading: {e}")
                return []
        else:
            # If query is empty or None, return all documents
            cursor = self.collection.find({})
            return list(cursor)
    
    # Complete this update method to implement the U in CRUD.
    def update(self, query, new_values):
        """ Updates documents in the collection based on the query. """
        if query is not None and new_values is not None:
            try:
                # Use $set to update specific fields without replacing the whole document
                result = self.collection.update_many(query, {"$set": new_values})
                return result.modified_count # Returns the number of documents modified
            except Exception as e:
                print(f"An error occurred during update: {e}")
                return 0
        else:
            raise Exception("Query and new values parameters must not be empty")

    # Complete this delete method to implement the D in CRUD.
    def delete(self, query):
        """ Deletes documents from the collection based on the query. """
        if query is not None:
            try:
                result = self.collection.delete_many(query)
                return result.deleted_count # Returns the number of documents deleted
            except Exception as e:
                print(f"An error occurred during deletion: {e}")
                return 0
        else:
            raise Exception("Query parameter must not be empty")
