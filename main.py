from fastapi import FastAPI
import uvicorn

app = FastAPI()
file_test = 'names.txt'


@app.get("/test")
def test():
    response = {'msg': 'hi from test'}
    return response

@app.get("/test/{name}")
def test_parm(names):
    with open(file_test, "a") as f:
            data =  {'msg': names}
            f.write(names)
            f.close()
            return data



app = FastAPI()

@app.post("/caesar")
def caesar_cipher(text: str, offset: int, mode: str):

    the_result = ""
    for char in text:
        if char.isalpha():
            the_letter = ord("a")
            if mode == "encrypt":
                the_result += chr((ord(char) - the_letter + offset) % 26 + the_letter)
            elif mode == "decrypt":
                the_result += chr((ord(char) - the_letter - offset) % 26 + the_letter)
        else:
            the_result += char

    if mode == "encrypt":
        return {"encrypted_text": the_result}
    elif mode == "decrypt":
        return {"decrypted_text": the_result}
    else:
        return {"you need just 'encrypt' or 'decrypt'"}
    # return


@app.get("/fence/encrypt")
def encrypt_cipher(text):
    text1 = text.split(" ")
    even = ""
    not_even = ""
    for i , x in enumerate(text1):
        if i % 2 == 0:
            even += x
        elif i % 2 != 0:
            not_even += x

    the_finish_text = not_even + even
    return the_finish_text

# #
@app.post("/fence/decrypt")
def decrypt_cipher(text:str):
    not_even = ""
    even = ""
    for i in range(len(text)):
        if i % 2 == 0:
            not_even += text[i]
        if i % 2 != 0:
            even += text[i]
    finish = even + not_even
    return finish

#






if __name__ == "__main__":
    uvicorn.run(app,host="localhost",port=8000)
