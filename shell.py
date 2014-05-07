import sys
from snitch import config
from snitch.storage import DatabaseMixin

config_file = 'snitch.conf'
conf = config.parse_config(config_file)

data = DatabaseMixin()
data.sync_db(conf)
sqlite = data.sqlite
