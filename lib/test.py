from kavenegar import *

from lib.local_setting import KAVENEGAR_API


def send_sms(user_phone, message):
    try:
        api = KavenegarAPI(KAVENEGAR_API)
        params = {
            'receptor': str(user_phone),  # User's phone number
            'message':message ,  # Message to send
        }
        response = api.sms_send(params)  # Send SMS

        # Ensure the response is of the correct type (list or dict)
        if isinstance(response, list):
            print(f"SMS sent successfully. Response: {response}")
        else:
            print(f"Unexpected response format. Response: {response}")

    except APIException as e:
        print(f"Kavenegar APIException: {str(e)}")
    except HTTPException as e:
        print(f"Kavenegar HTTPException: {str(e)}")
    except Exception as e:
        print(f"Unexpected error occurred while sending SMS: {str(e)}")
if __name__ =='__main__':
    send_sms('9376522710', 'hiii')
