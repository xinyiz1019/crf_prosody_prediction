# crf_prosody_prediction/crf
- based on CRFsuite
- training and 10-fold cross validation integrated in one file

1. crf_slash_cross
Predict the position of phrase boundary (slash) applying a very basic feature set, which includes:
    - token
    - base form of token
    - POS

2. crf_slash_cross_im
Predict the position of phrase boundary (slash) applying an improved feature set, which includes:
    - token
    - base form of token
    - POS
    - lexical stress pattern (according to CMU pronouncing dictionary)
    - n-gram features

3. crf_prsstress_cross_features / crf_stcstress_cross_features
Predict the position of phrase stress / sentence stress applying the improved feature set, which adds the followings compared the one applied in slash prediction:
    - word's backward position in phrase
    - phrase's backward position in sentence

4. crf_prsstress_cross_pslash / crf_stcstress_cross_pslash
Predict the position of phrase stress / sentence stress employing predicted position of phrase boundary (slash) as a feature.
Slash information comes from the prediction result of "crf_slash_cross_im".

5. crf_prsstress_cross_slash / crf_stcstress_cross_slash
Predict the position of phrase stress / sentence stress employing correct position of phrase boundary (slash) as a feature.
Slash information comes from the original manually annotated data.
