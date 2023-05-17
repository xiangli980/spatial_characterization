import openslide
import numpy as np

file_path = './neptune/13_26609_033_520 L01 HE.ndpi'
file = openslide.OpenSlide(file_path)
# show the levels
print(file.level_count)
# show the dimensions of each level
print(file.level_dimensions)