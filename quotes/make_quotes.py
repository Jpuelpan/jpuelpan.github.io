import json

from string import Template

template = Template("""
<blockquote>
  <p>$body</p>
  <span class="author">$author, $originName</span>
</blockquote>""")

with open('quotes.json') as f:
    quotes = json.load(f)

    for quote in quotes:
        element = template.substitute(
            body=quote['body'],
            author=quote['author'],
            originName=quote['originName']
        )

        print(element)

