from tag import Tag
from lista_reproduccion import ListaReproduccion
from usuario import Usuario
from video import Video

#usuario
usuario = Usuario("pepe", "perez", "pperez@gmail.com", "xx22")

#videos
videos = [
    Video("POO - La guia definitiva", usuario, Tag("dev")),
    Video("¿Como aprender programacion y no morir en el intento?", usuario, Tag("dev")),
    Video("Programacion en Python para videojuegos", usuario, Tag("dev"))
]

#agrego los tags a los videos
videos[0].add_tag(Tag("poo"))
videos[0].add_tag(Tag("programming"))
videos[0].add_tag(Tag("developer"))

videos[1].add_tag(Tag("noob"))
videos[1].add_tag(Tag("lern"))

videos[2].add_tag(Tag("videogames"))
videos[2].add_tag(Tag("python"))

#Genero 2 Listas de reproducción
listas = [
    ListaReproduccion("Videos Favoritos"),
    ListaReproduccion("TUP"),
    ListaReproduccion("Musica")
]

#Agrego videos a la lista de reproduccion
listas[0].add_video(videos[0])
listas[0].add_video(videos[1])

listas[1].add_video(videos[0])
listas[1].add_video(videos[2])
listas[1].add_video(videos[1])