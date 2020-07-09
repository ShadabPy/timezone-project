from datetime import datetime, timedelta
from pytz import timezone


class DateTimeModule():

    def current_datetime(self,timezone_name):
        """

        :return:
        """
        try:
            datetime_dict = {}
            now_utc = datetime.now(timezone('UTC'))
            now_pacific = now_utc.astimezone(timezone(timezone_name))

            day_name = now_pacific.strftime("%A")
            current_date = now_pacific.strftime("%Y/%m/%d")
            current_ist_time = now_pacific.strftime("%H:%M:%S")

            date_fields = current_date.split('/')
            iso_date_hour_min_obj = None
            if len(date_fields) >= 3:
                time = (current_ist_time).split(':')
                if time is not None:
                    hour_int = int(time[0])
                    mint_int = int(time[1])
                    iso_date_hour_min_obj = datetime(int(date_fields[0]), int(date_fields[1]), int(date_fields[2]),
                                                     hour_int, mint_int, 0)

            datetime_dict["IST_Date"] = current_date
            datetime_dict["day"] = day_name.lower()
            datetime_dict["cur_datetime_iso_obj"] = iso_date_hour_min_obj
            return datetime_dict
        except Exception as e:
            print (e)

    def get_next_day_data(self,day_count,timezone_name):
        """

        :return:
        """
        try:
            now_utc = datetime.now(timezone('UTC'))
            now_pacific = now_utc.astimezone(timezone(timezone_name))
            now_pacific = now_pacific + timedelta(days=int(day_count))
            day_name = now_pacific.strftime("%A")
            return day_name.lower()

        except Exception as e:
           print (e)


    def convert_str_datetime_obj(self,str_date,str_time):
        """

        :param str_date:
        :param str_time:
        :return:
        """
        try:
            ist_datetime_obj = None
            date_fields = str_date.split('/')
            time = (str_time).split(':')
            if len(date_fields) >= 3:
                if time is not None:
                    hour_int = int(time[0])
                    min_int = int(time[1])
                    ist_datetime_obj = datetime(int(date_fields[0]), int(date_fields[1]), int(date_fields[2]),
                                       hour_int, min_int, 0)

            return ist_datetime_obj

        except Exception as e:
            print (e)