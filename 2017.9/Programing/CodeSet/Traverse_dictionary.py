#coding=utf-8
#2017.9.22,Flash,×Öµä±éÀú

users_0={
    'username':'efermi',
    'first':'enrico',
    'last':'fermi'
	}
for key,value in users_0.items():
	print ("\nKey: "+key)
	print ("\nValue:"+value)
print "=============================="
fav_languages= {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python'
    }

print "=============Keys in Dictionary============"

for name in fav_languages.keys():
	 print name.title()
print "===========Values in Dictionary============"

for value in fav_languages.values():
	 print value.title()
print "===========items in Dictionary=============="

for name,favorite in fav_languages.items():
	 print name.title()+"'s favorite language is "+favorite.title()+"."
print "================================================================"
print "fav_languages.keys()="+str(fav_languages.keys())
print "fav_languages.values()="+str(fav_languages.values())
print "fav_languages.items()="+str(fav_languages.items())

print "================================================================"
for name in sorted(fav_languages.keys()):
	print name.title()
print "=================="
for language in sorted(fav_languages.values()):
	print language.title()
print "=================="
for language in set(fav_languages.values()):
	print language.title()
print "=================="
for language in sorted(fav_languages.items()):
	print language
