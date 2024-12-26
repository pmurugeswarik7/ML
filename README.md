# ML

# Save a model to a pickle file
```python
import pickle

with open('salary.pkl', 'wb') as file:
    pickle.dump(model, file)

from google.colab import files
files.download('salary.pkl')
