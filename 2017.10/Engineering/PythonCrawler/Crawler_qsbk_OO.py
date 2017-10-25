# coding=utf-8
# 2017.10.25,Flash,���°ٿ�������
import urllib
import urllib2
import re
# ���°ٿ�������
class QSBK():
    def __init__(self):
        """��ʼ������������һЩ����"""
        self.pageIndex = 1
        self.user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:51.0) Gecko/20100101 Firefox/51.0"
        self.re = r'<div class="article.*?<h2>(.*?)</h2>.*?<span>(.*?)</span>.*?</a>(.*?)<div class="stats">.*?<span class="stats-vote"><i class="number">(.*?)</i>.*?<a.*?<i class="number">(.*?)</i>';
        # ��ʼ��headers
        self.headers = {"User-Agent": self.user_agent}
        # ��Ŷ��ӵı���,ÿ��Ԫ����ÿһҳ�Ķ���
        self.stories = []
        # ��ų����Ƿ�������еı���
        self.enable = False

    def getPage(self, pageindex):
        """����ĳһҳ���������ҳ�����"""
        try:
            url = "https://www.qiushibaike.com/hot/page/" + str(pageindex)
            # ���������request
            request = urllib2.Request(url, headers=self.headers)
            # ����urlopen��ȡҳ�����
            response = urllib2.urlopen(request)
            # ��ҳ��ת��Ϊutf-8����
            pageCode = response.read().decode('utf-8')
            return pageCode

        except urllib2.URLError, e:
            if hasattr(e, "reason"):
                print unicode("�����ܰ�ʧ�ܣ�����ԭ��"),e.reason
                return None
    def getPageItems(self,pageIndex):
        """����ĳһҳ���룬���ر�ҳ�����б�"""
        pageCode = self.getPage(pageIndex)
        if not pageCode:
            print unicode("ҳ�����ʧ��...")
            return None
        pattern = re.compile(self.re, re.S)
        items = re.findall(pattern, pageCode)
        # �����洢ÿҳ�Ķ���
        pageStories = []
        # ����������ʽƥ�����Ϣ
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
        """���ز���ȡҳ�����ݣ����뵽�б���"""
        # �����ǰδ����ҳ��С����ҳ���������һҳ
        if self.enable == True:
            if len(self.stories) < 2:
                # ��ȡ��һҳ
                pageStories = self.getPageItems(self.pageIndex)
                # ����ҳ�Ķ��Ӵ�ŵ�ȫ��list��
                if pageStories:
                    self.stories.append(pageStories)
                    # ��ȡ��֮��ҳ����������һ����ʾ�´ζ�ȡ��һҳ
                    self.pageIndex += 1

    def getOneStory(self, pageStories, page):
        """���ø÷�����ÿ�λس���ӡ��һ������"""
        # ����һҳ����
        for story in pageStories:
            # �ȴ��û�����
            input = raw_input()
            # ÿ������س�һ�Σ��ж�һ���Ƿ�Ҫ���ص���ҳ��
            self.loadPage()
            # �������Q����������
            if input == "Q":
                self.enable = False
                return
            print  "��"+str(page)+"ҳ\t", "������:",story[0],"\n"
            print  "Img Add:\t",story[2],"\n"
            print  "�� �� ��:\t",story[3],"\t","�� �� ��:\t",story[4],"\n"
            print  "��������:",unicode(story[1])


    def start(self):
        """��ʼ����"""
        print "���ڶ�ȡ���°ٿ�,���س��鿴�¶��ӣ�Q�˳�"
        # ʹ����ΪTrue�����������������
        self.enable = True
        # �ȼ���һҳ����
        self.loadPage()
        # �ֲ����������Ƶ�ǰ�����˵ڼ�ҳ
        nowPage = 0
        while self.enable:
            if len(self.stories) > 0:
                # ��ȫ��list�л�ȡһҳ�Ķ���
                pageStories = self.stories[0]
                # ��ǰ������ҳ����һ
                nowPage += 1
                # ��ȫ��list�е�һ��Ԫ��ɾ������Ϊ�Ѿ�ȡ��
                del self.stories[0]
                # �����ҳ�Ķ���
                self.getOneStory(pageStories, nowPage)

spider = QSBK()
spider.start()
