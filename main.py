import sys
import os
import ntpath
import cv2
import csv
import codecs

from preprocessing.segment_sentence import segment_sentence
from preprocessing.segmentation import segment
from preprocessing.augment import augment

from CNN.recognize_character import recognize

from Unicode.seqgen import sequenceGen
from Unicode.printdoc import unicode_to_kn
from Unicode.printdoc import decode_word


def segmentation_call(image):
    rootdir = 'web_app/hwrkannada/hwrapp/static/hwrapp/images/Processed_' + \
        os.path.splitext(ntpath.basename(image))[0]
    if not os.path.exists(rootdir):
        os.makedirs(rootdir)

    dir = rootdir + '/Segmented_' + os.path.splitext(ntpath.basename(image))[0]
    # call the segmentation script on the image
    segment(image)
    return rootdir, dir


def augmentation_call(image, rootdir):
    augdir = rootdir + '/Augmented_' + \
        os.path.splitext(ntpath.basename(image))[0]
    # augment each of the segmented images
    augment(rootdir, augdir)
    return augdir


def prediction_call(augdir):
    # recognize all images in the directory
    predictions = recognize(os.path.join(os.getcwd(), augdir))
    # generate the Unicode sequence based on predictions
    sequence = sequenceGen(predictions)
    # generate Kannada text from the Unicode sequence
    kannada_text = unicode_to_kn(sequence)
    return(kannada_text)

#python progrma to read text files

def translation_call(augdir):
    kann = prediction_call(augdir)
    data = []
    file1= codecs.open('kannada-dict.txt','r','utf8')
    content=file1.read()
    words=content.split()
    for x in words:
        data.append(x)
    file1.close()
    file2 = codecs.open('kannada-text.txt','r','utf8')
    content = file2.read()
    words = content.split()
    if(words[0] == data[1]):
        return("Information(Ma-hi-ti)")
    elif(words[0] == data[2]):
        return("Me(na-nu)")
    elif(words[0] == data[3]):
        return("(Hu-ndhi-ve)")
    elif(words[0] == data[4]):
        return("UP (Me-Le)")
    elif(words[0] == data[5]):
        return("Them (aa-va-ru)")
    elif(words[0] == data[6]):
        return("Change (ba-dha-la-va-ne)")
    elif(words[0] == data[7]):
        return("Bale-ooru")
    elif(words[0] == data[8]):
        return("Together(jothe)")
    elif(words[0] == data[9]):
        return("Some(Ke-La-Vu)")
    elif(words[0] == data[10]):
        return("Possible/Doable")
    elif(words[0] == data[11]):
        return("by/through/via")
    elif(words[0] == data[12]):
        return("We/Us (na-vu)")
    elif(words[0] == data[13]):
        return("What? (yenu)")
    elif(words[0] == data[14]):
        return("Ka")
    elif(words[0] == data[15]):
        return("Great (Utham-ah)")
    elif(words[0] == data[16]):
        return("In excess (Thumba)")
    elif(words[0] == data[17]):
        return("Mother (Thayi)")
    elif(words[0] == data[18]):
        return("Power/Strength (Shakthi)")
    elif(words[0] == data[19]):
        return("Blue colour(Nee-lee)")
    elif(words[0] == data[20]):
        return("For/to  me(nana-ge)")
    elif(words[0] == data[21]):
        return("Ours (namma)")
    elif(words[0] == data[22]):
        return("For  us (namage)")
    elif(words[0] == data[23]):
        return("And (matthe)")
    elif(words[0] == data[24]):
        return("Here (illi)")
    elif(words[0] == data[25]):
        return("Of More/ In Excess")
    elif(words[0] == data[26]):
        return("Figure (Chitra)")
    elif(words[0] == data[27]):
        return("Wheel (Chakra)")
    else:
        return("Unknown")
    # return data
    









                                                   
    # f = open("test.txt","r")
    # my_dict = eval(f.read())
    # Dict_keys = my_dict.keys()                        
    # Dict_values = my_dict.values()
    # if my_dict.get(valu):
    #     return(my_dict.get(valu))
    # else:
    #     return("not available")
    # f = codecs.open("kannada-text.txt", encoding='utf-8')
    # for line in f:
        # return (line)
    # with open("test.txt","r") as test_file:
                                                                    #     data = []
                                                                    #     read_test = test_file.read()
                                                                #     for row in read_test:
                                                                    #         data.append(row)
                                                                    #         # eval(data)
                                                                    # dick = data
    # return()

