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
	<input id="inp" style="border-radius: 5px; border: 1px solid grey; font-size: 105%; padding: 3px; margin: 5px; width: 99%;">

	<input type="button" style="border-radius: 5px; border: 1px solid grey; font-size: 200%;; padding: 3px; margin: 5px; width: 99.5%; height: 100px;" value="Search Now..." onclick="window.open('/search/'+inp.value, target='_blank');">

	<input type="button" style="font-size: 200%; width: 175px; height: 100px; border-radius: 10px; border: 1px solid grey;" onclick="window.open('/search/'+inp.value+' '+this.value.toLowerCase(), target='_blank');" value="PornHub"/>
	<input type="button" style="font-size: 200%; width: 175px; height: 100px; border-radius: 10px; border: 1px solid grey;" onclick="window.open('/search/'+inp.value+' '+this.value.toLowerCase(), target='_blank');" value="XVideos"/>
	<input type="button" style="font-size: 200%; width: 175px; height: 100px; border-radius: 10px; border: 1px solid grey;" onclick="window.open('/search/'+inp.value+' '+this.value.toLowerCase(), target='_blank');" value="XHamster"/>
	<input type="button" style="font-size: 200%; width: 175px; height: 100px; border-radius: 10px; border: 1px solid grey;" onclick="window.open('/search/'+inp.value+' '+this.value.toLowerCase(), target='_blank');" value="BeeG"/>
	<input type="button" style="font-size: 200%; width: 175px; height: 100px; border-radius: 10px; border: 1px solid grey;" onclick="window.open('/search/'+inp.value+' '+this.value.toLowerCase(), target='_blank');" value="You-Porn"/>
	<input type="button" style="font-size: 200%; width: 175px; height: 100px; border-radius: 10px; border: 1px solid grey;" onclick="window.open('/search/'+inp.value+' '+this.value.toLowerCase(), target='_blank');" value="MilfFox"/>
	<input type="button" style="font-size: 200%; width: 175px; height: 100px; border-radius: 10px; border: 1px solid grey;" onclick="window.open('/search/'+inp.value+' '+this.value.toLowerCase(), target='_blank');" value="Spankbang"/>
	<!-- <input type="button" style="font-size: 200%; width: 175px; height: 100px; border-radius: 10px; border: 1px solid grey;" onclick="window.location.href='/search/'+inp.value;" value=""/>
	<input type="button" style="font-size: 200%; width: 175px; height: 100px; border-radius: 10px; border: 1px solid grey;" onclick="window.location.href='/search/'+inp.value;" value=""/>
	<input type="button" style="font-size: 200%; width: 175px; height: 100px; border-radius: 10px; border: 1px solid grey;" onclick="window.location.href='/search/'+inp.value;" value=""/> -->
</body>
</html>
	'''

@app.route("/search/<q>")
def search(q):
	# for i in search(q, num_results=5):
	for j in googlesearch.search(q, num=5):
	# if True:
		url = j
		break
	# return "<a href=\"https://voidstars.vercel.app?url="+url+"\"><h1>Searching For => "+q+"</h1></a>"
	return '''
	<body onload="window.location.href = \'https://voidstars.vercel.app?url='''+url+'''\';">
	</body>
	'''

