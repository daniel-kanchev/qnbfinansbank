BOT_NAME = 'qnbfinansbank'
SPIDER_MODULES = ['qnbfinansbank.spiders']
NEWSPIDER_MODULE = 'qnbfinansbank.spiders'
ROBOTSTXT_OBEY = True
LOG_LEVEL = 'WARNING'
ITEM_PIPELINES = {
   'qnbfinansbank.pipelines.DatabasePipeline': 300,
}
