"""
The main entrypoint into the application.
"""
import structlog
from .benford import BenfordCalculator
logger = structlog.get_logger(__name__)


class MainController:
    """
    The MainController class represents the main entrypoint
    into the application. This handles injecting the data and
    setting up the process flow for the main processes 
    """
    def __init__(self, configuration):
        """
        :param configuration: is a dictionary with the configuration values. It looks like:
                        {
                            'file_name': '',
                            'numeric_column': ''
                        }
        """
        self.configuration = configuration

        logger.debug(self.configuration)

    def calculate_benford(self):
        """
        Calculates the Benford law output for a given input file and 
        prints the results to stdout
        :return: None
        """
        calculator = BenfordCalculator(self.configuration)
        calculator.process_file()
        return calculator.print_output()

 