from django.shortcuts import render_to_response
import facebook

graph = facebook.GraphAPI("524224001003755|bxRt_m7CmROPKV10-9Tf1pAiZFQ")


def obtienealbumes(request):
	albumes = graph.get_connections("425529830848130","albums")
	data = albumes["data"]
	return render_to_response('fotos/albumes.html',{'data':data})


def muestraalbum(request,ida):
	ids = str(ida)
	imagenes = []
	links = []
	datos = graph.get_connections(ids,"photos")
	fotos = datos["data"] #ingresa al array, dentro muchas opciones. "images" tiene source, q es el link de las fotos
	return render_to_response('fotos/album.html',{'ids':ids,'imagenes':fotos})