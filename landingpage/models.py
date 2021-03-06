from django.db import models
from PIL import Image

# Create your models here.


class PortfolioProject(models.Model):
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=300)
    link = models.URLField(max_length=200)
    project_image = models.ImageField(upload_to='Portfolio_projects')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Portfolio Project'
        verbose_name_plural = 'Portfolio Projects'

    def save(self, *args, **kwargs):
        super(PortfolioProject, self).save(*args, **kwargs)

        img = Image.open(self.project_image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.project_image.path)


class Testimonial(models.Model):
    name = models.CharField(max_length=250)
    testimonial = models.TextField()
    career = models.CharField(max_length=100)
    image = models.ImageField(upload_to='Testimonial_image')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Testimonial'
        verbose_name_plural = 'Testimonials'

    def save(self, *args, **kwargs):
        super(Testimonial, self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)


class ContactMe(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    subject = models.CharField(max_length=250)
    message = models.TextField()

    def __str__(self):
        return self.name
