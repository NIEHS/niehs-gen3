import os
from dictionaryutils import DataDictionary as GDCDictionary

#SCHEMA_DIR = '/Users/pateldes/Documents/gitlab/niehs-gen3/data-model-ods/ver-1.1/gdictionary/schemas'

SCHEMA_DIR = os.path.join(
    os.path.abspath(os.path.dirname(__file__)), 'schemas')
gdcdictionary = GDCDictionary(root_dir=SCHEMA_DIR)

