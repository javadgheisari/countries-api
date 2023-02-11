# import logging
# import threading

import pymongo

# from config.settings import Settings

# settings = Settings()


class MongoDB:
    """
    MongoDB interface class

    source: https://motor.readthedocs.io/en/stable/tutorial-asyncio.html
    """

    def __init__(self):
        # self.init_logger()
        # self.client = pymongo.MongoClient(
        #     f"mongodb://{settings.MONGO_USER}:{settings.MONGO_PASSWORD}@{settings.MONGO_HOST}:{settings.MONGO_PORT}"
        # )

        self.client = pymongo.MongoClient(host='localhost', port=27017)
        # get database
        self.db = self.client["SampleDB"]

    # # Init logger
    # def init_logger(self):
    #     self.logger = logging.getLogger(__name__)
    #     self.logger.info("Starting MongoDB")

    # get collection
    def get_collection(self, collection_name):
        return self.db[collection_name]

    # # insert one document
    # def insert_one(self, collection_name, document):
    #     collection = self.get_collection(collection_name)
    #     result = collection.insert_one(document)
    #     self.logger.info("Inserted one document into collection: %s", collection_name)

    # # insert many documents
    # def insert_many(self, collection_name, documents):
    #     collection = self.get_collection(collection_name)
    #     result = collection.insert_many(documents)
    #     self.logger.info(
    #         "Inserted %s documents into collection: %s", len(documents), collection_name
    #     )

    # find one document
    def find_one(self, collection_name, document):
        collection = self.get_collection(collection_name)
        result = collection.find_one(document)
        return result

    # # find many documents
    # def find_many(self, collection_name, document):
    #     collection = self.get_collection(collection_name)
    #     result = list(collection.find(document))
    #     return result

    # # count documents
    # def count(self, collection_name, document):
    #     collection = self.get_collection(collection_name)
    #     result = collection.count_documents(document)
    #     return result

    # # update one document
    # def update_one(self, collection_name, document, update):
    #     collection = self.get_collection(collection_name)
    #     result = collection.update_one(document, update)
    #     self.logger.info("Updated one document from collection: %s", collection_name)

    # # update many documents
    # def update_many(self, collection_name, document, update):
    #     collection = self.get_collection(collection_name)
    #     result = collection.update_many(document, update)
    #     self.logger.info(
    #         "Updated %s documents from collection: %s",
    #         result.modified_count,
    #         collection_name,
    #     )

    # # delete one document
    # def delete_one(self, collection_name, document):
    #     collection = self.get_collection(collection_name)
    #     result = collection.delete_one(document)
    #     self.logger.info("Deleted one document from collection: %s", collection_name)

    # # delete many documents
    # def delete_many(self, collection_name, document):
    #     collection = self.get_collection(collection_name)
    #     result = collection.delete_many(document)
    #     self.logger.info(
    #         "Deleted %s documents from collection: %s",
    #         result.deleted_count,
    #         collection_name,
    #     )
