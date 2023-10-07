from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline

tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-large")
model = AutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-large")
chatbot = pipeline("text-generation", model=model, tokenizer=tokenizer)


print(chatbot("hello!")[0]['generated_text'])