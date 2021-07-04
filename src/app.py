import json
import sys
import random
from faker import Faker


def handler(event, context):
  try:
      # Import library to insert fake datas.
      fake = Faker()

      # Generate fake books data.
      payload = {
          "book": {
              "isbn": str(fake.isbn13()),
              "title": str(fake.sentence(nb_words=5)),
              "author": str(fake.name()),
              "stock": str(random.randint(0, 20)),
          }
      }

      return {"statusCode": 200, "body": {"body": json.dumps(payload)}}


  except:
    print("[ERROR] " + str(sys.exc_info()[1]))
    return {"statusCode": 500, "body": {"message": str(sys.exc_info()[1])}}
