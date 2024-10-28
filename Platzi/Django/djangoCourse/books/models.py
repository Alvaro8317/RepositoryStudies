from django.db import models


class Publisher(models.Model):
    name = models.TextField(max_length=100)
    address = models.TextField(max_length=100)

    def __str__(self):
        return f"Publisher {self.name}, {self.address}"


class Author(models.Model):
    name = models.TextField(max_length=200)
    birth_date = models.DateField(null=True)

    def __str__(self):
        return f"Author {self.name}, {self.birth_date}"


class Profile(models.Model):
    author = models.OneToOneField(Author, on_delete=models.CASCADE)
    website = models.URLField()
    biography = models.TextField(max_length=500, null=True)

    def __str__(self):
        return f"Profile {self.website}, {self.biography}"


class Book(models.Model):
    title = models.TextField(max_length=100)
    publication_date = models.DateField()
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    authors = models.ManyToManyField(Author, related_name="authors")

    def __str__(self):
        return f"Book {self.title} of {self.publisher}"
