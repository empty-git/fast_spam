import requests as requests

from config import LINK, BOT_TOKEN, MESSAGE_TEXT


def get_users():
    """
        request for scrap users
        check if site work and users  exist
    """
    try:
        users = []
        response = requests.get(url=LINK)
        if response.status_code == 200:
            length = len(response.text.split("\n"))
            if length > 0:
                users = response.text.split("</br>")
                print("Users get  -  Done !")
                return users
            else:
                print("Users not found !")
        print(f"Request bad!\nDescription: {response.text}\n")
        return None
    except Exception as e:
        print(f"Error in request - {e}\n")
        return None


def bot_spammer(users: list):
    """
        send message for send text by https request
    """
    API_URL = "https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}"
    sended_messages_count = 0
    error_messages_count = 0
    for user_id in users:
        try:
            response = requests.get(API_URL.format(BOT_TOKEN, user_id, MESSAGE_TEXT))
            if response.status_code == 200:
                json_file = response.json()
                if json_file['ok']:
                    sended_messages_count += 1
                print(f"Message for user with id - {user_id} DONE")
        except Exception as e:
            error_messages_count = +1
            print(f"Error while send request with message for user - {user_id}: {e}")
    print(F"RESULTS:\nMESSAGES SEND COUNT = {sended_messages_count}\nBad requests send count = {error_messages_count}")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    users = get_users()
    if users is not None:
        bot_spammer(users = users)
    else:
        print("USERS NOT FOUND")
