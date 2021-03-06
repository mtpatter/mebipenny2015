import sys

## Chromakey is a technique to replace all pixels in an image that fall in a
## certain color range with the pixels from another image. In other words, a green
## screen.

## Input: The first two lines consist of one integer each, width W and height H of the
## images to follow, each between 1 and 256. After that, each line will consist of
## three numbers R G and B, each between 0 and 255. There will be W x H lines for
## the first (base) image, and then another W x H lines for the second (overlay)
## image.

## Output: For every pixel in the first image where the Green
## value is greater than the combined Red and Blue value, replace that pixel with
## the corresponding pixel from the second image. Every other pixel remains
## unchanged in the output.

## For example:

## STDIN:

# 2
# 2
# 75 35 5
# 15 255 35
# 12 46 35
# 16 48 5
# 0 0 0
# 15 75 30
# 5 25 3
# 0 4 0

## STDOUT:

## 75 35 5
## 15 75 30
## 12 46 35
## 0 4 0

def process(base, overlay):
  # Process each line of input here
  rgb = base.split()
  screen = overlay.split()
  if int(rgb[1]) > (int(rgb[0])+int(rgb[2])):
    rgb = screen
  rgb= ' '.join(rgb)
  return rgb

lines = sys.stdin.readlines()
width = int(lines[0])
height = int(lines[1])

imbase = lines[2:width*height+2]
imoverlay = lines[width*height+2:]

processed = map(process, imbase, imoverlay)
for line in processed:
    print line.strip()

