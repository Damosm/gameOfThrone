import pandas as pd
import json
import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode
import unicodedata
import os




########################################################################################################
#chargement des fichiers
########################################################################################################""

with open(r'C:\Users\utilisateur\Documents\Python\GameofThrone\game-of-thrones-srt\season1.json','r',encoding='utf-8') as f:
 data1 = json.load(f)

with open(r'C:\Users\utilisateur\Documents\Python\GameofThrone\game-of-thrones-srt\season2.json','r',encoding='utf-8') as f:
 data2 = json.load(f)

with open(r'C:\Users\utilisateur\Documents\Python\GameofThrone\game-of-thrones-srt\season3.json','r',encoding='utf-8') as f:
 data3 = json.load(f)

with open(r'C:\Users\utilisateur\Documents\Python\GameofThrone\game-of-thrones-srt\season4.json','r',encoding='utf-8') as f:
 data4 = json.load(f)

with open(r'C:\Users\utilisateur\Documents\Python\GameofThrone\game-of-thrones-srt\season5.json','r',encoding='utf-8') as f:
 data5 = json.load(f)

with open(r'C:\Users\utilisateur\Documents\Python\GameofThrone\game-of-thrones-srt\season6.json','r',encoding='utf-8') as f:
 data6 = json.load(f)
 
with open(r'C:\Users\utilisateur\Documents\Python\GameofThrone\game-of-thrones-srt\season7.json','r',encoding='utf-8') as f:
 data7 = json.load(f)
#############################################################################################  
liste_data = (data1,data2,data3,data4,data5,data6,data7)


##############################################################################################
#create table
##############################################################################################
# try :
  
#   cnx = mysql.connector.connect(user='root', password='damos02',
#                             host='127.0.0.1',
#                             database='dataia_nancy')
#   if (cnx.is_connected()):
#     print('is connected')

#   cursor = cnx.cursor()

#   cursor.execute('CREATE TABLE `dataia_nancy`.`gameofthrone` (`id` INT NOT NULL AUTO_INCREMENT,`saison` VARCHAR(100) NULL,`episode` VARCHAR(100) NULL,`titre` VARCHAR(100) NULL,`second` VARCHAR(100) NULL,`text` VARCHAR(200) NULL, PRIMARY KEY (`id`));')
  
#   cnx.commit()
    
#   cursor.close()  
#   cnx.close()
  
# except mysql.connector.Error as error:
#     print("Failed to create table {}".format(error))

# finally:
#     if (cnx.is_connected()):
#         cnx.close()
#         print("MySQL connection is closed")




################################################################################################
#insert
################################################################################################

# try :
  
#   cnx = mysql.connector.connect(user='root', password='damos02',
#                              host='127.0.0.1',
#                              database='dataia_nancy')
#   if (cnx.is_connected()):
#     print('is connected')
    
#   cursor = cnx.cursor()
  
#   for data in liste_data :
    
#     for a , b in data.items() :
#       print("\n")
#       print(a, "\n")
    
#       for second,text in data[("{}").format(a)].items() :
        
#         saison = a[17:19]
#         episode = a[20:22]
#         titre = a[23:-4]
#         text = unicodedata.normalize('NFKD', text).encode('ascii', 'replace') #Nettoyage
#         requete = ('insert into gameofthrone (saison,episode,titre,second,text) values (%s,%s,%s,%s,%s);')        
#         values = (saison,episode,titre,second,text)
#         print(requete,values)
#         cursor.execute(requete,values)

  
  
#   cnx.commit()
#   cursor.close()
  
  
#   cnx.close()

# except mysql.connector.Error as error:
#     print("Failed to insert record into gameofthrone table {}".format(error))

# finally:
#     if (cnx.is_connected()):
#         cnx.close()
#         print("MySQL connection is closed")

##################################################################################################
#select
###################################################################################################
try :
  
  cnx = mysql.connector.connect(user='root', password='damos02',
                            host='127.0.0.1',
                            database='dataia_nancy')
  if (cnx.is_connected()):
    print('is connected')

  cursor = cnx.cursor()

  cursor.execute('select * from gameofthrone limit 10;')

  
  row = cursor.fetchall()
  result = pd.DataFrame(row)

  print(result)
  
  cursor.close()  
  cnx.close()
  
except mysql.connector.Error as error:
    print("Failed to select record into gameofthrone table {}".format(error))

finally:
    if (cnx.is_connected()):
        cnx.close()
        print("MySQL connection is closed")