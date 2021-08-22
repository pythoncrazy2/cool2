import textwrap
from io import BytesIO

from PIL import Image, ImageDraw, ImageFont, ImageOps, ImageSequence

def caption(fn: str, text: str):
    old_im = Image.open(fn)
    ft = "gif"
    font = ImageFont.truetype('.//Fonts//One-Regular.ttf', 50)

    width = 10
    while True:
        lines = textwrap.wrap(text, width=width)
        if (font.getsize(lines[0])[0]) > old_im.size[0]:
            break
        width += 4

    lines = textwrap.wrap(text, width=width - 10)
    bar_height = (len(lines) + 1) * (font.getsize(lines[0])[1]) + 15
    print(bar_height)

    frames = []
    for frame in ImageSequence.Iterator(old_im):
        frame = ImageOps.expand(
        frame,
        border=(0,int(bar_height),0,0),
        fill="white"
    )
        draw, y = ImageDraw.Draw(frame), 15
        for line in lines:
            w, _ = draw.textsize(line, font=font)
            draw.text(
                ((old_im.size[0] - w) / 2, y),
                line,
                font=font,
                fill='green'
            )
            y += 50
        del draw
        b = BytesIO()
        frame.save(b, format=ft)
        frames.append(Image.open(b))

    frames[0].save(
        f'out.{ft}',
        save_all=True,
        append_images=frames[1:],
        format=ft,
        loop=0,
    )

caption(
    '1984.gif',"work fucking dammit")