import requests

app_id = "7722809"
Beksultan_user_id = "41056505"
Aizhan_user_id = "84541674"
access_token = "25fc6fd491db480f88533fa68632210a7705dcd4ab65fb21cfe9bfcfec4a3a75f17e3146ca5b52e45a1b9"
v = "5.126"
URL = "https://api.vk.com/method/"


class vk_user():
    def __init__(self, user_id):
        self.user_id = str(user_id)

    def __str__(self):
        return "https://vk.com/id" + self.user_id

    def __and__(user1, user2):
        params = {"access_token": access_token, "v": v, "source_uid": user1.user_id, "target_uid": user2.user_id}
        getMutual_URL = URL + "friends.getMutual"
        friends = requests.get(getMutual_URL, params=params)
        friends_objects = []
        friends_str = ""
        for friend in friends.json()["response"]:
            friends_object = vk_user(friend)
            friends_str += "," + str(friend)
            friends_objects.append(friends_object)
        friends_str = friends_str[1:]
        print(Beksultan.get_info(friends_str))
        return friends_objects

    def get_params(self):
        return {"access_token": access_token, "v": v}

    def get_info(self, user_ids):
        get_info_URL = URL + "users.get"
        params = self.get_params()
        params["user_ids"] = user_ids
        info = requests.get(get_info_URL, params=params)
        friends_names = []
        for friend in info.json()["response"]:
            friends_names.append(friend["first_name"] + " " + friend["last_name"])
        return friends_names


if __name__ == "__main__":
    Beksultan = vk_user(Beksultan_user_id)
    Aizhan = vk_user(Aizhan_user_id)
    print(Aizhan)
    B_and_A_mutual_friends = Beksultan & Aizhan
