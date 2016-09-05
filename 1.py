def process(filePath,outPath=''):
	fp = open(filePath)
	fpa = open(outPath+'arousalData','w+')
	fpv = open(outPath+'valenceData','w+')

	i = 0
	outPutA = list()
	outPutV = list()
	for line in fp:
		paras = line.split(',')
		i += 1
		outLineA = str(i)+' '+paras[0]+' '+paras[1]+'\n'
		#line_id song_id arousal
		outLineV = str(i)+' '+paras[0]+' '+paras[3]+'\n'
		#line_id song_id valence
		outPutA.append(outLineA)
		outPutV.append(outLineV)

		if len(outPutA) > 100:
			for i in range(len(outPutA)):
				fpa.write(outPutA[i])
				fpv.write(outPutV[i])
			outPutV = []
			outPutA = []

	for i in range(len(outPutA)):
		fpa.write(outPutA[i])
		fpv.write(outPutV[i])

	fp.close()
	fpa.close()
	fpv.close()

if __name__ == "__main__":
	fromFile = raw_input("fromFile?")
	toPath = raw_input("toPath?")
	process(fromFile,toPath)
