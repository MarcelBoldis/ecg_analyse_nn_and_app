try:
    import sys
    from flask_pymongo import PyMongo
except ValueError:
    print("Modules loading failed in " + sys.argv[0])

setup = {
    'DB_NAME': 'ECG_Datasets',
    'COLLECTION_NAME': 'ECG_Data'
}
