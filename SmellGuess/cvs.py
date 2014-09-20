#<<<<<<< HEAD
def decode_base64(data):
    """Decode base64, padding being optional.

    :param data: Base64 data as an ASCII byte string
    :returns: The decoded byte string.

    """
    missing_padding = 4 - len(data) % 4
    if missing_padding:
        data += b'='* missing_padding
    return decodestring(data)

#=======
import codecs
from django.utils.encoding import smart_str, smart_unicode


def SQL_to_csv():
    listSmeller = Smeller.objects.all()
    listGuess = Guess.objects.all()

    sm = open ('Smeller.csv', 'w+')
    gu = open ('Guess.csv', 'w+')
    
    sm_header="id;sex;age;date_registration"
    gu_header="id;smeller;sample;intensity;humor;note;image;feeling;name"
    sm.write(sm_header)
    gu.write(gu_header)
    
    
    for s in listSmeller :
        tmp_sentence="\n"+ str(s.id)+ ";" + s.sex+ ";"+ str(s.age)+ ";"+ str(s.date_registration)
        #tmp_sentence="\n"+ str(s.id)+ ";"+ s.name+ ";"+ s.sex+ ";"+ str(s.age)+ ";"+ str(s.date_registration) #obsolete
        sm.write(str(tmp_sentence))
        #s.sample.id
    sm.close()
    
    for g in listGuess :
        tmp_sentence="\n"+ str(g.id) + ";"+ str(g.smeller.id)+ ";"+str(g.sample.id)+";"+str(g.intensity)+";"+str(g.humor.name)+";"+str(g.note.name)+";"+str(g.image.name)+ ";"+ str(g.feeling)+ ";"#+ str(g.name)
        gu.write(str(tmp_sentence))
        #g.smeller.id
    gu.close()
   
SQL_to_csv()
#"id;name;sex;age:date_registration"
#"1;Flo;F;18;01/01/14"    
#"id;id_Smeller;id_Sample;intensity;humor;note;image;feeling;name"
#"1;1;1;20;COLERE;FRUITE;AIL;80;MA MERE"
