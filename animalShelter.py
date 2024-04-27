from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    # Initialize the AnimalShelter class with MongoDB connection
    def __init__(self, user, passwd, host ='nv-desktop-services.apporto.com', port=32486, db='AAC', col='animals'):
      
      # Establishing the MongoDB connection
        self.client=MongoClient(f'mongodb://{user}:{passwd}@{host}:{port}/{db}?authSource=admin')
      
      # Accessing the specified database
        self.database=self.client[db]
      
      # Accessing the specififed collection
        self.collection=self.database[col]
        
    # Complete the create method C    
    def create(self, data):      
        if data is not None:
            try:
                # Attempting to insert the document
                result =self.collection.insert_one(data)
                # Printing result
                print(result)
                # Return True if an ID assigned, indicationg success
                return True if result.inserted_id is not None else False 
            except Exception as e:
                # Handling insertion failure
                print(f"Insertion failed: {e}")
        else:
            # Raising an exception if no data is provided
            raise Exception('Nothing to save, because data parameter is empty')
    
    # Complete the read method R              
    def read(self, searchData):
        if searchData:
            # Searching for documents matching the seachData
            data = self.collection.find(searchData)
        else:
            # If no serchData provided, return all documets without their IDs
            data = self.collection.find()
        return data
        
    # Complete the update method U
    def update(self, searchData, updateData):
        if searchData is not None:
           # Performing the update operation
           result = self.collection.update_many(searchData, {"$set": updateData})
        else:
           # Raising an exception of no search criteria is provided
           raise Exception('Nothing to update, because data parameter is empty')
        return result.raw_result
        
    # Complete the delete method D
    def delete(self, deleteData):   
        if deleteData is not None:
           try:
              # Attempting to delete the documents matching deleteData
              result = self.collection.delete_many(deleteData)
              # Returning the count of deleted documents
              return {"deleted_count": result.deleted_count}
           except Exception as e:
              # Handling deletion failure
              raise Exception(f"Deletion failed: {str(e)}")
        else:
           # Raising an exception if no delte criteria is provided
           raise Exception('Nothing deleted, because data parameter is empty')
   
