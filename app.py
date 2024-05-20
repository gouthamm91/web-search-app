import googlesearch
from flask import Flask
app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def homePage():
	return '''
<!DOCTYPE html>
<html>
<head>
	<title></title>
</head>
<body style="font-family: sans-serif; background-color: rgba(200, 200, 200, 1)">
	<center>
	<a style="font-size: 200%; font-weight: bold; color: red;">VPN</a> <a style="font-size: 200%; font-weight: bold;">KILLER</a><br>
	<input id="inp" style="border-radius: 5px; border: 1px solid grey; font-size: 105%; padding: 3px; margin: 5px; width: 99%;" onchange="if (this.value.trim() != '') {window.open('/search/'+inp.value.replace(/ /g, '+'), target='_blank');}"/>

	<input type="button" style="border-radius: 5px; border: 1px solid grey; font-size: 200%;; padding: 3px; margin: 5px; width: 99.5%; height: 100px;" value="Search Now..." onclick="if (inp.value.trim() != '') {window.open('/search/'+inp.value.replace(/ /g, '+'), target='_blank');}">

	<!-- <input type="button" style="font-size: 200%; width: 175px; height: 100px; border-radius: 10px; border: 1px solid grey;" onclick="window.open('/search/'+inp.value.replace(/ /g, '+')+ '+' +this.value.toLowerCase().replace(/ /g, '+'), target='_blank');" value="PornHub"/>
	<input type="button" style="font-size: 200%; width: 175px; height: 100px; border-radius: 10px; border: 1px solid grey;" onclick="window.open('/search/'+inp.value.replace(/ /g, '+')+ '+' +this.value.toLowerCase().replace(/ /g, '+'), target='_blank');" value="XVideos"/>
	<input type="button" style="font-size: 200%; width: 175px; height: 100px; border-radius: 10px; border: 1px solid grey;" onclick="window.open('/search/'+inp.value.replace(/ /g, '+')+ '+' +this.value.toLowerCase().replace(/ /g, '+'), target='_blank');" value="XHamster"/>
	<input type="button" style="font-size: 200%; width: 175px; height: 100px; border-radius: 10px; border: 1px solid grey;" onclick="window.open('/search/'+inp.value.replace(/ /g, '+')+ '+' +this.value.toLowerCase().replace(/ /g, '+'), target='_blank');" value="BeeG"/>
	<input type="button" style="font-size: 200%; width: 175px; height: 100px; border-radius: 10px; border: 1px solid grey;" onclick="window.open('/search/'+inp.value.replace(/ /g, '+')+ '+' +this.value.toLowerCase().replace(/ /g, '+'), target='_blank');" value="You-Porn"/>
	<input type="button" style="font-size: 200%; width: 175px; height: 100px; border-radius: 10px; border: 1px solid grey;" onclick="window.open('/search/'+inp.value.replace(/ /g, '+')+ '+' +this.value.toLowerCase().replace(/ /g, '+'), target='_blank');" value="MilfFox"/>
	<input type="button" style="font-size: 200%; width: 175px; height: 100px; border-radius: 10px; border: 1px solid grey;" onclick="window.open('/search/'+inp.value.replace(/ /g, '+')+ '+' +this.value.toLowerCase().replace(/ /g, '+'), target='_blank');" value="Spankbang"/>
	<input type="button" style="font-size: 200%; width: 175px; height: 100px; border-radius: 10px; border: 1px solid grey;" onclick="window.location.href='/search/'+inp.value;" value=""/>
	<input type="button" style="font-size: 200%; width: 175px; height: 100px; border-radius: 10px; border: 1px solid grey;" onclick="window.location.href='/search/'+inp.value;" value=""/>
	<input type="button" style="font-size: 200%; width: 175px; height: 100px; border-radius: 10px; border: 1px solid grey;" onclick="window.location.href='/search/'+inp.value;" value=""/> -->
</body>
</html>
	'''

@app.route("/search/<q>")
def search(q):
	# for i in search(q, num_results=5):
	n = 0
	# for j in googlesearch.search(q, num=5):
	# for j in googlesearch.search(q, tld='com', country="US", num=5):
	for j in googlesearch.search(q, tld='co.in', num=5):
	# if True:
		n = n + 1
		url = j
		# if n <= 0:
		if True:
			if 'www.xvideos.com' in url:
				url = url.replace('https://www.xvideos.com', 'https://www.xvideos2.uk')
			else:
				url = url.replace('https://www.pornhub.com', 'https://de.pornhub.org').replace('https://www.pornhub.org', 'https://de.pornhub.org')
				url = url.replace('https://www.xnxx.com', 'https://xnxx115.health').replace('https://xnxx.com', 'https://xnxx115.health')
				url = url.replace('https://www.beeg.com', 'https://beeg.onl').replace('https://beeg.com', 'https://beeg.onl')
				url = url.replace('https://www.spankbang.com', 'https://spankbang.party').replace('https://spankbang.com', 'https://spankbang.party')
				url = url.replace('https://www.youporn.com', 'https://you-porn.com').replace('https://www.you-porn.com', 'https://you-porn.com')
				url = url.replace('https://www.xhamster.com', 'https://xhamster.desi').replace('https://xhamster.com', 'https://xhamster.desi')
				url = url.replace('https://www.', 'https://')
			break
		else:
			break
	# return "<a href=\"https://voidstars.vercel.app?url="+url+"\"><h1>Searching For => "+q+"</h1></a>"
	return '''
	<body onload="window.location.href = \''''+url+'''\';">
	</body>
	'''

