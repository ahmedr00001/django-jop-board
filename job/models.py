from django.db import models
from django.utils.text import slugify



JOB_TYPE_CHOICES = (
    ('Full Time', 'Full Time'),
    ('Full Time', 'Part Time'),
)


class Category (models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name


#function to customize upload folder
def image_uploader(instance, imageName):
    image_name, extension = imageName.rsplit(".", 1) 
    return "job/%s.%s" % (instance.id if instance.id else "temp", extension)


class Job(models.Model):
    title = models.CharField(max_length=100)
    jop_type= models.CharField(max_length=15 ,choices=JOB_TYPE_CHOICES)
    description = models.TextField(max_length=1000)
    published_at = models.DateTimeField(auto_now= True)
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    experience = models.IntegerField(default=1)
    category = models.ForeignKey(Category , on_delete=models.CASCADE)
    image = models.ImageField(upload_to=image_uploader)
    slug = models.SlugField(default="", null=True)


    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
    
    def __str__(self):
        return self.title



class Apply(models.Model):
    job = models.ForeignKey(Job , on_delete=models.CASCADE)
    name = models.CharField(max_length=25)
    email = models.EmailField()
    website = models.URLField()
    cv = models.FileField(upload_to='apply')
    cover_letter = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now= True)

    def __str__ (self):
        return self.name