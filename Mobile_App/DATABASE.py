
import gspread
from oauth2client.service_account import ServiceAccountCredentials



class DataBase:

    def __init__(self, scope, json, sheet_name):
        self.__scope = scope
        self.__creds = ServiceAccountCredentials.from_json_keyfile_name(json, scope)  # Gets credentials from a json file in same directory
        self.__client = gspread.authorize(self.__creds)
        self.__sheet = self.__client.open(sheet_name).sheet1
        self.__data = self.__sheet.get_all_records()

    #-----------------GET FUNCTIONS-------------------#

    def get_OnOff(self):
        return self.__sheet.cell(2, 2).value


    def get_Central(self):
        return self.__sheet.cell(3, 2).value


    def get_StartSignal(self):
        return self.__sheet.cell(4, 2).value


    def get_Sensor_on(self):
        return self.__sheet.cell(6,2).value


    def get_MOTION_DET(self):
        return self.__sheet.cell(7, 2).value


    def get_CameraOn(self):
        return self.__sheet.cell(8,2).value


    def get_CPU_TEMP(self):
        return self.__sheet.cell(10, 2).value


    def get_CPU_USAGE(self):
        return self.__sheet.cell(11, 2).value


    def get_HUS_TEMP(self):
        return self.__sheet.cell(12, 2).value

    #-----------------UPDATE FUNCTIONS----------------#

    def update_OnOff(self, value):
        self.__sheet.update_cell(2, 2, value)


    def update_Central(self, value):
        self.__sheet.update_cell(3, 2, value)


    def update_Sensor_on(self,value):
        self.__sheet.update_cell(7,2, value)


    def update_MOTION_DET(self, value):
        self.__sheet.update_cell(7, 2, value)


    def update_CameraOn(self, value):
        self.__sheet.update_cell(8, 2, value)


    def update_CPU_TEMP(self, value):
        self.__sheet.update_cell(10, 2, value)


    def update_CPU_USAGE(self, value):
        self.__sheet.update_cell(11, 2, value)


    def update_HUS_TEMP(self, value):
        self.__sheet.update_cell(12, 2, value)


    #--------------------Start System----------------#


    def getStartSignal(self):
        return self.__sheet.cell(4,2).value


    def update_StartSignal(self, value):
        self.__sheet.update_cell(4, 2, value)




