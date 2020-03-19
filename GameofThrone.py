import pandas as pd
import json
import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode
import re


########################################################################################################
#chargement des fichiers
########################################################################################################""
with open(r'C:\Users\utilisateur\Documents\Python\GameofThrone\game-of-thrones-srt_Nettoyé\season1.json','r',encoding='utf-8') as f:
  data1 = json.load(f)

with open(r'C:\Users\utilisateur\Documents\Python\GameofThrone\game-of-thrones-srt_Nettoyé\season2.json','r',encoding='utf-8') as f:
  data2 = json.load(f)

with open(r'C:\Users\utilisateur\Documents\Python\GameofThrone\game-of-thrones-srt_Nettoyé\season3.json','r',encoding='utf-8') as f:
  data3 = json.load(f)

with open(r'C:\Users\utilisateur\Documents\Python\GameofThrone\game-of-thrones-srt_Nettoyé\season4.json','r',encoding='utf-8') as f:
  data4 = json.load(f)

with open(r'C:\Users\utilisateur\Documents\Python\GameofThrone\game-of-thrones-srt_Nettoyé\season5.json','r',encoding='utf-8') as f:
  data5 = json.load(f)

with open(r'C:\Users\utilisateur\Documents\Python\GameofThrone\game-of-thrones-srt_Nettoyé\season6.json','r',encoding='utf-8') as f:
  data6 = json.load(f)
  
with open(r'C:\Users\utilisateur\Documents\Python\GameofThrone\game-of-thrones-srt_Nettoyé\season7.json','r',encoding='utf-8') as f:
  data7 = json.load(f)

liste_data = (data1,data2,data3,data4,data5,data6,data7)

######################################################################""
#essaie de nettoyage(ne fonctionne pas)
#####################################################################
# for a , b in data.items() :
#     # print("\n")
#     # print(a, "\n")
  
#     for i,j in data[("{}").format(a)].items() :
#       j = re.sub('"','',j.rstrip())
#       # print(j)

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

#   cursor.execute('CREATE TABLE `dataia_nancy`.`gameofthrone` (`id` INT NOT NULL AUTO_INCREMENT,`second` VARCHAR(100) NULL,`text` VARCHAR(200) NULL,`saisonEpisode` VARCHAR(100) NULL,PRIMARY KEY (`id`));')
  
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
#                             host='127.0.0.1',
#                             database='dataia_nancy')
#   if (cnx.is_connected()):
#     print('is connected')
    
#   cursor = cnx.cursor()
  
#   for data in liste_data :
    
#     for a , b in data.items() :
#       print("\n")
#       print(a, "\n")
    
#       for i,j in data[("{}").format(a)].items() :
            
#         requete = ('insert into gameofthrone (second,text,saisonEpisode) values ("{}","{}","{}");').format(i, j, a)
#         print(requete)
#         cursor.execute(requete)

  
  
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