import json, pandas
from dataclasses import dataclass

@dataclass
class UNFOLLOWERS:
    FOLLOWERS_FILE_LOCATION = r"followers_1.json"
    FOLLOWING_FILE_LOCATION = r"following.json"

    def get_followers_data(self, file_loc)-> set:
        table = pandas.read_json(file_loc)["string_list_data"]
        temp_data = json.loads(table.to_json())
        result = set()
        for temp_data_index, temp_data_list in temp_data.items():
            temp_data = temp_data_list[0]
            result.add(temp_data["value"])
        return result

    def get_following_data(self, file_loc):
        following_table = pandas.read_json(file_loc)
        temp_data = json.loads(following_table.to_json())["relationships_following"]
        following = set()
        for temp_data_index, temp_data_dict in temp_data.items():
            temp_data_dict = temp_data_dict["string_list_data"][0]
            following.add(temp_data_dict["value"])
        return following


    def get_set_of_unfollowers(self) -> set:
        set_of_followers = self.get_followers_data(self.FOLLOWERS_FILE_LOCATION)
        set_of_following = self.get_following_data(self.FOLLOWING_FILE_LOCATION)
        set_of_unfollowers = set_of_following.difference(set_of_followers)
        return set_of_unfollowers


unfollow = UNFOLLOWERS()
print(unfollow.get_set_of_unfollowers())