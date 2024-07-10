#!/bin/bash

echo "Running the following command to install the 'typing_extensions' module using pip:"
echo ""
pip install typing-extensions
pip install pyfiglet
pip install pytz
pip install colorama

echo ""
echo "Alternatively, if you're using a specific Python version, you might need to use pip3:"
echo ""
pip3 install typing-extensions
pip3 install pyfiglet
pip3 install pytz
pip3 install colorama

echo ""
echo "Installation complete."
read -p "Press Enter to exit."