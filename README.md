
# PDF2Wav

Note: This Project is a work in progress. Help is appreciated! Look at the contributing section to look at some features that could be worked on!


A simple Flask based REST API for converting text contained in PDF's to freeform speech using a TTS API, with some extra emphasis on using design patterns, and decoupling business logic whenever possible. 








## Badges

[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg)](https://opensource.org/licenses/)


## Authors

- [@adiraokhoury](https://www.github.com/adiraokhoury)


## Contributing

Contributions are always welcome!
Features Requests are tracked in [this](https://github.com/users/adiraokhoury/projects/1) github project board. 



## Blog Post


The internals of why and how I built this is detailed in my [blog post](https://adiraokhoury.github.io/blogPost1.html) on my [website](https://adiraokhoury.github.io). 
## Lessons Learned



Flask is NOT a reliable web server. Nginx and Gunicorn make flask capable of handling high traffic. 

Dependency Inversion and Injection in Python is very easy to violate due to a lack of type checking. Using a plugin like [mypy](https://mypy.readthedocs.io/en/stable/index.html) can help mitigate this. 

There aren't a lot of experiments done on Reading and Writing wav files from/to different cache implementations. From this perspective, I do think that repurposing this project as a tool for analyzing bulk R/W performance of multimedia on different storage implementations(S3, NFS, Redis, etc) might be a future avenue for improvement. 

##Setup and Installation

Install the requirements:

'''
pip3 install requirements.txt
'''
