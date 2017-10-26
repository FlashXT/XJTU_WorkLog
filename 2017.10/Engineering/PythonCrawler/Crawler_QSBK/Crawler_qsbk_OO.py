# coding=utf-8
# 2017.10.25,Flash,糗事百科爬虫类
import urllib
import urllib2
import re
# 糗事百科爬虫类
class QSBK():
    def __init__(self):
        """初始化方法，定义一些变量"""
        self.pageIndex = 1
        self.user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:51.0) Gecko/20100101 Firefox/51.0"
        self.re = r'<div class="article.*?<h2>(.*?)</h2>.*?<span>(.*?)</span>.*?</a>(.*?)<div class="stats">.*?<span class="stats-vote"><i class="number">(.*?)</i>.*?<a.*?<i class="number">(.*?)</i>';
        # 初始化headers
        self.headers = {"User-Agent": self.user_agent}
        # 存放段子的变量,每个元素是每一页的段子
        self.stories = []
        # 存放程序是否继续运行的变量
        self.enable = False

    def getPage(self, pageindex):
        """传入某一页的索引获得页面代码"""
        try:
            url = "https://www.qiushibaike.com/hot/page/" + str(pageindex)
            # 构建请求的request
            request = urllib2.Request(url, headers=self.headers)
            # 利用urlopen获取页面代码
            response = urllib2.urlopen(request)
            # 将页面转化为utf-8编码
            pageCode = response.read().decode('utf-8')
            return pageCode

        except urllib2.URLError, e:
            if hasattr(e, "reason"):
                print unicode("连接糗百失败，错误原因："),e.reason
                return None
    def getPageItems(self,pageIndex):
        """传入某一页代码，返回本页段子列表"""
        pageCode = self.getPage(pageIndex)
        if not pageCode:
            print unicode("页面加载失败...")
            return None
        pattern = re.compile(self.re, re.S)
        items = re.findall(pattern, pageCode)
        # 用来存储每页的段子
        pageStories = []
        # 遍历正则表达式匹配的信息
        for item in items:
			haveImg = re.search("img",item[2])
			if  haveImg:	
				pattern2 = re.compile(r'src="(.*?)"',re.S)
				items2 = re.findall(pattern2,item[2])
				for it in items2:
					pageStories.append([item[0].strip(), item[1].strip(), it.strip(), item[3].strip(), item[4].strip()])
			else:
				pageStories.append([item[0].strip(), item[1].strip(),"None", item[3].strip(), item[4].strip()])
        return pageStories


    def loadPage(self):
        """加载并提取页面内容，加入到列表中"""
        # 如果当前未看的页数小于两页，则加载另一页
        if self.enable == True:
            if len(self.stories) < 2:
                # 获取新一页
                pageStories = self.getPageItems(self.pageIndex)
                # 将该页的段子存放到全局list中
                if pageStories:
                    self.stories.append(pageStories)
                    # 获取完之后页面索引加以一，表示下次读取下一页
                    self.pageIndex += 1

    def getOneStory(self, pageStories, page):
        """调用该方法，每次回车打印出一个段子"""
        # 遍历一页段子
        for story in pageStories:
            # 等待用户输入
            input = raw_input()
            # 每当输入回车一次，判断一下是否要加载到新页面
            self.loadPage()
            # 如果输入Q，则程序结束
            if input == "Q":
                self.enable = False
                return
            print  "第"+str(page)+"页\t", "发布人:",story[0],"\n"
            print  "Img Add:\t",story[2],"\n"
            print  "点 赞 数:\t",story[3],"\t","评 论 数:\t",story[4],"\n"
            print  "发布内容:",unicode(story[1])


    def start(self):
        """开始方法"""
        print "正在读取糗事百科,按回车查看新段子，Q退出"
        # 使变量为True，程序可以正常运行
        self.enable = True
        # 先加载一页内容
        self.loadPage()
        # 局部变量，控制当前读到了第几页
        nowPage = 0
        while self.enable:
            if len(self.stories) > 0:
                # 从全局list中获取一页的段子
                pageStories = self.stories[0]
                # 当前读到的页数加一
                nowPage += 1
                # 将全局list中第一个元素删除，因为已经取出
                del self.stories[0]
                # 输出该页的段子
                self.getOneStory(pageStories, nowPage)

spider = QSBK()
spider.start()
