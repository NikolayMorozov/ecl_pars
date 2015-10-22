'''
Created on 21 Oct 2015

@author: NMorozov
'''

import numpy as np 


def parsingProps(fileName, properties):
    """
    reads one ECLIPSE *.F0000 file and reads specified properties form this file
    
    takes:
        fileName -  is a str
        properties  - dict of str:list, where str - propertyName, list expected to be empty
    returns:
        properties as a dictionary of  {str:list of real}
    """
    propName = None # name of property
    expectedValueCount = None # expected count of values 
    readingValues = False
    j = 0 # value read count for currently reading property
    
    try:

        f = open(fName)
        
        for line in f:
            line = line.translate(None,"'")
            line = line.strip()
            words = line.split()

            if len(words)>0:
                if readingValues:
                    
                    try: 
                        l1 = map(float, words)
                    except:
                        print "finish with error for", propName, "on value ", j
                        j = 0
                        properties[propName] = []
                        readingValues = False
                        expectedValueCount = None
                        propName = None                                            
                        continue
                    
                    properties[propName] = properties[propName] + l1
                    j += len(l1)
                    
                    if j == expectedValueCount:
                        print "finish with ", propName, j
                        j = 0
                        readingValues = False
                        expectedValueCount = None
                        propName = None
                        
                    if j > expectedValueCount and expectedValueCount != None:
                        print "Houston we have a problem", j
                
                if words[0] in properties:
                    expectedValueCount = int(words[1])
                    readingValues = True
                    propName = words[0]
                    print "let's read ", propName
    finally:
        f.close()      # closing
        print "done"
#        for p in properties:
#            print p, len(properties[p])
        return properties
 

def propToNpArray(property, nX, nY):
    """
        creates numpy array from property given NX, NY
        
        
    """
    
    
    return npArray
        

if __name__ == '__main__':
    fName = "D:/Project/Dubai/Clients/Fab/Dome2015/dome.sim/ECL/ECL.F0000"
    
    properties = {"PRESSURE":[],"SWAT":[], "SOIL":[]}
    properties = parsingProps(fName, properties)

    for p in properties:
        print p, len(properties[p])
    


  
    
                     

                        

#                 faces.append(face(line))
#             if i >= 100: # trim to save time on start
#                 break
#             i += 1
# 

