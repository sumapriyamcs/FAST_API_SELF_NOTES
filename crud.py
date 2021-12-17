from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

list_of_usernames=[]

@app.get("/home/{user_name}")

def write_home(user_name:str,query):
    return{
        "name":user_name,
        "age":24,
        "query":query
    }


@app.put("/user_name/{user_name}")
def put_data(user_name:str):
    print(user_name)
    list_of_usernames.append(user_name)
    return{
        "username":user_name
    }


@app.post("/postdata")  

def  post_data(user_name:str) :
  list_of_usernames.append(user_name)
  return{
        "usernames":list_of_usernames
  }


@app.delete("/deletedata/{user_name}")
def delete_data(user_name:str):
        list_of_usernames.remove(user_name)
        return{
            "usernames":list_of_usernames
        }

@app.api_route("/homedata",methods=['GET','POST','PUT','DELETE'])
def handle_homedata(username:str):
    print(username)
    return{
        "username":username
    }
    