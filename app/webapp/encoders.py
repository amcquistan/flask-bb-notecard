
from medea import medea, MedeaEncoder
from datetime import date, datetime

medea.register(datetime, lambda obj: obj.strftime('%Y-%m-%d %H:%M'))
medea.register(date, lambda obj: obj.strftime('%Y-%m-%d'))
JSONEncoder = MedeaEncoder
