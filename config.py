#Configuration parameter


#Summary warehouse
url = 'https://search.jd.com/Search'
Search_data ={
			'keyword':'XXXXXXXXX',
			'enc':'utf-8',
			'qrst': 1,
			'rt':1 ,
			'stop':1,
			'vt':2,
			'wd':'XXXXXXXXXXXX',
			'page': 1,
			's':1,
			'click':0
}
CommentUrl = 'http://sclub.jd.com/comment/productPageComments.action'

Comment_data ={
			'callback':'fetchJSON_comment98vv229',
			'productId':0,
			'score': 0,
			'sortType':5 ,
			'page':0,
			'pageSize':10,
			'isShadowSku':0,
			'fold': 1}
Headers_Of_GET = {
'Host': 'search.jd.com',
'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:64.0) Gecko/20100101 Firefox/64.0',
'Accept': '*/*',
'Referer': 'https://www.jd.com/?cu=true&utm_source=c.duomai.com&utm_medium=tuiguang&utm_campaign=t_16282_77255798&utm_term=366e6707232442a5bdd1e29f591e1bfb',
'Cache-Control':'max-age=0',
'Connection': 'keep-alive',
'cookies':''
}