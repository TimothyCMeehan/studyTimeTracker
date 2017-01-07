import session

class Topic:
    
    def __init__(self, topic_name):
        self.__topic_name = topic_name
        self.__current_week = []
        self.__weeks = []
        self.__week_number = 0

    def get_this_weeks_total(self):

        total = 0

        for session in self.__current_week:
            total += session.get_duration()
            
        return total

    def convert_seconds_for_display(self, total):
        response = []
        response_string = ""
        days = total // 86400
        total = total % 86400
        hours = total // 3600
        total = total % 3600
        minutes = total // 60
        seconds = total % 60

        if days > 0:
            if days == 1:
                response.append("{} day".format(int(days)))
            else:
                response.append("{} days".format(int(days)))
        if hours > 0:
            if hours == 1:
                response.append("{} hour".format(int(hours)))
            else:
                response.append("{} hours".format(int(hours)))
 
        if minutes > 0:
            if minutes == 1:
                response.append("{} minute".format(int(minutes)))
            else:
                response.append("{} minutes".format(int(minutes)))
        if seconds > 0:
            if seconds == 1:
                response.append("{} second".format(int(seconds)))
            else:
                response.append("{} seconds".format(int(seconds)))

        if len(response) == 0:
            return "0 seconds"
        else:
            for i in range(len(response)):
                if (i == (len(response) - 1)) and (len(response) > 1) :
                    response_string += "and {}.".format(response[i])
                elif len(response) < 3:
                    response_string += "{} ".format(response[i])
                else:
                    #
                    response_string += "{}, ".format(response[i])
            return response_string
 
    
    def get_average(self):
        total = 0
        sessions = 0
        for week in self.__weeks:
            for session in week:
                total += session.get_duration()
                sessions += 1
                
        try:
            average = (total / sessions)
            return average

        except:
            return 0
   
    def __str__(self):
        #think about this one when you need it
        return " {}  |  Time Invested This Week: {}  |  Avg. Per Week: {}".format(self.__topic_name,
                                        self.convert_seconds_for_display(self.get_this_weeks_total()),
                                        self.convert_seconds_for_display(self.get_average()))
    
    def start_new_week(self):
        self.__weeks.append(self.__current_week)
        self.__current_week = []
        self.__week_number += 1

    def start_new_session(self, minutes=0):
        s = session.Session(minutes)
        self.__current_week.append(s)

    def end_session(self):
        self.__current_week[-1].end_session()

    def get_current_week(self):
        return self.__weeks[-1]

    def get_name(self):
        return self.__topic_name
