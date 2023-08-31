Install environment with command ```pip install .```

You can find examples on how to embed data and use ChatGPT 3.5 in the ```chatGPTexamples.py``` file

# Key and models
azure_openai_key = ff9de7d753b5443b9846bfb3de8e6edb
azure_openai_endpoint = https://cs-openai-us-jml.openai.azure.com/

embedding_model = text-embedding-ada-002
embedding_model_deployment = text-embedding-ada-002

chatgpt_model = gpt-35-turbo
chatgpt_model_deployment = gpt-35-turbo

# Goals of the case
Create a chatbot using Azure OpenAI that can answer questions about Queen Margrethe’s new years speeches for the past 20 years.

3 hours before the case ends, we will send out a list of questions that the Chatbot should be able to answer. 

The team with the best answers win

As a bonus question - Each team creates one question for the other teams that their own chatbot can answer. 

# Tips on approaching the case
Start figuring out how to convert the documents into vectors. OpenAI has a good tutorial that gives an example on how to do this: https://platform.openai.com/docs/tutorials/web-qa-embeddings

Once the documents are ready, and you have an idea on how to fetch context for ChatGPT, start experimenting with how ChatGPT responds

You can try to use a vector store to store the generated embeddings, however you can also just use numpy to store and search for vectors if you want to reduce complexity.

Some evaluation questions will be focused on what year the queen mentioned a specific topic. Plan for this

If you feel stuck on the quality of responses, there are some immediate things you can look into:
Revisit data chunking and/or preprocessing before vectorizing it. You can use Llama index for this, but you don’t have to

Reduce question into multiple sub questions. You can use Langchain if you want to, but you don’t have to

# Evaluation criteria
Each chatbot will be evaluated on:

The answers it gives to the questions we send you

The answers it gives to the questions other teams have created
