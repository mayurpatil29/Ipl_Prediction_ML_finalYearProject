import pickle
with open('C:/AA/New folder/tree_model.pkl', 'rb') as f:
    data = pickle.load(f)
with open('filename.txt', 'w') as f:
    f.write(str(data))
