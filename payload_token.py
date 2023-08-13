from copy import copy

import jwt
import datetime

payload = {
    'user': 'Jorik',
    'password': '7H"5y;un(}qV',
}


def encode_user_token(data: dict) -> str:
    data = copy(data)
    data.update({'sub': 'username',
                 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=15),
                 'iat': datetime.datetime.utcnow()})
    print(data)
    encoded_jwt = jwt.encode(data, key='secret', algorithm='HS256')
    return encoded_jwt


def decode_user_token(token: str) -> dict:
    try:
        decoded_jwt = jwt.decode(token, 'secret', algorithms=['HS256'])
        return decoded_jwt
    except:
        print('Error')
        return {}


print(encode_user_token(payload))
print(decode_user_token('eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjoiSm9yaWsiLCJwYXNzd29yZCI6IjdIXCI1eTt1bih9cVYiLCJzdWIiOiJ1c2VybmFtZSIsImV4cCI6MTY5MTk1NjMzMywiaWF0IjoxNjkxOTU1NDMzfQ.-XGqq9iiQvmMvxf6fdB0tS62cpr6yQs_Q4Nukslgu_o'))
