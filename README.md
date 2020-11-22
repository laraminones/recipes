# recipes

This project is a search engine of cooking recipes, made for academic and testing purposes.

By using Elasticsearch, Scrapy, Django and Python we provide some search functionalities over a reduced collection of cooking recipes.

In order to do that and once the prerequisites are met, we crawl a cooking recipes site ([recipetineats.com](https://www.recipetineats.com/recipes/?fwp\_paged=)) using scrapy. Then we load the obtained data in Elasticsearch using a Python script. Finally, we provide the search and visualization functionalities through a web app made in Python. This app retrieves Elasticsearch's data by using query and aggregation methods the **elasticsearch_dsl** library provides.

*The following prerequisites and execution instructions have been considered for a Ubuntu 20.04 LTS system.*
### Prerequisites
* Install Python3.
```bash
$ sudo apt-get install python3
```
* Install pip.
```bash
$ sudo apt-get install python3-pip
```
* Install Scrapy ([guide here](https://docs.scrapy.org/en/latest/intro/install.html)).
```bash
$ sudo apt-get install python3 python3-dev python3-pip libxml2-dev libxslt1-dev zlib1g-dev libffi-dev libssl-dev
```
```bash
$ pip3 install Scrapy
```

* Install Elasticsearch
```bash
$ sudo apt-get install apt-transport-https
```
```bash
$ echo "deb https://artifacts.elastic.co/packages/7.x/apt stable main" | sudo tee /etc/apt/sources.list.d/elastic-7.x.list
```
```bash
$ sudo apt-get update && sudo apt-get install elasticsearch
```
* Install Django ([guide here](https://www.djangoproject.com/download/)) and elasticsearch_dsl library.

```bash
$ pip3 install Django==3.1.3
```
```bash
$ pip3 install elasticsearch-dsl
```

### Execution

* Execute Scrapy spider (this step is not really needed since we did upload the recipes.jsonlines file to the repo).
If you still want to re-run the crawling process go to recipes/ folder, delete de recipes.jsonlines and execute the following command.
```bash
$ scrapy crawl recipes -o recipes.jsonlines:jsonlines
```

* Launch Elasticsearch as service
```bash
$ sudo systemctl start elasticsearch.service
```

* Load crawled data into Elastic, using the index_loader.py Python script. This file is placed in recipes/
```bash
$ python3 index_loader.py
```
*Notice the recipes.jsonlines file needs to be in the same folder the Python script is.*

* Launch the Django app.
```bash
$ python3 manage.py runserver
```

### Test the app
Navigate to localhost:8000/ on your prefered browser too see the app main page.
