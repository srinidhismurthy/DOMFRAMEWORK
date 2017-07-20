import logging
import inspect

def fileLogger(loglevel=logging.INFO):
    loggername=inspect.stack()[1][3]
    # create logger object
    logger=logging.getLogger(loggername)
    logger.setLevel(logging.INFO)
    #Create console Handler for Logger Object
    fileHandler=logging.FileHandler(filename="Mylogs.log",mode='w')
    fileHandler.setLevel(loglevel)

    # Create a formatter
    formatter=logging.Formatter("%(asctime)s,%(name)s,%(levelname)s,%(message)s",datefmt="%d/%m/%Y %I:%M:%S %p")

    # Set the formater to the Handler
    fileHandler.setFormatter(formatter)

    # Add handler to the object.
    logger.addHandler(fileHandler)

    return logger


def consoleLogger(loglevel=logging.INFO):
    loggername=inspect.stack()[1][3]
    # create logger object
    logger=logging.getLogger(loggername)
    logger.setLevel(logging.INFO)
    #Create console Handler for Logger Object
    cHandler=logging.StreamHandler()
    cHandler.setLevel(loglevel)

    # Create a formatter
    formatter=logging.Formatter("%(asctime)s-%(name)s-%(levelname)s-%(message)s",datefmt="%d/%m/%Y %I:%M:%S %p")

    # Set the formater to the Handler
    cHandler.setFormatter(formatter)

    # Add handler to the object.
    logger.addHandler(cHandler)


    return logger








