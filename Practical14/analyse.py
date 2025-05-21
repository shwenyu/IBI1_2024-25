import xml.dom.minidom  # Import the DOM parser for XML
import xml.sax  # Import the SAX parser for XML
import time  # Import the time module for performance measurement
import os  # Import the os module for file and directory operations

os.chdir('Practical14')  # Set the current working directory to 'Practical14'
xml_file = 'go_obo.xml'  # Define the XML file name
NAMESPACES_TO_TRACK = [  # Define the namespaces to track
    "molecular_function",  # Namespace for molecular functions
    "biological_process",  # Namespace for biological processes
    "cellular_component"  # Namespace for cellular components
]

def parse_xml_dom(file):  # Parse the XML file using DOM parser and print the number of terms
    print(f"\n--- Starting Analysis with DOM API ---")  # Print start message
    start_time = time.perf_counter()  # Record the start time
    domtree = xml.dom.minidom.parse(file)  # Parse the XML file into a DOM tree
    collection = domtree.documentElement  # Get the root element of the DOM tree
    terms = collection.getElementsByTagName("term")  # Get all "term" elements
    result_mulecular_function = {}  # Initialize dictionary for molecular functions
    result_biological_process = {}  # Initialize dictionary for biological processes
    result_cellular_component = {}  # Initialize dictionary for cellular components
    result = {  # Combine all dictionaries into a single result dictionary
        "molecular_function": result_mulecular_function,  # Map molecular functions
        "biological_process": result_biological_process,  # Map biological processes
        "cellular_component": result_cellular_component  # Map cellular components
    }
    for node in terms:  # Iterate through each "term" element
        #node_id = node.getElementsByTagName("id")[0].childNodes[0].nodeValue  # Get the term ID
        node_name = node.getElementsByTagName("name")[0].childNodes[0].nodeValue  # Get the term name
        node_namespace = node.getElementsByTagName("namespace")[0].childNodes[0].nodeValue  # Get the term namespace
        is_a = node.getElementsByTagName("is_a")  # Get all "is_a" elements
        len_is_a = is_a.length  # Count the number of "is_a" elements
        result[node_namespace][node_name] = len_is_a  # Store the count in the result dictionary
    for i in NAMESPACES_TO_TRACK:  # Iterate through each namespace to track
        max_count = max(result[i].values())  # Find the maximum count in the namespace
        max_key = [k for k, v in result[i].items() if v == max_count]  # Find the term(s) with the maximum count
        print(f"Max count for {i}: {max_count} for {max_key}")  # Print the maximum count and corresponding terms

    end_time = time.perf_counter()  # Record the end time
    duration = end_time - start_time  # Calculate the duration of the analysis
    print(f"--- Analysis completed in {duration:.2f} seconds ---")  # Print the duration
    return duration  # Return the duration

def parse_xml_sax(file):  # Parse the XML file using SAX parser and print the number of terms
    print(f"\n--- Starting Analysis with SAX API ---")  # Print start message
    start_time = time.perf_counter()  # Record the start time
   
    class CoHandler(xml.sax.ContentHandler):  # Define a custom SAX content handler
        def __init__(self):  # Initialize the handler
            self.current_data = ""  # Track the current XML element
            result_mulecular_function = {}  # Initialize dictionary for molecular functions
            result_biological_process = {}  # Initialize dictionary for biological processes
            result_cellular_component = {}  # Initialize dictionary for cellular components
            self.result = {  # Combine all dictionaries into a single result dictionary
                "molecular_function": result_mulecular_function,  # Map molecular functions
                "biological_process": result_biological_process,  # Map biological processes
                "cellular_component": result_cellular_component  # Map cellular components
            }
            self.namespace = ""  # Initialize the namespace
            self.name = ""  # Initialize the term name
            self.is_a_count = 0  # Initialize the "is_a" count

        def startElement(self, name, attrs):  # Handle the start of an XML element
            self.current_data = name  # Update the current element name
            if self.current_data == "term":  # If the element is a "term"
                self.name = ""  # Reset the term name
                self.namespace = ""  # Reset the namespace
                self.is_a_count = 0  # Reset the "is_a" count
            if self.current_data == "is_a":  # If the element is "is_a"
                self.is_a_count += 1  # Increment the "is_a" count
       
        def characters(self, content):  # Handle the text content of an XML element
            if self.current_data == "name":  # If the current element is "name"
                self.name += content  # Append the content to the term name
            elif self.current_data == "namespace":  # If the current element is "namespace"
                self.namespace += content  # Append the content to the namespace
            
        def endElement(self, name):  # Handle the end of an XML element
            if name == "name":  # If the element is "name"
                self.name = self.name #.strip()  # Strip whitespace from the term name
            elif name == "namespace":  # If the element is "namespace"
                self.namespace = self.namespace #.strip()  # Strip whitespace from the namespace
            elif name == "term":  # If the element is "term"
                if self.namespace in NAMESPACES_TO_TRACK and self.name:  # If the namespace is tracked and the name is valid
                    self.result[self.namespace][self.name] = self.is_a_count  # Store the "is_a" count in the result dictionary
            self.current_data = ""  # Reset the current element name

    parser = xml.sax.make_parser()  # Create a SAX parser
    parser.setFeature(xml.sax.handler.feature_namespaces, 0)  # Disable namespace handling
    handler = CoHandler()  # Create an instance of the custom handler
    parser.setContentHandler(handler)  # Set the custom handler for the parser
    parser.parse(file)  # Parse the XML file
    for i in NAMESPACES_TO_TRACK:  # Iterate through each namespace to track
        namespace_dict = handler.result[i]  # Get the result dictionary for the namespace
        max_count = max(namespace_dict.values())  # Find the maximum count in the namespace
        max_key = [k for k, v in namespace_dict.items() if v == max_count]  # Find the term(s) with the maximum count
        print(f"Max count for {i}: {max_count} for {max_key}")  # Print the maximum count and corresponding terms
   
    end_time = time.perf_counter()  # Record the end time
    duration = end_time - start_time  # Calculate the duration of the analysis
    print(f"--- Analysis completed in {duration:.2f} seconds ---")  # Print the duration
    return duration  # Return the duration

time_dom = parse_xml_dom(xml_file)  # Call the function to parse the XML file using DOM
time_sax = parse_xml_sax(xml_file)  # Call the function to parse the XML file using SAX
if time_dom < time_sax:  # Compare the durations of the two parsers
    print(f"DOM parser is faster by {time_sax - time_dom:.2f} seconds")  # Print the result if DOM is faster
else:  # If SAX is faster
    print(f"SAX parser is faster by {time_dom - time_sax:.2f} seconds")  # Print the result if SAX is faster
# The SAX parser is generally faster for large XML files due to its event-driven nature,
# while the DOM parser loads the entire document into memory, which can be slower.