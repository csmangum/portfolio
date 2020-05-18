import spacy
from spacy.matcher import Matcher
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Load Spacy nlp library
nlp = spacy.load("en_core_web_lg")

# Functions
def sentiment_scale(num):
    """ Seperates the sentiment score into a usable category
        Returns: string
    """

    if num >= 0.3 and num < 0.6: scale ='slightly_positive'
    elif num >= 0.6: scale ='positive'
    elif num <= -0.3 and num > -0.6: scale ='slightly_negative'
    elif num <= -0.6: scale ='negative'
    else: scale = 'neutral'

    return scale


def sentiment_scores(sentence):
    """ Calculates the sentiment of the inputed text
        Returns: dictionary of sentiment scores and the categorical sentiment
    """

    sid_obj = SentimentIntensityAnalyzer()

    sentiment_dict = sid_obj.polarity_scores(sentence)

    compound_sentiment = sentiment_scale(sentiment_dict['compound'])

    return {'sentiment_scores':sentiment_dict, 'compound_sentiment':compound_sentiment}


def get_names():
    """ Identify the list of full names and associated details
        Returns: dictionary
    """
    # Get lis of unique full names
    lst = [str(e) for e in doc.ents if e.label_ == 'PERSON']

    lst.sort(key=len, reverse=True)

    full_names = []

    for l in lst:
        if str(l) not in str(full_names):
            full_names.append(str(l))

    all_mentions = [{'name':e.text, 'position':(e.start_char, e.end_char)} for e in doc.ents if e.label_ == 'PERSON']

    return full_names, all_mentions


def main():
    """ Performs the main bit of processing to get all mentions of each named entity,
        locations and sentiments
        Returns: dictionary
    """

    people = []

    for person in full_names:                                                   # Iterate through every named entity

        sentiments = []
        all_mentions = []
        individual = dict()

        for name in each_mentions:
            if name['name'] in person:                                          # Skip if the string is not in main fullname
                for s in doc.sents:
                    if name['position'][0] in range(s.start_char,s.end_char):   # Get the sentence span
                        if str(s) not in all_mentions:

                            all_mentions.append(str(s))

                            result = sentiment_scores(str(s))
                            result['location'] = name['position']
                            result['sentence_span'] = (s.start_char,s.end_char)

                            sentiments.append(result)
            else:
                continue

        joined_sentences = ','.join(all_mentions)                               # Join all sentences with mention to named entity

        sent_result = sentiment_scores(joined_sentences)                        # Get sentiment score for all mentions in the article
        individual['name'] = person
        individual['all_mentions_sentiment'] = sent_result
        individual['mentions'] = sentiments

        people.append(individual)                                               # Append the named entity

    return people

# Main loop
count = 1

for ids in article_ids:                                                         # loop through every article id

    article =  posts.find_one({"_id": ids})
    text = article['full_text']

    doc = nlp(text)

    full_names, each_mentions = get_names()                                     # Get names and mentions

    people = main()                                                             # Find every location and sentiment

    article_sentiment = sentiment_scores(str(doc.text))                         # Calculate sentiment of the article as a whole

    count += 1

if count % 1000 == 0:
    print(f'{count} articles updated')
