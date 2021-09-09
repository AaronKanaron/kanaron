import random as rd

r_word = []

def r(e):
    return rd.choice(e)

with open("D:/Files/Programering/python/Resurser/SvenskaOrdBank.txt", "r", encoding="utf-8") as file:
		r_word = [w.strip() for w in file.readlines()]
		print(len(r_word))
  
print(r(r_word))



motiv = ["se ljuset", "se meningen med livet", "se havet", "må bra", "må hemskt", "dö"]

verb_ob = ["spring", "hoppa", "dö", "älska", "runka", "sök hjälp"]
verb_b = ["lukta", "lyssna", "tro", "gå", "andas", "avlida", "runka", "spela", "skrika", "springa", "leva"]

# adj = ["stark", "smart", "framgångsrik", "rolig", "fritänkade"]

substantiv = [
    ("bok", "boken", "böcker", "böckerna", "en"),
	("stol", "stolen", "stolar", "stolarna", "en"),
	("bord", "bordet", "bord", "borden", "ett"),
	("katt", "katten", "katter", "katterna", "en"),
	("mörker", "mörkret", "mörkret", "mörkrarna", "ett"),
	("ljus", "ljuset", "ljusen", "ljusen", "ett"),
	("rykte", "rykten", "ryktet", "rykterna", "ett"),
	("fader", "fadern", "fadrar", "fadrarna", "en"),
 	("familjemedlem", "familjemedlemmen", "familjemedlemmar", "familjemedlemmarna", "en"),
	("liv", "livet", "liv", "liven", "ett"),
	("kuk", "kuken", "kukar", "kukarna", "en"),
	("röv", "röven", "rövar", "rövarna", "en"),
	("kaffe", "kaffet", "kaffe", "kaffen", "en"),
	("ensamhet", "ensamheten", "ensamhet", "ensamheten", "en"),
	("självplågeri", "självplågeriet", "självplågeri", "självplågeriet", "ett"),
	("anonymt knull", "det anonyma knullet", "anonymt knull", "det anonyma knullet", "ett"),
	("hora", "horan", "horor", "hororna", "en")
] 


adjektiv = [
    (
        ("livsbejakande", "livsbejakande"),
    	("fett het", "fett hett"), 
     	("cool","coolt"), 
      	("fantastisk", "fantastiskt"), 
       	("underbar", "underbart"), 
        ("älskvärd", "älskvärd"), ("härlig", "härligt"),
        ("stark", "starkt"),
        ("snygg", "snyggt"),
        ("fin", "fint")
    ),
	(
		("livsförnekande", "livsförnekande"), 
		("ohet", "ohett"), 
		("o-cool", "o-coolt"),
		("fruktansvärd", "fruktansvärt"),
		("gräslig", "gräsligt"), 
		("ohövlig","ohövligt"), 
		("hemsk","hemskt"),
		("grinig", "grinigt"),
		("ful", "fult"),
		("hopplös", "hopplöst")
    ),
	(
		"intelligens",
		"erotik",
		"dygd",
		"smisk"
	)
]

uncatorgized = [("universell acceptans bland jämnåriga")]

# adj_b = ["grinigt", "fult", "hopplöst", "livsbejakande", "fett hett", "coolt", "fantastiskt", "underbart"]
# adj_ob = ["grinig", "ful", "hopplös", "livsbejakande", "fett het", "cool", "fantastisk", "underbar"]

äga = ["din lilla kropp", "din lilla snopp", "ditt fula ansikte", "din feta kropp", "din feta snopp", "din runda mage"]

#OMMOMOMOOMMOMMKMMNMMN MMMMMMMMMMMMMMMMMMMMMKMMMMMMKMMMMMMMMMMMMMMMMMMMMMM;MmmmmMMM M;MM;MM M;;;;MM

start = [
    "Bli en mästare på att " + r(verb_b) + ", så kommer du att " + r(motiv), 
    
    "Förbered dig inte för att " + r(motiv) + ", " + r(verb_ob) + " bara.",
    
    "Före " + r(substantiv)[1] + ", kommer " + r(substantiv)[3],
    
    "En liten dos med " + r(substantiv)[0] + " är faktiskt " + r(adjektiv[0])[1],
    
    "Titta inte på " + r(äga) + ", utan " + r(verb_ob) + " istället",
    
	"Var inte " + r(adjektiv[1])[0] + ", det är " + r(adjektiv[1])[1],
 
    "Det finns ett samband mellan " + r(substantiv)[0] + " och " + r(substantiv)[2],
    
    r(substantiv)[1].capitalize() + " - Det är där för att " + r(verb_b) + " på dig",
    
    "Lev aldig upp till " + r(substantiv)[1],

    "Du behöver inte ha en semester för att bli " + r(adjektiv[0])[0],
    
    "Det finns ett tydligt samband mellan " + r(uncatorgized) + " och " + r(substantiv)[2],
    
    "Om du vill ha tillfredsställelse, be om " + r(substantiv)[1],
    
    "Ingen " + r(adjektiv[2]) + ", ingen " + r(adjektiv[2]),
    
    "Att vara " +  r(substantiv)[1] + " är " + r(adjektiv[0])[1],
    
    "Puberteten är som " + r(substantiv)[0],
    
    "Bete dig " + r(adjektiv[1])[1] + ". Bete dig " + r(adjektiv[0])[1],
    
    "Älska alltid " + r(substantiv)[2] + ". Hata alltid " + r(substantiv)[2],
    
   	r(r_word).capitalize() + " - Det är mitt favorit ord. Det är så " + r(adjektiv[0])[1]

]


print(
	
	r(start)
)