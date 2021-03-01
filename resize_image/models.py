from django.db import models

class Product(models.Model):
    image = models.ImageField('Gambar', null=True, blank=True)
    name = models.CharField('Nama Produk', max_length=30)

    def save(self):
        import sys
        from PIL import Image
        from io import BytesIO
        from django.core.files import File

        im = Image.open(self.image)
        basewidth = 200
        wpercent = basewidth/float(im.size[0])
        hsize = im.size[1]*wpercent
        size_f = (basewidth, int(hsize))
        im = im.resize(size_f, Image.NEAREST)

        output = BytesIO()
        im.save(fp=output, format='JPEG', quality=90)
        self.image = File(output, name=self.image.name)

        super(Product, self).save()
