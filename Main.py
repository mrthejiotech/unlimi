print(f"""
┏━━━━━━━━━━━━━━━━━━━━━━━━━━┓           
❖ › Channel :- @EDITIONDARK 
❖ › By      :- @HIIAMDARK
┗━━━━━━━━━━━━━━━━━━━━━━━━━━┛                """)
print('\x1b[38;5;208m⇼'*60)
print('\x1b[38;5;22m•'*60)
print('\x1b[38;5;22m•'*60)
print('\x1b[38;5;208m⇼'*60)
import requests
import random
import string
import json
import hashlib
from faker import Faker

# Function to generate a random string
def generate_random_string(length):
    letters_and_digits = string.ascii_letters + string.digits
    return ''.join(random.choice(letters_and_digits) for i in range(length))

# Function to get available mail domains from mail.tm
def get_mail_domains():
    url = "https://api.mail.tm/domains"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()['hydra:member']
        else:
            print(f'[×] E-mail Error : {response.text}')
            return None
    except Exception as e:
        print(f'[×] Error : {e}')
        return None

# Function to create a mail.tm account
def create_mail_tm_account():
    fake = Faker()
    mail_domains = get_mail_domains()
    if mail_domains:
        domain = random.choice(mail_domains)['domain']
        username = generate_random_string(10)
        password = fake.password()
        birthday = fake.date_of_birth(minimum_age=18, maximum_age=45)
        first_name = fake.first_name()
        last_name = fake.last_name()
        url = "https://api.mail.tm/accounts"
        headers = {"Content-Type": "application/json"}
        data = {"address": f"{username}@{domain}", "password":password}       
        try:
            response = requests.post(url, headers=headers, json=data)
            if response.status_code == 201:
                return f"{username}@{domain}", password, first_name, last_name, birthday
            else:
                print(f'[×] Email Error : {response.text}')
                return None, None, None, None, None
        except Exception as e:
            print(f'[×] Error : {e}')
            return None, None, None, None, None

# Function to register a Facebook account
def register_facebook_account(email, password, first_name, last_name, birthday):
    api_key = '882a8490361da98702bf97a021ddc14d'
    secret = '62f8ce9f74b12f84c123cc23437a4a32'
    gender = random.choice(['M', 'F'])
    req = {'api_key': api_key,'attempt_login': True,'birthday': birthday.strftime('%Y-%m-%d'),'client_country_code': 'EN','fb_api_caller_class': 'com.facebook.registration.protocol.RegisterAccountMethod','fb_api_req_friendly_name': 'registerAccount','firstname': first_name,'format': 'json','gender': gender,'lastname': last_name,'email': email,'locale': 'en_US','method': 'user.register','password': password,'reg_instance': generate_random_string(32),'return_multiple_errors': True}
    sorted_req = sorted(req.items(), key=lambda x: x[0])
    sig = ''.join(f'{k}={v}' for k, v in sorted_req)
    ensig = hashlib.md5((sig + secret).encode()).hexdigest()
    req['sig'] = ensig
    api_url = 'https://b-api.facebook.com/method/user.register'
    reg = _call(api_url, req)
    id=reg['new_user_id']
    token=reg['session_info']['access_token']
    return id, token

# Function to make an API call
def _call(url, params, post=True):
    headers = {'User-Agent': '[FBAN/FB4A;FBAV/35.0.0.48.273;FBDM/{density=1.33125,width=800,height=1205};FBLC/en_US;FBCR/;FBPN/com.facebook.katana;FBDV/Nexus 7;FBSV/4.1.1;FBBK/0;]'}
    if post:
        response = requests.post(url, data=params, headers=headers)
    else:
        response = requests.get(url, params=params, headers=headers)
    return response.json()

# Telegram bot token
bot_token = "6811878976:AAGl7DhIBSKejt2bKzGpvEguu4HhEKr7iDs"
# Telegram chat ID
chat_id = "5506358369"

# Function to send a message to Telegram
def send_message_to_telegram(message):
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    data = {"chat_id": chat_id, "text": message}
    response = requests.post(url, data=data)
    if response.status_code == 200:
        print("Message sent successfully to Telegram!")
    else:
        print("Failed to send message to Telegram.")

# Main function
def main():
    message_template = """

┏━━━━━━━━━━━━━━━━━━━━━━━━━━┓           
❖ › Channel :- @EDITIONDARK 
❖ › By      :- @HIIAMDARK
┗━━━━━━━━━━━━━━━━━━━━━━━━━━┛                
⋘▬▭▬▭▬▭▬﴾𓆩OK𓆪﴿▬▭▬▭▬▭▬⋙
[VB] EMAIL : {email}
[VB] ID : {id}
[VB] PASSWORD : {password}
[VB] NAME : {first_name} {last_name}
[VB] BIRTHDAY : {birthday} 
[VB] GENDER : {gender}
⋘▬▭▬▭▬▭▬﴾𓆩OK𓆪﴿▬▭▬▭▬▭▬⋙
[VB] Token : {token}

BY @HIIAMDARK

Team.
DARK EMPIRE
⋘▬▭▬▭▬▭▬﴾𓆩OK𓆪﴿▬▭▬▭▬▭▬⋙
"""

    # Number of accounts to create
    num_accounts = 1000000000000000000000000000000

    for i in range(num_accounts):
        email, password, first_name, last_name, birthday = create_mail_tm_account()
        if email and password and first_name and last_name and birthday:
            user_id, token = register_facebook_account(email, password, first_name, last_name, birthday)
            message = message_template.format(email=email, id=user_id, password=password, first_name=first_name, last_name=last_name, birthday=birthday, gender=random.choice(['M', 'F']), token=token)
            # Send message to Telegram
            send_message_to_telegram(message)

    print('\x1b[38;5;208m⇼'*60)

# Execute the main function
if __name__ == "__main__":
    main()
    
