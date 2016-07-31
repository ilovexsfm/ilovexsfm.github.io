from xml.etree.ElementTree import parse
import urllib


fd = open("data.json","w")
fcsv = open("data.csv","w")


tree = parse("idwk.xml")
note = tree.getroot()

tree_ddanzi = parse("idwk_ddanzi.xml")
note_ddanzi = tree_ddanzi.getroot()




data = note.findall("channel")[0]
data_length = len(data)

data_ddanzi = note_ddanzi.findall("channel")[0]
data_ddanzi_length = len(data_ddanzi)







fd.write("var data = ")
fd.write("[")

fcsv.write("date|title|summary|url\n")


item = data_ddanzi[12 : ]
for i in item:
	if i[2].text != None:
		fd.write("{")

		temp = i[6].text.replace("\n"," /// ")
		fcsv.write(temp)
		fcsv.write("|")

		temp = i[6].text.replace("\"","\\\"")
		temp = temp.replace("\n","\\n")
		fd.write("\"Date\": \"")
		fd.write(temp)
		fd.write("\",")


		temp = i[0].text.replace("\n"," /// ")
		fcsv.write(temp)
		fcsv.write("|")

		temp = i[0].text.replace("\n","\\n")
		temp = temp.replace("\"","\\\"");
		fd.write("\"title\": \"")
		fd.write(temp) 
		fd.write("\",")



		temp = i[3].text.replace("\n","  /// ")
		fcsv.write(temp)
		fcsv.write("|")

		temp = i[3].text.replace("\n","\\n")
		temp = temp.replace("\"","\\\"");
		fd.write("\"summary\": \"")
		fd.write(temp) 
		fd.write("\",")



		temp = i[5].text.replace("\n"," /// ")

		fcsv.write(temp)
		fcsv.write("\n")

		temp = i[5].text.replace("\n","\\n")
		temp = temp.replace("\"","\\\"")
		fd.write("\"url\": \"")
		fd.write(temp)
		fd.write("\"")

		fd.write("},")

		fd.write("\n")

item = data[12 : ]
for i in item:
	if i[2].text != None:
		fd.write("{")

		temp = i[6].text.replace("\n"," /// ")
		fcsv.write(temp)
		fcsv.write("|")

		temp = i[6].text.replace("\"","\\\"")
		temp = temp.replace("\n","\\n")
		fd.write("\"Date\": \"")
		fd.write(temp)
		fd.write("\",")


		temp = i[0].text.replace("\n"," /// ")
		fcsv.write(temp)
		fcsv.write("|")

		temp = i[0].text.replace("\n","\\n")
		temp = temp.replace("\"","\\\"");
		fd.write("\"title\": \"")
		fd.write(temp) 
		fd.write("\",")



		temp = i[3].text.replace("\n","  /// ")
		fcsv.write(temp)
		fcsv.write("|")

		temp = i[3].text.replace("\n","\\n")
		temp = temp.replace("\"","\\\"");
		fd.write("\"summary\": \"")
		fd.write(temp) 
		fd.write("\",")



		temp = i[5].text.replace("\n"," /// ")

		fcsv.write(temp)
		fcsv.write("\n")

		temp = i[5].text.replace("\n","\\n")
		temp = temp.replace("\"","\\\"")
		fd.write("\"url\": \"")
		fd.write(temp)
		fd.write("\"")

		fd.write("},")

		fd.write("\n")


fd.write("]")
fd.close()
