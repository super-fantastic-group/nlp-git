# NLP - Scraping GitHub for Programming Languages
##### By Fred & Misty - Super Fantastic Team 

---

### Topic
Predicting the primary language used in a GitHub repository by anazlying their respective README.md

- Information was gathered by web scraping GitHub
- Data chosen for this set were repositories that were starred over a hundred times

- Present a summary of findings for a general audience using [google slides](https://docs.google.com/presentation/d/19CbSGQgPQwyDRF16-tnPGGmYLi81gsi-UCVJ_0p3UVg/edit#slide=id.gc6f9e470d_0_0)

---

### Contents

    Jupyter Notebook    nlp-project.ipynb
    Notebook that thoroughly demonstrates the steps involved in performing analysis on the provided data

    Python Modules      acquire, prepare, explore, model
    Modules containing the functions that are used in the Notebook

    Data                data_final.json, URL_list_100.csv
    JSON file with the contents of each readme, the language Github has labeled for each repo, and their URL
    CSV that contains the urls of the scrapped repositories

    Prediction Model    dec_tree_model.p
    A pickle file that stores a the machine learning algorithm fitted to the training data used in the analysis

    Data Dictionary     data_dict.txt
    Definitions of each of the data fields used

