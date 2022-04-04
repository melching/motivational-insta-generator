from transformers import AutoTokenizer, AutoModel
import torch
import torch.nn.functional as F
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

tokenizer = AutoTokenizer.from_pretrained('sentence-transformers/all-MiniLM-L6-v2')
model = AutoModel.from_pretrained('sentence-transformers/all-MiniLM-L6-v2')

def mean_pooling(model_output, attention_mask):
    token_embeddings = model_output["last_hidden_state"]
    input_mask_expanded = attention_mask.unsqueeze(-1).expand(token_embeddings.size()).float()
    return torch.sum(token_embeddings * input_mask_expanded, 1) / torch.clamp(input_mask_expanded.sum(1), min=1e-9)

# following https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2
def get_sentence_embedding(model, sentences):
    encoded_input = tokenizer(sentences, padding=True, truncation=True, return_tensors='pt')
    with torch.no_grad():
        model_output = model(**encoded_input)
    sentence_embeddings = mean_pooling(model_output, encoded_input['attention_mask'])
    sentence_embeddings = F.normalize(sentence_embeddings, p=2, dim=1)
    return sentence_embeddings

def get_candidates_from_input(sentences):
    # need better candidate selection
    count = CountVectorizer(ngram_range=(1,1), stop_words="english").fit(sentences)
    candidates = list(count.get_feature_names_out())
    return list(candidates)

def get_keywords_using_embedding_similarity(sentences, top_n=5):
    sentence = ""
    for s in sentences:
        sentence += s + " "
    
    canditates = get_candidates_from_input([sentence])
    if len(canditates) < top_n:
        top_n = len(canditates)
    
    sentence_embed = get_sentence_embedding(model, sentence)
    canditate_embed = get_sentence_embedding(model, canditates)
    cosine_sim = cosine_similarity(sentence_embed, canditate_embed)

    keywords = [canditates[i] for i in cosine_sim.argsort()[0]][::-1][:top_n]
    return keywords

def pad_keywords(keywords, padding=["nature", "inspirational"]):
    keywords = keywords + padding
    return list(set(keywords)) # remove duplicates