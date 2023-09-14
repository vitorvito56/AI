import openai

#This program can have problems bases on your data plan for chat gpt (in special free plans)

openai.api_key = NULL # You need to put your own key, you can find on https://platform.openai.com/account/api-keys

x= input("Digite o que deseja")

resposta = openai.Completion.create( model="gpt-3.5-turbo",
                                     messages = [{ "role": "system", "context" : "Angry Assistant"},
                                     {"role": "user", "context": x
                                                  
                                                                           }])

print(resposta.choices[0].message["content"])

