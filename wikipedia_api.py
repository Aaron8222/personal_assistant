from wikipedia import suggest, summary

def get_article(title):
    return summary(title, sentences=2)

#print(get_article('Bill Clinton'))