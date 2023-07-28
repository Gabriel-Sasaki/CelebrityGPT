import openai

MODEL = 'gpt-3.5-turbo'

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def configure_api(organization_key, api_key):
    openai.organization = organization_key
    openai.api_key = api_key

try:
    organization_key = input(f'Organization Key: {bcolors.OKBLUE}')
    print(bcolors.ENDC, end='')
    api_key = input(f'API Key: {bcolors.OKBLUE}')
    print(bcolors.ENDC)
    configure_api(organization_key, api_key)
    
    celebrity = input(f'Digite a celebridade que você deseja conversar: {bcolors.OKBLUE}')
    print(bcolors.ENDC, end='')
    
    user_input = ''
    messages = []
    print('Para sair da conversa digite SAIR a qualquer momento!')
    print(f'Comece sua conversa com {celebrity}:', end='\n')
    while user_input != 'SAIR':
        print()
        user_input = input(f'>>> {bcolors.OKBLUE}')
        print(bcolors.ENDC)
        if user_input == 'SAIR':
            break
        messages.append({
            'role': 'user',
            'content': f'Responda a seguinte mensagem como se você fosse {celebrity} e estivessem em uma conversa casual: {user_input}'
        })
        response = openai.ChatCompletion.create(model=MODEL, messages=messages)
        messages.append(response.choices[0].message)
        
        print(celebrity, response.choices[0].message.content, sep=f'{bcolors.OKGREEN}: ', end=f'{bcolors.ENDC}\n')
        
except openai.error.AuthenticationError as error:
    print(error)

except openai.error.RateLimitError as error:
    print(error)