# B站番剧数据分析

 对B站番剧播放数据和tags进行APriori频繁项集挖掘

## 1.数据收集

使用python中的scrapy包构建爬虫 ，爬取了目前B站上所有番剧的：

- 番剧名
- 标签
- 播放量
- 追番数量
- 弹幕数量

收集的数据放在`/数据爬取/anime_data/data.csv`中

> 爬虫使用说明：
>
> 1. scrapy 安装 `pip install scrapy`(linux:`pip3 install scrapy`)
> 2. 命令行`cd`到`/数据挖掘/anime_data`目录下
> 3. 执行命令：`scrapy crawl anime_data -o data.csv`
