# -*- coding: utf-8 -*-
"""
This file contains all the extra code that we need to develop the sentimet analysis of the
tweets in spanish made about Medellin between 2019-2022
"""

replace_punctuation_dict = { '¿':'','?':'','!':'','¡':'','"':'','(':'',')':'','/':'','*':''}

replace_accent_dict ={'á':'a','é':'e','í':'i','ó':'o','ú':'u','ü':'u'}

stop_words = ['de','la','en','y','el','que','a','medellin','los','con','no','por','es','para','del','se',
              'un','las','una','lo','su','mas','esta','como','si','le','este','al','me','mi','pero','o',
              'sus','hay','son','nos','ya','te','tiene','hoy','todo','sin','tu','ha','q','fue','eso',
              'todos','muy','años','ser','porque','asi','cuando','solo','desde','hace','les','ni','yo',
              'hacer','estan','donde','dia','ese','entre','hasta','toda','esa','e','va','han','aqui','parte',
              'esto','tan','ahora','uno','bien','cada','quien','tienen','mucho','gran','tambien','estamos',
              'usted','puede','sera','dos','ver','nuestrs','siempre','estos','contra','nada','dias','era',
              'tener','debe','a','traves','sobre','sea','vez','cali','menos','muchos','sido','tenemos','san',
              'año','durante','ejemplo','medio','soy','buen','señor','cuenta','hola','aca','van','estas',
              'algo','mismo','da','nunca','todas','hecho','hizo','he','vamos','d','estoy','paso','cual','bogota',
              'nuestro','nuestra','antioquia','colombia','nuestros']

