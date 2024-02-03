import json as JSON

"""

I feel that I must apologise for any bugs in the code below.
Please let me know if you find any bugs at itshollyevergreen@gmail.com on GitHub 
or HollyEvergreen on Itch.io or Discord @pennyevolus or in the Yggdrasil Studios
Community Discord at https://discord.gg/Z4jKn4VdRV in the #bug-reports forum channel.

"""



class Parse:
    class yggDataToJSON:
        def __init__(self, *args):
            for arg in args:
                pass
        
        def Convert(self, f: str) -> str:
            """
            A method to convert the given data file to a JSON file.
            Args:
                f (str): The file path to be converted.
            Returns:
                The FilePath to the converted JSON file.
            """
            filepath = f.split(".")[0] + ".json"
            with open(filepath, 'w') as file:
                file.write(JSON.dumps(Parse.yggDataParser().Parse(f)))
            return filepath
    class yggDataParser:
        def __init__(self, *args):
            for arg in args:
                pass

        def Parse(self, f: str) -> dict:
            """
            A method to parse the given data file, 
            sanitize the data, and put it in the 
            correct format for data processing.
            Args:
                f (str): The file path to be parsed.
            Returns:
                the data from the file in the correct format for data processing.
            """
            
            with open(f, 'r') as file:
                d:List[str] = file.readlines()
            
            # This for loop is going through each line of the *.yyg file to sanitize the data in
            # the file and put it in the correct format for the data process pass.
            for line in range(len(d)):
                # The code below is removing linebreaks from the current line of the *.yyg file.
                # It is doing this as the lines are already in seperate strings
                if '\n' in d[line]:
                    d[line] = d[line].replace('\n', '')
            
            header = False 
            
            """
            {
                'format': [
                    'DATA1 name',
                    'DATA2 name',
                    ...,
                    'DATAn name'
                ],
                units = {
                'DATA1 name' : 'units',
                'DATA2 name' : 'units',
                ...,
                'DATAn name' : 'units',
                }
                'index': {
                    'DATA1 name': DATA1,
                    'DATA2 name': DATA2,
                    ...,
                    'DATAn name': DATAn
                }
            }
            """
            # The DataDict:(dict) object is used to store the processed data in the above format
            DataDict = {}
            FormatMap = {}
            UnitsMap = {}
            DataMap = {}
            DataCollection = {}
            
            
            # This for loop is going through each line of the file to process the Data inside it.
            # It uses the '#HEADER' directive to know where the format header starts. It also
            # uses the #StartOfData and #EndOfData directives to know where the data exists.
            DataDictIndex = 0
            for line in d:
                if line.startswith('#'):
                    # This checks if the line is a directive this parses the directive safely as
                    # some directives can have arguments in them. this method allows us to parse
                    # the directive without the arguments increasing the complexity of the code.
                    match line.split(' ')[0]:
                        case '#HEADER':
                            # Set the header to true to indicate we are processing the header
                            header = True
                        case '#StartOfData':
                            # Set the header to false to indicate we are processing the data
                            header = False
                            
                            # Add the format and units to the Data dictionary
                            DataDict['format'] = FormatMap['format']
                            DataDict['units'] = UnitsMap
                        case '#EndOfData':
                            # Add the data to the Data dictionary and return it
                            DataDict['DATA'] = DataCollection
                            return DataDict
                else:

                    # This checks if the line is in the header of the file or not.
                    if header:

                        # this code checks if the line is a format specifier
                        if line.startswith('['):
                            # Create The Data Format
                            line = line.lstrip('[')
                            line = line.rstrip(']')
                            dataFormat = line.split(',')
                            # Add the data format to the format map
                            FormatMap['format'] = dataFormat

                        # This code checks if the line is a units specifier
                        elif line.startswith('{'):
                            UnitsMap.update(JSON.loads(line))

                    else:
                        DataDictIndex += 1 # increment the index of the data being written to the data dictionary
                        for name in enumerate(dataFormat):
                            DataMap[name[1]] = line.split(',')[name[0]]
                        
                        DataCollection[str(DataDictIndex)] = DataMap