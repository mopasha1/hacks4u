from taipy.gui import Gui, navigate

index = """<|navbar|>"""
page_1 =  """
#TAIPY GUI TUTORIALS - Layouts

<|Expandable Description|expandable|expanded=False|
##How does it work? 
<|layout|columns= 1 3 2|

<|#Resources|>

<|#Courses|>

<|#Roadmaps|>
|>
|>
"""

page_2 = """
<|layout|columns=1 1 1|

    <|
###FIRST COLUMN

    |>

    <|
###SECOND COLUMN

    |>

    <|
###THIRD COLUMN
Button 1:  
 

Button 2:  


Button 3:  


|>
|>
"""


if __name__ == '__main__':
    pages = {
        "/":index,
        "Page-1" : page_1,
        "Page-2": page_2
    }
    gui = Gui(pages=pages)
    gui.run(dark_mode=False)
