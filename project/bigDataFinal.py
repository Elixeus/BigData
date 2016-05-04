from string import punctuation, maketrans
import sys


def eventWordCount(index, lines):
    '''
    author: Xia Wang
    This function maps the candidates of each election cycle and return a
    tuple of (candidate name, media attitude). It first makes sure the
    encoding is utf-8 because there are characters like e' that cannot be
    decoded by the ancsii codec. Then it parse the http string (last column
    of the input files) to find out if the last name of a candidate is present.
    For the rows where candidate names are present, the name of the candidate and
    the media attitude towards it will be output as a tuple.

    TODO: The function uses a list of corresponding candidate names. Decide whether
    to create this list internally to each map script and use a different map script
    for each election cycle, or to create a csv file with the list provided. Also
    modify the __main__ part, specify how the map takes place.

    parameters:
    ----------------------

    index: the index of the input file
    lines: the content of the row
    '''
    ls = set(['clinton', 'sanders', 'trump', 'cruz', 'rubio'])
    # do something about this list
    import csv
    from string import punctuation, maketrans
    import itertools
    if index == 0:
        lines.next()
    reader = csv.reader(itertools.imap(lambda x: x.encode('utf-8'), lines),
                        delimiter='\t')
    for row in reader:
        (day, score, url) = (row[1], row[34], row[-1])
        # find the corresponding info
        # change all punctuations to comma, change all
        # letter case to lower, and split the words
        words = set(url.lower()
                       .translate(maketrans(punctuation,
                                            ',' * len(punctuation)))
                       .split(','))
        if len(ls.intersection(words)) == 1:
            # ls is a set that contains all the relevant candidate names
            for candidate in list(ls.intersection(words)):
                yield (candidate, float(score), day)


if __name__ == '__main__':
    #    sc = pyspark.SparkContext()
    events = sc.textFile('20160425.export.CSV')
    # !!!!!!!do something here!!!!!!! events is the textFile RDD

    attitude = events.mapPartitionsWithIndex(eventWordCount).mapValues(lambda x:
                                                                       (x, 1)) \
        .reduceByKey(lambda x, y: (x[0] + y[0], x[1] + y[1]))
    # print counts
    attitude.saveAsTextFile('output3.txt')
