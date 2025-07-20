from googleapiclient.errors import HttpError
from utils import *
import globals

def get_message_batch(service):
    service.users().messages().list(userId='me', q='').execute()
    response = service.users().messages().list(userId='me', q=globals.query, maxResults=globals.request_size).execute()
    messages = response.get('messages', [])
    return messages

def display_msg(service, msg):
        msg_id = msg['id']
        message = service.users().messages().get(userId='me', id=msg_id, format='metadata').execute()
        headers = message['payload']['headers']

        subject = '(No Subject)'
        for header in headers:
            if header['name'] == 'Subject':
                subject = header['value']
                break

        print(f"Message ID: {msg_id} | Subject: {subject}")
        return message

def batch_info(service, messages):
    batch_size = 0
    msg_ids = []
    for msg in messages:
        try:
            msg_id = msg['id']
            msg_ids.append(msg_id)
            message = display_msg(service,msg)
            size = message.get('sizeEstimate', 0)
            batch_size += size
            globals.total_del += 1
        except HttpError as error:
            print(f"{RED}Skipped message {msg_id}: {error} {RESET}")
            continue
    print(f"{CYAN}Gmail batch deleted of size {batch_size / (1024*1024):.2f} MB {RESET}")
    globals.total_size += batch_size
    return msg_ids

def batch_delete_callback(request_id, response, exception):
    if exception:
        print(f"{RED}Error deleting message {request_id}: {exception} {RESET}")
    else:
        print(f"{GREEN}Deleted message {request_id} {RESET}")

def batch_delete_messages(service, message_ids):
    batch = service.new_batch_http_request(callback=batch_delete_callback)

    for msg_id in message_ids:
        batch.add(service.users().messages().delete(userId='me', id=msg_id), request_id=msg_id)

    batch.execute()