from django.shortcuts import render_to_response

import facebook

graph = facebook.GraphAPI("CAAHcx2lc0OsBAEPskLkUMuvTkysGZABVzlIhpC4NIgR4xYzi0KaXxngZCCgSqftZBDn0RfnqaU5bsziNElmlB9eyZCJbPh0eMTwj6MvfIjnxSNntim52XGFxkPcsQX3tkBDVFB12j0hVTJwyT8hCEpNTxaicSjbHKmbxUvYbdgghzwhGKZBwiW2o1sygKvf3lYb8gKwBfq8VLPf7CQdMDD4A5eGnxhIEZD")
#graph = facebook.GraphAPI("524224001003755|bxRt_m7CmROPKV10-9Tf1pAiZFQ")


def inicio(request):
	yo = graph.get_object("me")
	datos = graph.get_connections(yo['id'], "friends")
	amigos = datos['data']
	return render_to_response('index/index.html',{'yo':yo, 'amigos':amigos})


def compartir(request):
	dale = {'name':'QPasacix.Com',
			'link':'https://www.facebook.com/Qpasacixcom',
			'caption':'Las mejores fotos de los mejores tonos!',
			'description':'Esta es la mejor pagina social de la ciudad! Dale Like!',
			'picture': 'https://scontent-a.xx.fbcdn.net/hphotos-ash2/v/t1.0-9/p75x225/1463720_774971659237277_6714613847933765527_n.jpg?oh=9bd30b42f913bf5a8298c32d4a2b210b&oe=5512FD57'}
	m = "Dale like a esta pagina!"
	comp = graph.put_wall_post(m,dale)
	return render_to_response('index/post.html',{'comp':comp})