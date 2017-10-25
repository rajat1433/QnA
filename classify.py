# -*- coding: utf-8 -*-
"""
@author: Rajat
"""

s='''A two-and-half year old girl. Who was sleeping next to her mother. A daily wage labourer. 
On Saturday night was raped and murdered. Her body was found by the police on Sunday.  
The victims body was found behind Prayeja city area.Both the parents of the girl work as a daily labourers. 
Police are yet to trace the culprit.'''

if (s.find("raped") | s.find("abducted") | s.find("molested") | s.find("rape") | s.find("abused")):
    print("Its a rape Article/News")
else:
    print("Its not a rape article.")    


