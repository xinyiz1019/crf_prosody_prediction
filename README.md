
# crf_prosody_prediction
demo code of prosodic events prediction applying CRFs

## ./scripts

Tools here can help with pre-processing the original data in diretory "./data/txt_with_stress".
One example of the original data looks like:

<a class="monospaced">
&nbsp&nbsp1&nbsp&nbsp&nbsp&nbsp&nbsp3&nbsp&nbsp&nbsp1&nbsp&nbsp|&nbsp&nbsp2&nbsp&nbsp1&nbsp&nbsp&nbsp1&nbsp&nbsp&nbsp&nbsp1&nbsp4&nbsp&nbsp1<br>   
Bright sunshine shimmers on the ocean. </a>

in which the numbers stand for the stress level of the corresponding syllable, and the "|" (vertical line) stands for phrase boundary.

By applying label_gen and sent_gen, the expected output looks like

[['Bright', 'NNP', 'N', 'NPS', 'NSS'], ['sunshine', 'NN', 'S', 'PS', 'NSS'], ['shimmers', 'NNS', 'N', 'NPS', 'NSS'], ['on', 'IN', 'N', 'NPS', 'NSS'], ['the', 'DT', 'N', 'NPS', 'NSS'], ['ocean', 'NN', 'N', 'PS', 'SS'], ['.', '.', '', 'NPS', 'NSS']]

in which the first label in each element is token itself, following POS tagging, slash information (S for having slash and N for no slash), phrase stress information and sentence stress information. 

Data like this are ready for the crf training.

## ./crf

The core programs of predicting prosodic events using crf and detailed description can be found here.

## publication
This research was poster presented at 2018 ASJ autumn meeting. The paper can be found here:
http://gavo.t.u-tokyo.ac.jp/~xinyi/ASJ_paper.pdf
