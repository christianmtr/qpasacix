from django.shortcuts import render_to_response
import facebook

graph = facebook.GraphAPI("CAACEdEose0cBAKOLRwMNv4zj7QvJIkid0Q4IdhIPtOheZAgIWANyPlK7EIPojg0jdMBvSlJw6ZCZCebM1s96MxZCnynLwx2EG5ZBhlmcciX5eM36RmsnyV9fU7zLZBlZCSZBoZChquclgWNgSbIa0ceBuSfZAo70C9NUPIJ57f1OZCZCca8weahGnvyGgLksjxe2CvnCkNjsPxPlR6bJfCJsgjGlTa5zaDjPqqAZD")
#graph = facebook.GraphAPI("524224001003755|bxRt_m7CmROPKV10-9Tf1pAiZFQ")
#dale = {"name": "Q'Pasacix.Com", "link": "https://www.facebook.com/Qpasacixcom", "caption": "Las mejores fotos de los mejores tonos!", "description": "Esta es la mejor pagina social de la ciudad! Dale Like!", "picture": "https://scontent-a.xx.fbcdn.net/hphotos-ash2/v/t1.0-9/p75x225/1463720_774971659237277_6714613847933765527_n.jpg?oh=9bd30b42f913bf5a8298c32d4a2b210b&oe=5512FD57"}

def inicio(request):
	yo = graph.get_object("me")
	datos = graph.get_connections(yo['id'], "friends")
	amigos = datos['data']
	return render_to_response('index/index.html',{'yo':yo, 'amigos':amigos})

def compartir(self):
	yo = graph.get_object("me")
	m = "Dale like a esta pagina!"
    comp = graph.put_wall_post(message=m,attachment={"name": "Q'Pasacix.Com", "link": "https://www.facebook.com/Qpasacixcom", "caption": "Las mejores fotos de los mejores tonos!", "description": "Esta es la mejor pagina social de la ciudad! Dale Like!", "picture": "https://scontent-a.xx.fbcdn.net/hphotos-ash2/v/t1.0-9/p75x225/1463720_774971659237277_6714613847933765527_n.jpg?oh=9bd30b42f913bf5a8298c32d4a2b210b&oe=5512FD57"})
#    return render_to_response('index/post.html',{'comp':comp})
	return self.inicio()