# NewContentAnalyzer (NCA)

## Yifei Yan, Steven Karson, Aditya Srivastava

### Files and Folders
##### Master_API
- Pulls news content using this file, specify news topic and sources, saves it to a json file structure
- Utilizes Event Registry API to pull news from selected sources

##### Master_File
- Performs pre-processing, vectorization, and LDA topic modeling for given topic and dataset
- Displays whether or not the new article contains new content at a given depth liven, given the user-specified hyperparameter
- Also provides visualizations of LDA topics, and lists the main topic of each article

##### Master_dataset
- Contains datasets of articles
- Data files labeled "new" contain an unread article with manually-labeld "new content"
- Data files labeled "old" contain an unread article with manually-labeld "old content"

### Research Question
- Given a set of articles one has read about a specific subject (i.e. a reading history), can we determine whether a new “unread” article about that subject contains new content or only content that has already been read in prior articles?

### Methods
- Collect a number of “read” articles on a given subject (e.g., the trade war) and one “unread” article, creating a collection of articles, denoted A
- Pre-process each article’s text
- Vectorize articles using TF-IDF Vectorizer
- Fit LDA model on the collection of articles A
- Transform articles into topic distributions using fitted LDA model
- Find the “main topic” of the “unread” article, and if its main topic is unique compared to those of the other articles, label it as “new content”
- Otherwise, if the hyperparameter depth = 1, then label the article as “old content”
- Otherwise, if the selected model depth ≥ 2, create a subset of articles in A, denoted B, which contains all articles that share the same main topic as the “unread” article
- Perform LDA again on the subset B
- Find the “main topic” of the “unread” article, and if its main topic is unique compared to those of the other articles, label it as “new content”, and otherwise, label it as “old content” if depth = 2
- If depth ≥ 3, continue the process of performing LDA on the subset of articles that share the same main topic as the “unread” article for that depth level, until the article is labeled “new content” or the model reaches its max depth

### Evaluation of Work
- To assess the Model’s ability to identify “new content”
	- The set of “read articles” are selected such that they were all published before a “cutoff” date prior to an important public release of information (e.g., Theresa May’s resignation). 
	- The selected “unread” article was published at a time after this “cutoff” date and describes this unexpected event and includes this new information
	- This guarantees the “unread” article contains new content since the old articles could not contain this new information

- Assessing the Model’s ability to identify “old content”
	- Given a collection of articles on a given subject, select an article which primarily contains information that is already included in the other articles, and label this article as “unread,” and label the others as “read”

- We evaluated our work on four subjects
	- Trade war news, Huawei news, Brexit news, and opioid epidemic news
	- For each news subject, we ran two tests, one in which the “unread” article was manually labeled as “new content,” and one in which a different “unread” article was labeled as “old content” based on our reading
	- In 7 out of 8 test cases, our model successfully identified whether the “unread” article contained “new content” or only “old content” with a depth level = 2

### Potential Futre Work
- Perform more in-depth analysis on the accuracy of the model by testing on more datasets
- Improve the accuracy of the model
- Improve the speed of the model
- Provide the percentage of new content in an article
- Highlight new content in an article
- Summarize new content in an article
- Suggest other articles with new content
- Create a timeline of new content to track new information over time


** This project was done under the supervison and direction of Professor Soroush Vosoughi in COSC 89.21: Data Mining & Knowledge Discovery.