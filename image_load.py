from pma_python import *

# connect to the local PMAhost
session_ID = connect("http://localhost:54001/")

# path to slide directory
slide_dir = "Root/home/pgrylls/Documents/RSG/Cancer-Slide/test_image"

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

# get the information for the current slide
slide_info = get_slide_info(slides[0], sessionID=session_ID)
# get the information for the current slide
slide_files = get_files_for_slide(slides[0], sessionID=session_ID)

print(slide_info)

slide_width = slide_info['Width']
slide_height = slide_info['Height']

# set the size of the output tiles
output_tile_size = 1024
trim_w = slide_width % output_tile_size
trim_h = slide_height % output_tile_size
trim_w_t = trim_w // 2
trim_w_b = trim_w // 2 + (trim_w % 2)
trim_h_t = trim_h // 2
trim_h_b = trim_h // 2 + (trim_h % 2)

# Load the image using pillow: https://pillow.readthedocs.io/en/stable/reference/Image.html
slide_tiles = get_tiles(slides[0], fromX=trim_w_t, toX=trim_w_b, fromY=trim_h_t, toY=trim_h_b)
print(slide_tiles)

for tile in slide_tiles:
    print("a")
    print(tile)
