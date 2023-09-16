from PIL import Image, ImageDraw, ImageFont
import random

font_size = 72
font_colour = 'black'
font_path = './assets/ArimoNerdFont-Bold.ttf'
font_var = ImageFont.truetype(font_path, font_size)

max_width = 900
font_height = 60
line_spacing = 12

def create_list(input: str):
    options_list = []
    if not input.isprintable():
        raise Exception(r">:(")
        
    for option in input.split(','):
        if option.startswith(' ') or option.endswith(' '): # I just realized this doesn't work. Gotta be smarter than this lol. #Nvm somehow it works. I tought it would replace all spaces in the entire isolated string
            option.replace(' ', '')
            options_list.append(option)
        else:
            options_list.append(option)
    return options_list

def randomize(opt_list: list):
    range_val = len(opt_list) - 1
    result = opt_list[random.randint(0, range_val)]
    return result

def draw_result(result: str):
    lines = []
    line = []
    if not result.isprintable():
        raise Exception(r">:(")
    
    box = font_var.getbbox(result)
    if box[2] <= max_width:
        #draw canvas and add text
        canvas = Image.new('RGB', (1000, 140), color='white')
        draw = ImageDraw.Draw(canvas)
        draw.text((50, 40), text=result, fill='black', font=font_var, align='center')
        return canvas

    else:
        y = 40
        words = result.split(' ')

        for word in words:
            test_line = line + [word]
            test_text = ' '.join(test_line)
            text_width = font_var.getbbox(test_text)

            if text_width[2] <= max_width:
                line = test_line
            else:
                lines.append(' '.join(line))
                line = [word]

        if line:
            lines.append(' '.join(line))

        dyn_y = 80 + (len(lines) * (font_height + line_spacing) - line_spacing)
        canvas = Image.new('RGB', (1000, dyn_y), color='white')
        draw = ImageDraw.Draw(canvas)

        for line in lines:
            draw.text((50, y), text=line, fill='black', font=font_var, align='center')
            y += font_height + line_spacing

        return canvas
    
def merge_result(canvas: Image):
    biboo = Image.open('./assets/bijouthumbsup_by_zephylyne.jpg')
    height = canvas.height
    merge_canvas = Image.new('RGB', (1000, 1000 + height))
    merge_canvas.paste(canvas, (0, 0))
    merge_canvas.paste(biboo, (0, height))
    return merge_canvas

if __name__ == '__main__':
    base_string = input('Enter your options separated by a comma for each:')
    testlist = create_list(base_string)
    res = randomize(testlist)
    text_canv = draw_result(res)
    final_image = merge_result(text_canv)
    final_image.save('wisdom_of_biboo.jpg')
    final_image.show()

    