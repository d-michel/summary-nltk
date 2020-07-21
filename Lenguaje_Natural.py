from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
import nltk
from PdfToTxt import file_to_file

def summary(input_pdf):
    '''
    This function gives to you the summary of a text thanks to the nltk package
        (using a natural language proccessing algorithm).
    
    Input:
        input_pdf -> (str) address of the text file in .pdf format.
        
    Output:
        summary -> (str) content of the summary of the original text.
        summary.txt -> (.txt file) additionally, this script creates a .txt
            file whose content is said summary.
    '''
    # Converting input text from .pdf to .txt format using an own function: 
        # file_to_file(input_pdf) from PdfToTxt.py script
        
    input_txt = file_to_file(input_pdf)

    # Downloading nltk.stopwords and nltk.punkt methods from nltk package
    
    nltk.download("stopwords")
    nltk.download("punkt")
    
    # Setting up language of the input data (in our case, in spanish) with
        # which the nltk.stopwords.words method will work
    
    SW = set(stopwords.words("spanish"))
    
    # Extracting input text from the .txt file to the string text variable
    
    with open(input_txt, "r") as file:
        text = file.read().replace('\n', '')
        
        # Storing the text in a word_tokenize method to later give it a value
        
        words = word_tokenize(text)
        
        # Creating the freqTable dictionary to use it as a table of
            # frequencies of the words
        
        freqTable = dict()
    
    # Going over the text to store it in the table
    
    for word in words:
        word = word.lower() # Setting words in lower case and storing them in 
                                # word variable
        
        if word in SW:
            continue # If the word is in SW, the cycle continues
        
        if word in freqTable:  
            freqTable[word] += 1 # If the word is already in the table of
                                     # frequencies, it adds 1 to its position
        
        else: # If not, the word is included in the table with value equal to 1
            freqTable[word] = 1 
    
    # Creating sentences variable where the sentences to be valued from the
        # text will be stored
        
    sentences = sent_tokenize(text)
    
    # Creating a dictionary where those values will be stored
    
    sentenceValue = dict()
    
    # Going over the sentences of the text
    
    for sentence in sentences:
        
        for word, freq in freqTable.items(): # Going over the words of the
                                                 # frequencies table
            
            if word in sentence.lower(): # If the word is in the sentences
                                             # (in lower case),
                
                if sentence in sentenceValue: # And if the sentence is in the
                    sentenceValue[sentence] += freq # dictionary of sentences,        
                                                    # we add 1 to the freq.
                                                    # value of the sentence
                    
                else: # If not, the value of the sentence  in the dictionary is
                    sentenceValue[sentence] = freq # equal to 1
    
    # Adding all the values ​​in the sumValues variable and averaging them
    
    sumValues = 0
    
    for sentence in sentenceValue:
        sumValues += sentenceValue[sentence]
    
    average = int(sumValues/ len(sentenceValue))
    
    # Creating an string variable where the summary will be stored
    
    summary = ''

    # If the value of and sentence is bigger than 1.5 (changeable) times the 
        # average, it will be added to the summary of the text

    for sentence in sentences:
        if (sentence in sentenceValue) and (sentenceValue[sentence] > (1.5 * average)):
            summary += " " + sentence
    
    # Extracting the summary from the string to a .txt file saved in the folder
        # where is our script
    
    output_txt = open("summary.txt", "w+")
    output_txt.write(summary)
    output_txt.close()
        
    return(summary)