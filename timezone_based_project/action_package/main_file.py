import sys
from logger_file import logger
# from logger_module
from datetime_module.datetime_module import DateTimeModule
from utils import INDIA_TIMEZONE,USA_TIMEZONE,DAY_STRING

class MainClass():

    def __init__(self,task_type,user,country,start_time,end_time,day):
        self.task_type = task_type
        self.user = user
        self.country = country
        self.start_time = start_time
        self.end_time = end_time
        self.day = day



    def proceed_timezone_check(self):
        """

        :return:
        """
        try:
            if None  in (task_type,user,country,start_time,end_time):
                print ("Please pass all mandatory field.None value is not acceptable")
            else:
                dateTimeModule = DateTimeModule()
                if country is not None:
                    timezone = self.get_time_zone(country)
                    if timezone is not None:
                        curr_datteime_dict = dateTimeModule.current_datetime(timezone)
                        cur_date = curr_datteime_dict.get("IST_Date")
                        cur_datetime_iso_obj = curr_datteime_dict.get("cur_datetime_iso_obj")
                        current_day = curr_datteime_dict.get("day")
                        star_time_status = self.check_time_format(start_time)
                        end_time_status = self.check_time_format(end_time)
                        if star_time_status and end_time_status:
                            star_time_obj = dateTimeModule.convert_str_datetime_obj(cur_date,start_time)
                            end_time_obj = dateTimeModule.convert_str_datetime_obj(cur_date,end_time)
                            if day is None:
                                self.check_action_time_period(cur_datetime_iso_obj,star_time_obj,end_time_obj)
                            else:
                                day_status = self.check_day_format()
                                if day_status:
                                    self.check_action_day_time_period\
                                        (cur_datetime_iso_obj,star_time_obj,end_time_obj,current_day,timezone)

        except Exception as e:
            logger.exception(e)

    def get_time_zone(self,country):
        """

        :return:
        """
        timezone = None
        country_lower_case = country.lower()
        if country_lower_case == "india":
            timezone = INDIA_TIMEZONE
        elif country_lower_case == "usa":
            timezone = USA_TIMEZONE
        else:
            print ("Country name does not exist in our database. We can only proceed to India and USA.")
        return timezone

    def check_action_time_period(self,currnt_time, start_time_obj,end_time_obj):
        """

        :param currnt_time:
        :param start_time:
        :param end_time:
        :return:
        """
        try:
            if start_time_obj <= currnt_time <= end_time_obj:
                print ("True")
            else:
                print ("False")
                print (start_time)
        except Exception as e:
            logger.exception(e)

    def check_action_day_time_period(self,cur_datetime_iso_obj,star_time_obj,end_time_obj,
                                     current_day,timezone_name):
        """

        :return:
        """
        try:
            dateTimeModule = DateTimeModule()
            day_lst = day.split(",")
            day_lower_lst = map(lambda x: x.lower(), day_lst)
            if current_day in day_lower_lst:
                if star_time_obj <= cur_datetime_iso_obj <= end_time_obj:
                    print ("True")
            else:
                count = 1
                next_action_day = ""
                while(next_action_day not in day_lower_lst):
                    next_action_day = dateTimeModule.get_next_day_data(count,timezone_name)
                    count = count + 1
                print (next_action_day, str(start_time))


        except Exception as e:
            logger.exception(e)

    def check_time_format(self,time_data):
        """

        :param time_data:
        :return:
        """
        try:
            status = True
            time_lst = time_data.split(":")
            if len(time_lst) ==3:
                hour = time_lst[0]
                min = time_lst[1]
                sec = time_lst[2]
                if hour.isdigit() == False:
                    status = False
                    print ("Time does not consider any non-numeric value")
                else:
                    if int(hour) >= 24 or  int(hour) <0:
                        status = False
                        print ("Hour value must be in 0-23")
                if min.isdigit() == False:
                    print ("Time doest not consider any non-numeric value")
                else:
                    if int(min) >=60 or int(min) <0:
                        status = False
                        print ("Minute value must be in 0-59")

                if sec.isdigit() == False:
                    status = False
                    print ("Time doest not consider any non-numeric value")
                else:
                    if int(sec) >=60 or int(sec) <0:
                        status = False
                        print ("Second value must be in 0-59")
            else:
                status = False
                print ("Time format is not acceptable. It should be like that `HH:MM:SS`")
            return status
        except Exception as e:
            logger.exception(e)

    def check_day_format(self):
        """

        :param day:
        :return:
        """
        try:
            status = True
            all_day_lst = DAY_STRING.split(",")
            input_day_lst = day.split(",")
            for input_day in input_day_lst:
                if input_day.lower() not in all_day_lst:
                    status = False
                    print ("Input day must be in given format :-  "+"'"+DAY_STRING+"'")
            return status
        except Exception as e:
            logger.exception(e)



if __name__ == "__main__":
    task_type = sys.argv[1]
    user = sys.argv[2]
    country = sys.argv[3]
    start_time = sys.argv[4]
    end_time = sys.argv[5]
    arg_len=  (str(sys.argv))
    day = None
    len_data = len(arg_len.split(","))
    if len_data >= 7:
        day = sys.argv[6]
    main = MainClass(task_type,user,country,start_time,end_time,day)
    main.proceed_timezone_check()
