import requests
import json

from resume import Resume
from filter import Filter

def takePrice(elem):
    return elem.get("price")

def getResume(filter):
    url = "https://api.mercadolibre.com/sites/MLA/search"

    name = filter.get("product_name")

    params = {"q": name}

    response = requests.get(url,params)
    response_json = response.json()

    selected_items = response_json.get("results")[0:1]

    selected_items.sort(key=takePrice)

    resume = Resume()

    for item in selected_items:
        resume.message += "Titulo: " + item.get("title")
        resume.message += "\nPrecio: " + str(item.get("price"))
        resume.message += "\nLink: " + item.get("permalink") + "\n\n"

    return resume
