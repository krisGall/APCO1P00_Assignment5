# Name         : Kristopher Gall
# ID           : 7356942
# Assignment   : 5
# Part         : 1 out of 1
# Date         : December 2, 2022

from bs4 import BeautifulSoup

soup = BeautifulSoup(open("big_data.html"), "html.parser")
my_file = open("output.html", "w")

###############################################################################
# It is advised to not alter the functions found below.
###############################################################################

# starts an HTML tag
def begin(tag_name: str) -> None:
  my_file.write("<" + tag_name + ">")
  my_file.write("\n")

# ends an HTML tag
def end(tag_name: str) -> None:
  my_file.write("</" + tag_name + ">")
  my_file.write("\n")

# used to write some text inside HTML tag
def write(text: str) -> None:
  my_file.write(text)

# creates an SVG tag with the width and height
def begin_svg(width: int, height: int) -> None:
  my_file.write("<svg " + 
    get_attribute("width", str(width)) + 
    get_attribute("height", str(height)) +
    ">"
  )
  my_file.write("\n")

# ends the SVG tag
def end_svg() -> None:
  my_file.write("</svg>")
  my_file.write("\n")

# adds an attribute for SVG image
def get_attribute(name: str, value: str) -> str:
  return " " + name + "=\"" + value + "\" "

# writes an SVG line
def line(x1: int, y1: int, x2: int, y2: int, stroke: str) -> None:
  my_file.write("<line " + 
    get_attribute("x1", str(x1)) +
    get_attribute("y1", str(y1)) + 
    get_attribute("x2", str(x2)) + 
    get_attribute("y2", str(y2)) + 
    get_attribute("stroke", stroke) +
    "></line>"
  )
  my_file.write("\n")

###############################################################################
# Add code here...
###############################################################################

###############################################################################
# My functions
###############################################################################

def circle(cx: int, cy: int, r: int, fill: str, stroke: str) -> None:
    ''' Creates a circle at position given with colors given
    cx = circle x pos
    cy = circle y pos
    r = radius length
    fill = fill color
    stroke = line color'''
    my_file.write("<circle cx=\"" + str(cx) + "\"" +
                  "cy=\"" + str(cy) + "\"" +
                  "r=\"" + str(r) + "\"" +
                  "fill=\"" + fill + "\"" +
                  "stroke=\"" + stroke + "\"" +
                  "/>")
    my_file.write("\n")

def get_data() -> list:
    ''' Finds all td tags in the current souped data and
    stores the values as an integer and returns the list'''
    table_elements: list = soup.find_all("td")
    table_elements_int: list = []
    for element in table_elements:
        table_elements_int.append(int(element.string))
    return table_elements_int

def get_average(values: list) -> float():
    '''Takes a list of values and returns their average
    values = list of values to average'''
    total: int = 0
    for value in values:
        total += value
    average: float = total/len(values)
    return average

def get_min(values: list) -> int():
    ''' Takes a list of values and returns the minimum value
    values = list of values to find min of'''
    current_min: int = None
    for value in values:
        # Getting first value
        if current_min == None:
            current_min = value
        # Replacing current min if value is lower
        if current_min > value:
            current_min = value
    return current_min

def get_max(values: list) -> int():
    ''' Takes a list of values and returns the maximum value
    values = list of values to find max of'''
    current_max: int = None
    for value in values:
        # Getting first value
        if current_max == None:
            current_max = value
        # Replacing current max if value is higher
        if current_max < value:
            current_max = value
    return current_max

def write_required_values(minimum: int, maximum: int, average: float):
    ''' Writes the minimum, maximum and average into the file all
    stored in a html <div> tag
    minimum = lowest value
    maximum = highest value
    average = average value '''
    begin("div")
    begin("div")
    write("<b> The minimum value is </b><i>"  + str(minimum) + "</i>\n")
    end("div")
    begin("div")
    write("<b> The maximum value is </b><i>" + str(maximum) + "</i>\n")
    end("div")
    begin("div")
    write("<b> The average value is </b><i>" + str(average) + "</i>\n")
    end("div")
    end("div")

##############################################################################
# Script
##############################################################################

# Calculating required values
values: list = get_data()
average_value: float = get_average(values)
min_value: int = get_min(values)
max_value: int = get_max(values)

# Generating HTML
begin("html")
begin("head")
end("head")
begin("body")

## Creating the circles
begin_svg(200,500)
circle(50,100,20,"red","blue")
circle(150,400,30,"green","orange")
end_svg()

## Outputting the required values
write_required_values(min_value, max_value, average_value)
end("body")
end("html")

my_file.close()
