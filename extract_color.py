import os
from PIL import Image
import webcolors
import json
import time

image = input("Which image you want to process: ")
start_time = time.perf_counter()

def is_path(image):
    return os.path.exists(image)

def change_path(path):
    os.chdir(path)

def get_resolution(image):
    img = Image.open(image)
    width = img.width
    height = img.height
    pixel_number = width * height
    return width, height, pixel_number, img

def processing(img, width, height):
    pixels = img.load()
    first_color = pixels[0, 0]
    second_color = pixels[width - 1, height - 1]
    third_color = pixels[width // 2, height // 2]
    return first_color, second_color, third_color

def rgb_hex(first_color, second_color, third_color):
    hex_color1 = webcolors.rgb_to_hex(first_color)
    hex_color2 = webcolors.rgb_to_hex(second_color)
    hex_color3 = webcolors.rgb_to_hex(third_color)
    return hex_color1, hex_color2, hex_color3

def store_color_json(common_color):
    os.system("touch color.json")
    color_data = {"common_color": common_color}
    with open("color.json", "w") as file:
        json.dump(color_data, file)
    print('All Done...')

if is_path(image):
    width, height, pixel_number, img = get_resolution(image)
    first_color, second_color, third_color = processing(img, width, height)
    hex_color1, hex_color2, hex_color3 = rgb_hex(first_color, second_color, third_color)
    common_color = f"{hex_color1}, {hex_color2}, {hex_color3}"
    store_color_json(common_color)
    end_time = time.perf_counter()
    elapsed_time = round(end_time - start_time, 2)
    print(f"Time taken: {elapsed_time} seconds")
else:
    path = input("Please Insert Your Image Directory: ")
    change_path(path)
    print("Directory Has Been Changed")
