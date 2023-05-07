# Import necessary libraries
import tensorflow as tf
import pandas as pd
import numpy as np

def load_data(file):
    data = pd.read_csv(filepath_or_buffer = 'school_shit\machine learning\Person A,Person B.csv', names = ['qestion', 'answer'])
    return(data)

def preprocess(data):
  # Tokenize the text
  tokenized_data = [tokenize(text) for text in data]

  # Convert to lowercase
  lowercased_data = [[word.lower() for word in text] for text in tokenized_data]

  # Remove special characters
  preprocessed_data = []
  for text in lowercased_data:
    filtered_text = []
    for word in text:
      filtered_text.append(re.sub(r'[^\w\s]', '', word))
    preprocessed_data.append(filtered_text)

  # Return preprocessed data
  return preprocessed_data

#data needs to be a .csv file
def split_data(data):
  # Convert the dataframe to a list of lists
  data = load_data()
  x_data, Y_data  = data.split(80, 20)
  # Return the data
  return data



def create_model(input_dim, output_dim):
  # Initialize model
  
  model = tf.keras.Sequential()

  # Add an LSTM layer with 128 units
  model.add(tf.keras.layers.LSTM(128, input_shape=(None, input_dim)))

  # Add a dense layer with 64 units and ReLU activation
  model.add(tf.keras.layers.Dense(64, activation='relu'))

  # Add a dense output layer with a softmax activation
  model.add(tf.keras.layers.Dense(output_dim, activation='softmax'))

  # Return the model
  return model


# Compile and train the model
def train_model(model, data, val_data):
  # Compile the model with an optimizer and loss function
  model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

  # Train the model on the training data
  model.fit(data, epochs=5)

  # Evaluate the model on the validation data
  loss, accuracy = model.evaluate(val_data)

  # Print the evaluation results
  print("Loss:", loss)
  print("Accuracy:", accuracy)

  # Return the trained model
  return model


# Generate responses
def generate_response(model, prompt):
  # Tokenize and preprocess the prompt
  tokenized_prompt = tokenize(prompt)
  lowercased_prompt = [word.lower() for word in tokenized_prompt]
  filtered_prompt = [re.sub(r'[^\w\s]', '', word) for word in lowercased_prompt]
  # Encode the prompt as a sequence of integers
  encoded_prompt = [word_to_index[word] for word in filtered_prompt]
  # Pad the prompt to the maximum length
  padded_prompt = pad_sequences([encoded_prompt], maxlen=max_input_len, padding='pre', truncating='pre')
  # Use the model to generate a response to the prompt
  response = model.predict(padded_prompt)
  # Decode the response from a sequence of integers to a list of words
  decoded_response = [index_to_word[word_index] for word_index in response]
  # Join the words into a single string
  response_str = ' '.join(decoded_response)
  # Return the response
  return response_str

# Main function
def main():
  # Load the data
  data = load_data('school_shit\machine learning\Person A,Person B.csv')
  # Preprocess the data
  data = preprocess(data)
  # Split the data into training and validation sets
  train_data, val_data = split_data(data)
  # Create the model
  model = create_model()
  # Train the model
  model = train_model(model, train_data, val_data)
  # Generate responses
  while True:
    prompt = input("Enter a prompt: ")
    response = generate_response(model, prompt)
    print(response)

# Run the main function
if __name__ == "__main__":
  main()
