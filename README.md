# wanfang-spider
**环境：selenium库**

## 介绍：
本爬虫能根据不同关键词爬取万方平台论文基本信息
万方url.py能爬取万方文章对应的编号，它将存在同目录下的url.csv文件里，可作为请求参数访问对应文章页面
万方概要.py可以根据url.csv中编号爬取对应文章概要，并将他们保存在同目录下gy.csv里

## 注意事项
本爬虫中默认爬取会议论文，如需爬取其他类型论文请更换目标url和关键词