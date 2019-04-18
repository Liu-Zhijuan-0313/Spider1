from scrapy import cmdline

name = 'pythonPotion'
cmd = 'scrapy crawl {0}'.format(name)
cmdline.execute(cmd.split())
