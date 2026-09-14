import requests
import json 
import base64
import os

#from dotenv import load_dotenv
#load_dotenv()
#annict_access_token=os.getenv("annict_access_token", None)

annict_access_token=os.getenv("annict-badge-key", None)

def Get_annict_user_data(user_id):
    url = 'https://api.annict.com/v1/users?access_token={0}&filter_usernames={1}'.format("6M6pPs-Ciw5LNYsBoW3DhO2hGPSObmuA28-HGs3ppAs",user_id)
    user_json_data = requests.get(url).text

    print(url,user_json_data)
    print(len(annict_access_token),annict_access_token is None)

    user_data=json.loads(user_json_data)
    return user_data

Get_annict_user_data("PeunginCabinet")

def Get_Badge_URL(text1,text2,color,style):
    return "https://img.shields.io/badge/{0}-{1}-{2}?style={3}".format(text1,text2,color,style)
    
def Annict(request):
    headers = {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'GET',
        'Access-Control-Allow-Headers': 'Content-Type',
        'Access-Control-Max-Age': '3600',
        "Content-Type": "image/svg+xml",
    }

    args = request.args.to_dict()

    user_id = args.get('user_id')
    if user_id is None:
        return ("The 'user_id' query parameter is missing.",400,{})

    annict_data=Get_annict_user_data(user_id)

    type_data = args.get('type')
    if type_data is None:
        return ("The 'type' query parameter is missing.",400,{})

    style = args.get('style')
    if style is None:
        style=""

    Get_Badge_URL_args_list={
        "followings_count":["Annict followings","lightgrey"],
        "followers_count":["Annict followers","lightgrey"],
        "records_count":["Annict recorded animes","brightgreen"],
        "wanna_watch_count":["Annict wanna watch animes","important"],
        "watching_count":["Annict watching animes","blue"],
        "watched_count":["Annict watched animes","green"],
        "on_hold_count":["Annict animes on hold","red"],
        "stop_watching_count":["Annict animes stopped watching","inactive"],
        "created_at":["Annict created at","brightgreen"]
    }

    hit_flag=False
    for key_type_data,Get_Badge_URL_args in Get_Badge_URL_args_list.items():
        if type_data==key_type_data:
            text2=str(annict_data["users"][0][type_data])
            if key_type_data=="created_at":
                text2=text2.replace("-"," ")
            badge=requests.get(Get_Badge_URL(Get_Badge_URL_args[0],text2,Get_Badge_URL_args[1],style)).text
            hit_flag=True
            break

    if hit_flag==False:
        return ("The 'type' query parameter is incorrect.",400,{})

    return (badge,200,headers)
