import ollama

note = '../notes.md'

with open(note, 'r') as file:
    content = file.read()

my_prompt = f'This is a personal note, what is it about? {content}'

response = ollama.generate(model='llama2-uncensored', prompt=my_prompt)

actual_response = response['response']

print(actual_response)