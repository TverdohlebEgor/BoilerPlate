Boilerplate_selenium(object)

A simple way to make faster create selenium applications
With Selenium you generaly want to make only 3 action:
-Click a button
-Get text from a label
-Input text into an input
And this boilerplate concentrate on this stuff:

Boilerplate_selenium(browser,debug):
Instanciate the class with browser:
-Chrome
-Firefox (default)
-Edge
-Safati
Debug:
-True (default)
-False -> make the window of the browser not appear

simple_connect(url,timeout):
Make a "stupid" connection that is based on a timeout to "wait" until is loaded
If it don't load in time it will lead to an Error
Url:
"http://google.com" (defualt)
The url of the page
timeout -> int (10 default)

smart_connect(url,timeout):
Make a "smart" connection that wait until the body part of html is loaded. After that it waits
other 3 second to good measure. The timeout is obligatory and it determines when the connection
stop if it not load in timeout.
Url:
"http://google.com" (defualt)
The url of the page
timeout -> int (20 default)

close_connection():
It closes the connection

simple_button_click(XPATH):
It clicks the button at XPATH

get_label_text(XPATH):
It gets the label at XPATH

get_labels_text(XPATH):
It gets multiple labels and return them in a list at XPATH (intended for id of common objects)

get_title_page():
return title of the page

simple_input(input,XPATH):
insert the input at XPATH

get_attribute(attribute,XPATH):
it get the attribute at XPATH E.G

<video tabindex="-1" class="video-stream html5-main-video" controlslist="nodownload" style="width: 853px; height: 480px; left: 0px; top: 0px;" src="blob:https://www.youtube.com/a95cb0f5-b254-43a4-b6df-648b3f32e81c"></video>

get_attribut("src",XPATH) return the "blob:https://www.youtube.com/a95cb0f5-b254-43a4-b6df-648b3f32e81c"

stupid_scroll_to_bottom(max_scrools):
scrool to the bottom of the page "stupidly" because it goes down X (default 30) time

smart_scroll_to_bottom():
It goes down until it is at the bottom, for some rare town it doesn't work (like youtube)
