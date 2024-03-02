# def main():
#   fake: Faker = Faker()

#   for i in range(1):
#     task = Blog.objects.create(
#       name=fake.paragraph(nb_sentences=1),
#       description=fake.paragraph(nb_sentences=1),
#       image=fake.image_url,
#     )
#     print(f"Created blog. Title: {task.name}")

#   blog_count = Blog.objects.count()

#   print(f"There are {blog_count} blogs in the database")
 
 
# if __name__ == "__main__":
#   import os

#   from django.core.wsgi import get_wsgi_application

#   os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
#   application = get_wsgi_application()

#   import random

#   from faker import Faker
#   from blogs_api.models import Blog

# main()



if __name__ == "__main__":
  import os

  from django.core.wsgi import get_wsgi_application

  os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
  application = get_wsgi_application()



from faker import Faker
from blogs_api.models import Blog

fake = Faker()
Faker.seed(2)

for i in range(3):
  name = fake.paragraph(nb_sentences=1)
  description = fake.paragraph(nb_sentences=2)
  # image = fake.image_url(width=250, height=250)
  new_blog = Blog(name=name, description=description)
  new_blog.save()
