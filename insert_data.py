# Import our pymongo library, which lets us connect our Flask app to our Mongo database.
import pymongo
import scrape_mars

# Create connection variable
conn = 'mongodb://localhost:27017'

# Pass connection to the pymongo instance.
client = pymongo.MongoClient(conn)

# Connect to a database. Will create one if not already available.
db = client.mydatabase
collection = db.mars

data = scrape_mars.scrape()

collection.insert(data)