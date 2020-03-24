# 词向量训练
import jieba
from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence
import nltk.tokenize as tk
import re
import gensim.models as g

original_data = open('/mnt/project/NLPandNLG/nlg/data/original_data.txt', 'r', encoding='utf-8')

reduce_data = open('/mnt/project/NLPandNLG/nlg/data/reduce_data.txt', 'r', encoding='utf-8')

sentence_data = open('/mnt/project/NLPandNLG/nlg/data/sentence_data.txt', 'r', encoding='utf-8')

paragraph_data = open('/mnt/project/NLPandNLG/nlg/data/paragraph_data.txt', 'r', encoding='utf-8')

# paragraph_tagged_data = open('/mnt/project/NLPandNLG/nlg/data/paragraph_tagged_data.txt', 'r', encoding='utf-8')

# 分句
# sp = ['。', '！', '？', '\n']
# all_sentences = original_data.read()
# length = len(all_sentences)
# start = 0
# for i in range(length - 1):
#     t = all_sentences[i]
#     if all_sentences[i] in sp and all_sentences[i + 1] != '”':
#         sentence = all_sentences[start:i + 1]
#         start = i + 1
#         if sentence != '' and sentence != '\n' and '---------' not in sentence:
#             if '\n' in sentence:
#                 sentence = re.sub('\n', '', sentence)
#             print(sentence)
#             sentence_data.write(sentence + '\n')
# sentence_data.close()

# 词向量训练
# 分词
# all_sentences = sentence_data.readlines()
# l = []
# for sentence in all_sentences:
#     l = []
#     seg_list = list(jieba.cut(sentence))
#     for temp_term in seg_list:
#         l.append(temp_term)
#     reduce_data.write(' '.join(l))
# reduce_data.close()
# r_reduce_data = reduce_data.read()
# model = Word2Vec(LineSentence(reduce_data), sg=0, size=300, window=9, min_count=3, workers=8)
# model.save('/mnt/project/NLPandNLG/nlg/data/all_data_word2vec.model')

# 段落向量训练
# tagged分段
# original_lines = original_data.readlines()
# L = len(original_lines)
# documents = []
# for i in range(L - 1):
#     if original_lines[i] == '+++---\n':
#         title = re.sub('\n', '', original_lines[i + 1])
#         idoc_start = i + 3
#     elif original_lines[i] == '+++\n':
#         idoc_end = i - 1
#         tmp = original_lines[idoc_start:idoc_end + 1]
#         doc = ''
#         for t in tmp:
#             doc += t
#         doc = doc.strip('\n')
#         documents.append(g.doc2vec.TaggedDocument(doc, title))
# model = g.Doc2Vec(documents, dm=0, dbow_words=1, vector_size=300, window=8, min_count=19, epochs=5, workers=8)
# model.save('/mnt/project/NLPandNLG/nlg/data/all_data_doc2vec.model')
