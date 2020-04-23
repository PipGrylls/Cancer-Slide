from pma_python import *

# connect to the local PMAhost
session_ID = connect("http://localhost:54001/")

# path to slide directory
slide_dir = "Root/Users/pgrylls/PycharmProjects/CancerImage/test_image"

# get a list of directories avalible to the session in the slide directory
dirs = get_directories(slide_dir)
print(dirs)

# get a list of slides avalible to the session in the slide directory
# set recursion to true if subdirectories are needed
dirs = get_directories(slide_dir, sessionID=session_ID, recursive=False)

print(dirs)


# get a list of slides avalible to the session in the slide directory
# set recursion to true if subdirectories are needed
slides = get_slides(slide_dir, sessionID=session_ID, recursive=False)

print(slides)

# get the information for the current slide
slide_info = get_slide_info(slides[0], sessionID=session_ID)

print(slide_info)

slide_files = get_files_for_slide(slides[0], sessionID=session_ID)

print(slide_files)

tile = get_tile(slides[0])

print(tile)
