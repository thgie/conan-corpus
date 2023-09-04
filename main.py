import json, os, pathlib, spacy

# clean extract file
if os.path.exists('conan_adj.json'):
    os.remove('conan_adj.json')

adjs = {}

# go through all the files in data folder
texts = sorted(os.listdir("the_conan_stories"))
for counter, file in enumerate(texts):

    print("Working on " + str(counter+1) + " of " + str(len(texts)) + ":")
    print(file+"\n")

    # check if it is a text file, just to make sure
    if file.endswith(".txt"):

        # load text file and remove new lines; we don't need those
        text = pathlib.Path(os.path.join("the_conan_stories", file)).read_text(encoding="utf-8")
        text = text.replace('-\n\n', '-').replace('\n\n', ' ').replace('  ', ' ')
        text = text.strip()

        # load the transformer model
        nlp = spacy.load("en_core_web_trf")

        # get all sentences in which Conan and other males are present
        phrase_matcher = spacy.matcher.PhraseMatcher(nlp.vocab)
        phrases = ['Conan']
        patterns = [nlp(text) for text in phrases]
        phrase_matcher.add('Conan', None, *patterns)

        # shredder that text
        doc = nlp(text)

        # go through all the sentences of the text
        for sent in doc.sents:

            # simple workaround to evade duplicates in the extract
            matched = False

            for match_id, start, end in phrase_matcher(nlp(sent.text)):

                if(matched):
                    continue

                # check if Conan or other males are present
                if nlp.vocab.strings[match_id] in ["Conan"]:

                    matched = True
                    
                    # check if sentence contains adjectives
                    pos_types = [token.pos_ for token in sent]
                    if "ADJ" in pos_types:
                        for token in sent:
                            if token.pos_ == "ADJ":
                                print(token.lemma_)
                                if token.lemma_ not in adjs:
                                    adjs[token.lemma_] = []
                                adjs[token.lemma_].append(sent.text)
        
# sort those adjectives
sorted_adjs = dict(sorted(adjs.items()))

# write those adjectives
json_adjs = json.dumps(sorted_adjs, indent=4)
with open("conan_adj.json", "w") as outfile:
    outfile.write(json_adjs)