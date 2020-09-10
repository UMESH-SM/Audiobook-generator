import pyttsx3 ,PyPDF2

engine = pyttsx3.init()
 
engine.setProperty('rate', 110)         # rate of speech pace

voices = engine.getProperty('voices')               
engine.setProperty('voice', voices[1].id)           # female voice

try:
    book = open('filename.pdf',mode='rb')           # input pdf name
    pdfReader = PyPDF2.PdfFileReader(book)
    
except:
    print('Upload a Valid pdf file.')
    exit()

num = pdfReader.getNumPages()
content = ''

for n in range(num):
    page = pdfReader.getPage(n)
    text = page.extractText()
    content = content + text

engine.say(content)                                     # Read out the pdf loud
engine.save_to_file(content, 'audiobook.mp3')           # save as a mp3 file 
engine.runAndWait()


