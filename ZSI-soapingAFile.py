from ZSI import ParsedSoap, TC
from pprint import pprint
import unittest

def soap_parse_ZSI(xml):
    ''' This function receives an XML SOAP and returns a dictionary. It is
    intended to be used inside a Node, this is why it raises a NodeParserError
    '''

    parsed_obj = None
    parsed_dict = dict()

    try:
        parsed_obj = ParsedSoap(xml)
        parsed_dict = parsed_obj.Parse(TC.Any())
        
    except Exception, e:
        print e

    return parsed_obj, parsed_dict

def openFile(file):
    
    f = open( file, 'r' )
    contents = f.read()
    f.close()

    return contents

def main( xml ):

    o, d = soap_parse_ZSI( xml )
    return o, d


    
if __name__ == '__main__':
    file = 'data4'

    xml = openFile( file )
    
    xml = xml.replace('xsi:type="m1:PolicyException"', '')
    Obj, Dic = main( xml )

    #print Dic

    #assertEqual(Obj.body_root,'Fault')

    #print Obj.data_elements.Fault
    #exit()

    #{'detail': {
        #'PolicyException': {
            #'messageId': u'SVC0001',
            #'text': u'DP019: Short-code tel:+14166295230 is not in the list of allowed short-codes for this application'}},
    #'faultcode': u'SOAP-ENV:Server',
    #'faultstring': None}

    if Dic:
        faultcode = Dic.get('faultcode')
        
        #messageID = Obj.body_root.detail.PolicyException.messageId
        #print messageID
        if faultcode: 
            print 'faultcode:\n%s' % faultcode

        if 'detail' in Dic:
            if 'PolicyException' in Dic['detail']:
                pe = Dic['detail']['PolicyException']

                messageId = pe.get('messageId')
                print 'msgId: %s' % messageId

                desc = pe.get('text')
                print 'desc: %s' % desc


        #pprint( Dic )
    #else:
    #    print Dic
