import os
import shutil

import tqdm
from PIL import Image
from nicegui import ui

images_loc = R"C:\Users\dakot\OneDrive\Pictures\Show pics"
static = R"C:\Users\dakot\Acropolis\static"

shutil.rmtree(static)
os.mkdir(static)

images = []
i = 1
for dirpath, dirnames, filenames in os.walk(images_loc):
    for filename in filenames:
        base, ext = os.path.splitext(filename)
        path = os.path.join(dirpath, filename)
        try:
            img = Image.open(path)
        except Exception as e:
            print(f"Had an error loading an image: {e}")
            continue
        path = os.path.join(static, filename)
        # img_w, img_h = img.size
        # factor = 1000 / img_w
        # small_w = int(img_w * factor)
        # small_h = int(img_h * factor)
        # img = img.resize((small_w, small_h))
        img.save(path)
        obj = {}
        obj["name"] = base
        obj["path"] = path
        obj["ext"] = ext
        obj["tag"] = os.path.split(dirpath)[1]
        images.append(obj)


@ui.page("/")
def homePage():
    with ui.row().classes("w-full flex justify-center"):
        ui.label("Photography by Dakota Winslow").classes("text-xl")

    with ui.element("div").classes("columns-3 w-full gap-2"):
        for obj in images:
            tailwind = f"mb-2 p-2] break-inside-avoid"
            with ui.card().classes(tailwind):
                ui.image(obj["path"])
                ui.label(obj["name"]).classes("text-center self-center italic")


ui.run()
