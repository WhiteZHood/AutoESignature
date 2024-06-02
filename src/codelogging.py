import logging
import logging.config
import storingfiles as sf


logging_config = sf.load_json_file("src/logging/loggingconfig.json")
logging.config.dictConfig(config=logging_config)
