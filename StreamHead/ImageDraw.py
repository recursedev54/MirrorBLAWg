from PIL import Image, ImageDraw
import math
import os

def convert_to_rgb(hex_code):
    # Convert hexadecimal color code to RGB tuple
    hex_code = hex_code.lstrip("#")
    return tuple(int(hex_code[i:i+2], 16) for i in (0, 2, 4))

def create_color_wheel(values, format, size=300):
    color_codes = {
        'p': '#680164',  # Purple
        'b': '#0000FF',  # Blue
        'g': '#216216',  # Green
        'r': '#FF0000',  # Red
        'y': '#FFFF00',  # Yellow
        'c': '#00FFFF',  # Cyan
        'o': '#F5A000',  # Orange
        'l': '#8BB58F',  # Lime
        'e': '#808080',  # Extra (Grey)
        'd': '#808080',  # Grey
        'f': '#808080',  # Grey
        'h': '#808080',  # Grey
        'i': '#808080',  # Grey
        'j': '#808080',  # Grey
        'k': '#808080',  # Grey
        'm': '#808080',  # Grey
        'n': '#808080',  # Grey
        'q': '#808080',  # Grey
        's': '#808080',  # Grey
        't': '#808080',  # Grey
        'u': '#808080',  # Grey
        'v': '#808080',  # Grey
        'w': '#000000',  # Grey
        'x': '#808080',  # Grey
        'z': '#808080',  # Grey
        'a': '#FF69B4',  # Grey
        'P': '#680164',  # Purple
        'B': '#0000FF',  # Blue
        'G': '#216216',  # Green
        'R': '#FF0000',  # Red
        'Y': '#FFFF00',  # Yellow
        'C': '#00FFFF',  # Cyan
        'O': '#F5A000',  # Orange
        'L': '#8BB58F',  # Lime
        'E': '#808080',  # Extra (Grey)
        'D': '#808080',  # Grey
        'F': '#808080',  # Grey
        'H': '#808080',  # Grey
        'I': '#808080',  # Grey
        'J': '#808080',  # Grey
        'K': '#808080',  # Grey
        'M': '#808080',  # Grey
        'N': '#808080',  # Grey
        'Q': '#808080',  # Grey
        'S': '#808080',  # Grey
        'T': '#808080',  # Grey
        'U': '#808080',  # Grey
        'V': '#808080',  # Grey
        'W': '#808080',  # Grey
        'X': '#808080',  # Grey
        'Z': '#808080',  # Grey
        'A': '#808080'   # Grey
    }

    angle_step = 360 / len(format)
    image = Image.new("RGB", (size, size), "black")
    draw = ImageDraw.Draw(image)
    radius = size // 2
    center = (size // 2, size // 2)
    
    for i, channel in enumerate(format):
        angle = math.radians(i * angle_step)
        x = int(center[0] + radius * math.cos(angle))
        y = int(center[1] + radius * math.sin(angle))
        hex_code = color_codes[channel]
        rgb = convert_to_rgb(hex_code)
        intensity_modifier = round(values[i] * 255)
        rgb = tuple(int(rgb_component * intensity_modifier / 255) for rgb_component in rgb)
        draw.ellipse((x - 42, y - 42, x + 42, y + 42), fill=rgb)

    image.save("color_wheel.png")
    os.system("color_wheel.png")

# Test the function with the corrected format string and additional color codes
input_values = [.61, .61, .61, .61, .61, .61, .61, .61, .61, .61, .61]
format_string = "ppbbggrrccmmyyoolleekw"
create_color_wheel(input_values, format_string)