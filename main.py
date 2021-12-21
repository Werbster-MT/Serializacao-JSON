import json

data = [1.70, 70.0]

with open('data.json', 'w', encoding = 'utf-8') as f:
    json.dump(data, f)

    print(isinstance(data, str))

with open('data.json', 'r') as f:
    resultado = json.load(f)
    print('Os dados recebidos do cliente são: {}'.format(resultado))

list = [1, 'simple', 'list']

with open('teste.json', 'w', encoding='utf-8') as f:
    json.dump(list, f)

print(list)
print(json.dumps(list))
