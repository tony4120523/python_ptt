#!/bin/bash
rm -f a.json
scrapy crawl ptt -o a.json
python3.6 a.py
