"""
Benford Laws Calculator
"""
import json
import structlog
import csv

logger = structlog.get_logger(__name__)

class BenfordCalculator:
    """
    This class represents a Benford Laws Calculator. This calculator
    works on an input tsv file, and will allow a user to specify which
    fields are numerical
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
        #Define the output frequency map for first digit values
        self.raw_benford_output = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}
        #keep track of the number of digits we successfully extracted, so we don't have to do another loop
        self.item_count = 0
    
    def get_raw_output(self):
        """
        Accessor to the raw_benford_output property
        Returns populated dictionary with first digit counts
        eg  {1:3,2:6,3:4,4:0,5:0,6:0,7:0,8:0,9:0}
        """
        return self.raw_benford_output

    def print_output(self):
        """
        :return: prints the output to stdout in tab-separated format
        :todo: write to a file if that is requested
        """
        print("Digit    Count   %")
        for item in self.raw_benford_output:
            digit = item
            count = self.raw_benford_output[item]
            percentage = (count / self.item_count)*100
            print("{}   {}  {:.1f}".format(str(digit), str(count), percentage))
        return 

    @staticmethod
    def get_header_indices(header_row, numeric_column_name):
        """
        :return: returns dictionary mapping the numeric column name to its index in the header row
        :rtype: dictionary[string]int
        """
        column_indexes = {}
        index=0
        for item in header_row:
            if item == numeric_column_name:
                column_indexes[numeric_column_name] = index
            
            index+=1        

        if not column_indexes:
            raise Exception("invalid numeric column name")

        logger.debug(json.dumps(column_indexes))
        return column_indexes


    def process_file(self):
        """
        Processes a file and applies the Benford principle to its contents
        Data gets saved to the raw_benford_output property
        """
        logger.info("Start Processing the File ")
        with open(self.configuration['file_name'], 'r') as tsv_file:
            logger.info("Loading file...")
            reader = csv.reader(tsv_file, delimiter='\t')
                      
            # read CSV headers
            try:
                headers = next(reader)
            except:
                raise Exception("No data to process")

            #get column indexes matching the column headers from the first row in the flat file
            logger.debug(self.configuration['numeric_column'])
            
            column_indexes = self.get_header_indices(header_row=headers, 
                                                     numeric_column_name=self.configuration['numeric_column'])

            # read rest of file
            for row in reader:
                #check to see if the row has an index matching the numeric column index
                if len(row) > column_indexes[self.configuration['numeric_column']]:
                    logger.debug("processed row " + str(self.item_count))
                    #get first digit of the numeric column string
                    try:
                        first_digit = int(str(row[column_indexes[self.configuration['numeric_column']]])[:1])
                        self.raw_benford_output[first_digit] += 1
                        self.item_count += 1
                    except ValueError:
                        #Handle the exception and carryon
                        logger.error("non-numeric data in numeric column: " + json.dumps(row))
                else:
                    #log the row if we can't find a matching index 
                    logger.warn("no numeric data found in row: " +json.dumps(row))
               
