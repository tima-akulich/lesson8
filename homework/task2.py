import os
from PIL import Image


def get_images(path):
    for _path in os.listdir(path):
        new_path = path + '/' + _path
        if os.path.isdir(new_path):
            yield from get_images(new_path)
        if _path.endswith('.jpg'):
            yield new_path


class Thumbnailer:
    def __init__(self, path, width, height):
        self.path = path
        self.width = width
        self.height = height
        self.images = list(self._get_images())

    def _get_images(self):
        return get_images(self.path)

    def create_thumbnails(self):
        for image in self.images:
            _image = Image.open(image)
            _image.thumbnail((self.width, self.height))
            name = _image.filename.replace('.jpg', '-thumb.jpg')
            _image.save(name)
            yield name


if __name__ == '__main__':
    thumbnailer = Thumbnailer('images', 100, 50)
    thumbnailer.create_thumbnails()
