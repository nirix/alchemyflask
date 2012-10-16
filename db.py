import yaml
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Attempt to load the settings file
try:
    conf_file = open('settings.yml')
    conf = yaml.load(conf_file)
    conf_file.close()
except:
    raise Exception('Error loading settings.yml')

engine = create_engine(conf['database'])
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()
