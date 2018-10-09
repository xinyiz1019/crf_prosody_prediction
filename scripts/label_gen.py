#Generate text files with POS and slash labels from original text
#POS label from NLTK
#slash label from original manually annotated data

import os
import nltk

def pruning(f_in):
    ##append " " (space) to symbols to simplify the segmentation of a sentence
    text=f_in.readline()[:-1]
    if '.' in text:
        text=text.replace('.',' .')
    if ',' in text:
        text=text.replace(',',' ,')
    if '?' in text:
        text=text.replace('?',' ?')
    if '!' in text:
        text=text.replace('!',' !')
    if ';' in text:
        text=text.replace(';',' ;')
    if ':' in text:
        text=text.replace(':',' :')
    if '" ' in text:
        text=text.replace('" ',' " ')
    if ' ”' in text:
        text=text.replace(' "',' " ')
    return text

##input & output path
in_path='../data/txt/'
out_path='../data/txt_with_pos/'
if not os.path.exists(out_path):
    os.makedirs(out_path)

##input files
files_ori=os.listdir(in_path)
files=[]
for efile in files_ori:
    if '.txt' in efile:
        files.append(efile)

##generate POS with NLTK
for efile in files:
    f_in=open(in_path+efile, 'r')
    text=pruning(f_in)##deal with symbols in text    
    tokens=text.split(' ')##generate list of tokens
    f_pos=str(nltk.pos_tag(tokens))
    f_out=open(out_path+efile, 'w')
    f_out.write(f_pos)
    f_out.close()

##generate(read) slash from original text 
in_path2='../data/txt_with_stress/'
out_path2='../data/txt_with_stresslabel/'
if not os.path.exists(out_path2):
    os.makedirs(out_path2)
files_ori=os.listdir(in_path2)
files=[]
for efile in files_ori:
    if '.txt' in efile:
        files.append(efile)
for efile in files:
    f=open(in_path2+efile,'r')
    t_with_s=f.readlines()
    if len(t_with_s)!=2:
        print(efile, '\nlength error!')
    syllable_index=[i for i,x in enumerate(t_with_s[0]) if x=='|']
    for a in syllable_index:
        if t_with_s[1][a]!=' ':
            print(efile, '\nspace error!')
            
    ##add pos label to result
    start=0
    word_index=[]
    space=0
    for i in syllable_index:
        for n in range(start, i):
            if t_with_s[1][n]==' ':
                space+=1
        word_index.append(space)
        space+=1
        start=i+1
    f_label=open(out_path+efile,'r')
    words=f_label.read()[2:-2].split('), (')
    for n in range(len(words)):
        if n in word_index:
            words[n]=words[n]+", 'S'"
        else:
            words[n]=words[n]+", 'N'"
    words='), ('.join(words)
    f_out2=open(out_path2+efile,'w')
    f_out2.write('[('+words+')]')
    f_out2.close()