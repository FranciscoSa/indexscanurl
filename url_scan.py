import urllib.request
import sys
import socket

lista = []
url_list = []

url ='http://' + input ('Entre com a url (EX : www.google.com ): ')

if url != '' :
	print ('\n <===========================> Baixando index.html <==========================>\n')
	urllib.request.urlretrieve(url,'index.html')
	print (' Download Concluido...\n')
else:
	print ('URL INVALIDA')
	sys.exit()

index = open ('index.html','r')
print ('\n <=====================> Processando Arquivo index.html <=====================>\n')
for line in index:
	if 'href="htt' in line :
		if '.com.br' in line:
			inicio = line.find('htt')
			fim = line.find('.com.br')
			temp = line[inicio:fim+7]
			if len(temp) < 50 and temp != '' :
				lista.append(temp)
			print ('URL encontrada : ',temp)
		else :
			inicio = line.find('htt')
			fim = line.find('.com')
			temp = line[inicio:fim+4]
			if len(temp) < 50 and temp != '' :
				lista.append(temp)
			print ('URL encontrada : ',temp )

print ('\n <=====================> Eliminando Urls Duplicadas <=====================>\n')
for i  in lista :
	if i not in url_list :
		url_list.append(i)
url_list.sort()
print ('Remoção de url duplicadas concluida' )

print ('\n <==========================> Resolvendo Hosts <==========================>\n')

#for i in url_list :
	#if 'https:' in i :
		#url = i [9:]
	#host = socket.gethostbyname(i)
	#print (url)
	#if 'https://' in i :
		

#print (url_list)

index.close()
