#!/usr/bin/python3
'''
Text indetation module, splits the text
when special characters appears
and care the spaces that has a SC before
'''

def text_indentation(text):
   '''
   Is the module that splits the text
   '''
   if not (isinstance(text, str)):
      raise TypeError('text must be a string')

   for chars in range(len(text)):
      if (text[chars] is ' ' and
          (text[chars - 1] == '.' or text[chars - 1] == ':'
           or text[chars -1] == '?')) :
         continue
      print(text[chars], end='')
      if text[chars] == '.' or text[chars] == ':' or text[chars] == '?':
         print('\n')
