interests = [ 
    (0, "Hadoop"), (0, "Big Data"), (0, "HBase"), (0, "Java"), 
    (0, "Spark"), (0, "Storm"), (0, "Cassandra"), 
    (1, "NoSQL"), (1, "MongoDB"), (1, "Cassandra"), (1, "HBase"), 
    (1, "Postgres"), (2, "Python"), (2, "scikit-learn"), (2, "scipy"), 
    (2, "numpy"), (2, "statsmodels"), (2, "pandas"), (3, "R"), (3, "Python"), 
    (3, "statistics"), (3, "regression"), (3, "probability"), 
    (4, "machine learning"), (4, "regression"), (4, "decision trees"), 
    (4, "libsvm"), (5, "Python"), (5, "R"), (5, "Java"), (5, "C++"), 
    (5, "Haskell"), (5, "programming languages"), (6, "statistics"), 
    (6, "probability"), (6, "mathematics"), (6, "theory"), 
    (7, "machine learning"), (7, "scikit-learn"), (7, "Mahout"), 
    (7, "neural networks"), (8, "neural networks"), (8, "deep learning"), 
    (8, "Big Data"), (8, "artificial intelligence"), (9, "Hadoop"), 
    (9, "Java"), (9, "MapReduce"), (9, "Big Data") 
]


# One simple (if not particularly exciting) way to find the most popular
 # interests is to count the words:
 # 1. Lowercase each interest (since different users may or may not
 # capitalize their interests).
 # 2. Split it into words.
 # 3. Count the results.
 # In code:
 
 words_and_counts = Counter(word
                            for user, interest in interests
                            for word in interest.lower().split())


for word, count in words_and_counts.most_common():
    if count > 1:
        print(word, count)
        

# which gives the results you’d expect (unless you expect “scikit-learn” to get
# split into two words, in which case it doesn’t give the results you expect):
# learning 3 
# java 3 
# python 3 
# big 3 
# data 3 
# hbase 2 
# regression 2 
# cassandra 2 
# statistics 2 
# probability 2 
# hadoop 2 
# networks 2 
# machine 2 
# neural 2 
# scikit-learn 2 
# r 2        

