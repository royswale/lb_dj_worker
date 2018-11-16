# scrape lb-dj.com worker data using scrapy

## scrapy

https://docs.scrapy.org/en/latest/intro/tutorial.html#creating-a-project

```bash
pip3 install scrapy
scrapy startproject lb_dj_worker
cd lb_dj_worker
scrapy genspider lbdjworker lb-dj.com
```