"""
This represents the main execution of the benford calculator. 
"""
import os
import argparse
import structlog
from core import MainController


logger = structlog.get_logger(__name__)



def main(**kwargs):
    """
    This is the main function used to initiate the script
    Returns: None
    """
    config = {
        'file_name':kwargs["file"],
        'numeric_column':kwargs["numeric_column"]
    }
    try:
        logger.info("Setting up main controller")
        # make a delta calculator controller
        controller = MainController(configuration=config)
        #do ze workssss
        logger.info("Processing File List")
        controller.calculate_benford()
       
    except Exception as e:
        logger.error(e, exc_info=True)
    
    return

if __name__ == '__main__':

    import structlog_config
    #bootstrap logging & argparser
    structlog_config.configure_structlog(level=os.environ.get('LOGLEVEL', 'INFO'), development_mode=False)
    logger = structlog.get_logger(__name__)
    parser = argparse.ArgumentParser()

    parser.add_argument('-f', '--file',
                        help="""The file that contains the data to validate Benford's theorem""")
    parser.add_argument('-nc', '--numeric_column',
                        help="""The numeric column for which to sample Benford's theorem""")
    ARGS = parser.parse_args()
   
    PARAMS = {
        "file": ARGS.file or "",
        "numeric_column": ARGS.numeric_column or ""
    }
    main(**PARAMS)

