import urllib, json
import datetime
import time
#import BitPyLoop
import Tkinter
import tkMessageBox
global loop 


def writeToFile(file, price):
	file.write( '"' +  str(now.strftime("%H:%m")) + '"' +":" + "\n")
	file.write(str(price))
	file.write("\n")

def repeatCheck(file):
	updatedPrice = getPrice()
	writeToFile(file, updatedPrice)
	time.sleep(10)
	repeatCheck(file)

def getPrice():
	url = "https://api.coinbase.com/v2/prices/spot?currency=USD"
	response = urllib.urlopen(url)
	data = json.loads(response.read())
	parsed_json = json.loads(json.dumps(data))
	currentPrice = float(parsed_json[u'data'][u'amount'])
	return currentPrice


now = datetime.datetime.now()

dataFileWriteJSON = open("Tree.json","a")
bitTreeString = "{"
bitTreeString = bitTreeString + '"' + str(now.strftime("%m-%d-%Y")) +'"' +":"+'\n'
dataFileWriteJSON.write(bitTreeString)

# Dislpay the GUI
top = Tkinter.Tk()

def displayPrice():
   tkMessageBox.showinfo( "BitCoin Price for " + str(now.strftime("%m/%d/%Y")), "$" + str(getPrice()))
def quit():
	global top
	top.destroy()
def quitLoop(win):
	win.destroy()
def startLoop():
	import BitPyLoop
	newWindow = Tkinter.Tk()
	newButton = Tkinter.Button(newWindow, text="End Loop and Program", command = lambda:quitLoop(newWindow))
	newButton.pack()
	newWindow.mainloop()
	dataFileWriteJSON = open("Tree.json","a")
	dataFileWriteJSON.write("}" + '\n')
	#while loop == True:
	#	dataFileWriteJSON = open("Tree.json","a")
	#	currentPrice = getPrice()
#		dataFileWriteJSON.write(str(currentPrice))




L1 = Tkinter.Button(top, text="Start ", command = startLoop)
B = Tkinter.Button(top, text ="Check BitCoin Price", command = displayPrice)
w = Tkinter.Button(top, text="End Program", command = quit)
top.configure(background='purple')

B.pack()
L1.pack()
w.pack()
top.mainloop()
#End GUI



