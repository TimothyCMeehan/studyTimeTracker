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
        return " {}  |  Hours This Week: {}  |  Avg. Per Week: {}".format(self.__topic_name,
                                                                         self.get_this_weeks_total(), self.get_average())
    
    def start_new_week(self):
        self.__weeks.append(self.current_week)
        self.__current_week = []
        self.__week_number += 1

    def start_new_session(self):
        s = session.Session()
        self.__current_week.append(s)

    def end_session(self):
        self.__current_week[-1].end_session()

    def get_current_week(self):
        return self.__weeks[-1]

    def get_name(self):
        return self.__topic_name
