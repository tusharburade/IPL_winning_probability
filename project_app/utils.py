import pickle
import json
import config
import numpy as np

class IPLProbability():
    def __init__(self,batting_team,bowling_team,city,runs_left,balls_left,wickets,total_runs_x,crr,rrr):
        self.batting_team = "batting_team_" + batting_team
        self.bowling_team = "bowling_team_" + bowling_team
        self.city = "city_" + city
        self.runs_left = runs_left
        self.balls_left = balls_left
        self.wickets = wickets
        self.total_runs_x = total_runs_x
        self.crr = crr
        self.rrr = rrr

    def load_model(self):
        with open(config.model_file_path,'rb') as f:
            self.model = pickle.load(f)
        with open(config.json_file_path,'r') as f:
            self.json_data = json.load(f)

    def get_probability(self):
        self.load_model()
        batting_team_index = self.json_data['columns'].index(self.batting_team)
        bowling_team_index = self.json_data['columns'].index(self.bowling_team)
        city_index = self.json_data['columns'].index(self.city)
        test_array = np.zeros(len(self.json_data['columns']))
        test_array[0] = self.runs_left
        test_array[1] = self.balls_left
        test_array[2] = self.wickets
        test_array[3] = self.total_runs_x
        test_array[4] = self.crr
        test_array[5] = self.rrr
        test_array[batting_team_index] = 1
        test_array[bowling_team_index] = 1
        test_array[city_index] = 1

        probability = self.model.predict([test_array])

        #return f"Probability of winning of {self.batting_team} is {probability[0][1]} \n Probability of winning of {self.bowling_team} is {probability[0][0]}"
        return probability