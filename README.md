# gemget-python
I wanted an easy function to return gemini text from a gemini url in python similar to [gemget](https://github.com/makew0rld/gemget) except I want to import it from python and I dont care for cli usage(currently). I forked code from [solder punks repo](https://tildegit.org/solderpunk/gemini-demo-1) and deleted a bunch of lines, un-deprecated some crusty old code. Also I dont understand half of these librarys, it "just werks".

things lost because Im lazy:
*  automatically detect encoding currently always assumes UTF-8  (cgi was deprecated and I didn't want to learn the new method)

things I want to add:
- proper TLS (Does NOT DO ANY validation of TLS certificates currently)
- encoding detection

##usage
```python
from gemget_python import gemget

gemini_text = gemget("URL")
```

