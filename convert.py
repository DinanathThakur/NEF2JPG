import os
import rawpy
import imageio
from tqdm import tqdm

def convert_nef_to_jpg(input_folder_path, output_folder_path):
    files = [f for f in os.listdir(input_folder_path) if f.endswith(".NEF")]
    for filename in tqdm(files, desc="Converting NEF to JPG"):
        nef_path = os.path.join(input_folder_path, filename)
        jpg_filename = os.path.splitext(filename)[0] + ".jpg"
        jpg_path = os.path.join(output_folder_path, jpg_filename)
        
        with rawpy.imread(nef_path) as raw:
            rgb = raw.postprocess()
        imageio.imsave(jpg_path, rgb, quality=90)
    print("Conversion completed!")

# Usage example
input_folder_path = "<source folder>"
output_folder_path = "<destination folder>"
convert_nef_to_jpg(input_folder_path, output_folder_path)
