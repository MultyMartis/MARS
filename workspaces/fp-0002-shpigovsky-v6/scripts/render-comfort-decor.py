from pathlib import Path
from PIL import Image, ImageDraw

w, h = 383, 360
border = (71, 83, 113, 255)
img = Image.new("RGBA", (w, h), (255, 255, 255, 255))
draw = ImageDraw.Draw(img)
draw.rectangle([0, 0, w - 1, h - 1], outline=border, width=1)

workspace = Path(r"C:\AI MARS\workspaces\fp-0002-shpigovsky-v6")
out = workspace / "src/img/content/home-comfort/comfort-gallery-logo-decor.webp"
out.parent.mkdir(parents=True, exist_ok=True)

logo_path = workspace / "src/img/branding/logo.svg"
try:
    import cairosvg

    logo_png = out.parent / "_logo-temp.png"
    cairosvg.svg2png(url=str(logo_path), write_to=str(logo_png), output_width=180)
    logo = Image.open(logo_png).convert("RGBA")
    img.alpha_composite(logo, ((w - logo.width) // 2, (h - logo.height) // 2))
    logo_png.unlink(missing_ok=True)
except Exception:
    draw.text((96, 168), "Shpigovsky", fill=border)

rgb = Image.new("RGB", img.size, (255, 255, 255))
rgb.paste(img, mask=img.split()[3])
rgb.save(out, "WEBP", quality=86)
print(rgb.size[0], rgb.size[1])
