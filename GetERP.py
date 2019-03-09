import 	re
import 	requests
from   	config    import  *
import 	os
'''
爬取公司的ERP系统将产品库存情况存入Excel
'''
def PageGet(url,data,headers):
	'''
	获取单独的每一页
	'''
	try:
		Res = requests.get(url,params =data,headers = headers)
		html = Res.content.decode('utf-8','ignore')
		return html
	except requests.exceptions.ConnectTimeout:
		print('ConnectTimeout Net Error!')
	except requests.exceptions.HTTPError:
		print('HTTPRequests status Error!')
	except requests.exceptions.Timeout:
		print('Timeout Url Error!')
	except requests.exceptions:
		print("获取第页失败！！" )
		return  None

def ProductPageGet(html):
	p1 = r'<div id="J_topPage".*?</em><i>(.*?)</i>'
	pattern2 = re.compile(p1, re.S)
	# 在源文本中搜索符合正则表达式的部分
	Data_Lable = re.findall(pattern2, html)
	return int(Data_Lable[0])

def CommentPageGet(url,data):
	'''
	获取单独的每一页
	'''
	try:
		Res = requests.get(url,params =data)
		html = Res.content.decode('GB2312','ignore')
		return html
	except requests.exceptions.ConnectTimeout:
		print('ConnectTimeout Net Error!')
	except requests.exceptions.HTTPError:
		print('HTTPRequests status Error!')
	except requests.exceptions.Timeout:
		print('Timeout Url Error!')
	except requests.exceptions:
		print("获取第页失败！！" )
		return  None
def PageAnalysisProcessing(html):
	'''
	正则表达式处理返回的页面信息
	'''
	result =[]
	p1 = r'<div.*?<a target="_blank" title="(.*?)" href="//item.jd.com/(.*?)\.html".*?</div>'
	pattern2 = re.compile(p1,re.S)
	#在源文本中搜索符合正则表达式的部分
	Data_Lable = re.findall(pattern2,html)
	#result  = Data_Lable
	#去重
	for sub in Data_Lable:
		if sub not in result:
			result.append(sub)
	return result
def GetMaxPageNum(html):
	p1 = r'"maxPage":(.*?),"testId"'
	pattern2 = re.compile(p1, re.S)
	# 在源文本中搜索符合正则表达式的部分
	result = re.findall(pattern2, html)
	return int(result[0])

def CommentPageAnalysisProcessing(html):
	'''
	正则表达式处理返回的页面信息
	'''
	result=[]
	p1 = r'"content":"(.*?)","creationTime":"(.*?)","isTop'
	pattern2 = re.compile(p1,re.S)
	#在源文本中搜索符合正则表达式的部分
	Data_Lable = re.findall(pattern2,html)
	for sub in Data_Lable:
		if sub not in result:
			result.append(sub)
	#print(result)
	return result
def FileIsExecute(file):
	'''
	判断一个文件存在与否
	'''
	try:
		f=open(file)
		f.close()
	except FileNotFoundError:
		return False
	return True

def WriteUserLog(L_num,logmsg):
		if FileIsExecute('commen.txt') is not True:
			fileUserLog = open('commen.txt','w+',encoding='GB2312')
		else:
			fileUserLog = open('commen.txt', 'a',encoding='GB2312')
		fileUserLog.write('第 %5d 条 评论信息：'% L_num)
		fileUserLog.write(logmsg[0] +' %s 产生。' % logmsg[1] +'\n')
		fileUserLog.close()

def main():
	HTML=PageGet(url,Search_data,Headers_Of_GET)
	ProductPageNum= ProductPageGet(HTML)
	x = 1
	for n in range(1,ProductPageNum*2,2):
		Search_data['page'] = n
		Search_data['s'] = (n-1)*30+1
		HTML = PageGet(url, Search_data, Headers_Of_GET)
		ProductInformation = PageAnalysisProcessing(HTML)
		for Num in ProductInformation:
			Comment_data['productId']=Num[1]
			MAXPageNum = GetMaxPageNum(CommentPageGet(CommentUrl,Comment_data))
			WriteUserLog(0, ['','\n\n*********>>>>>以下评论对应的商品为： https://item.jd.com/'+ Num[1]+ '.html <<<<<*********'])
			for n in range(0,MAXPageNum):
				Comment_data['page'] = n
				HTML = CommentPageGet(CommentUrl,Comment_data)
				CommmDitile=CommentPageAnalysisProcessing(HTML)
				for sub in CommmDitile:
					WriteUserLog(x,sub)
					x+=1
					#print(x,sub)
	print('处理完成！')

























if __name__ == '__main__':
	main()