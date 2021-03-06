import json


class JSONFile:

    @staticmethod
    def get_swaps(filename="request_list.json"):
        try:
            json_file = json.load(open(filename, "r", encoding="UTF-8"))
        except FileNotFoundError as e:
            return e
        except json.decoder.JSONDecodeError as e:
            return e

        return json_file['requests']['swap']

    @staticmethod
    def read_json(filename):
        try:
            json_file = json.load(open(filename, "r", encoding="UTF-8"))
        except FileNotFoundError as e:
            return e
        except json.decoder.JSONDecodeError as e:
            return e

        return json_file

    @staticmethod
    def add_request(request_type, request, filename="request_list.json"):
        json_file = JSONFile.read_json(filename)
        if isinstance(json_file, Exception):
            print("Ошибка: "+json_file.__str__())
        else:
            json_file['request'][request_type].append(request)

        JSONFile.set_json_data(json_file, filename)

    @staticmethod
    def delete_request(hash_code, filename="request_list.json"):
        json_file = JSONFile.read_json(filename)
        if isinstance(json_file, Exception):
            print("Ошибка: "+json_file.__str__())
            return

        for request_type in json_file["request"]:
            index = 0
            max_index_value = len(json_file['request'][request_type])
            while True:

                if json_file['request'][request_type][index].split()[2] == hash_code:

                    del json_file['request'][request_type][index]
                    break

                index += 1
                if index == max_index_value:
                    break

            # Фиксируем преждевременный выход из цикла
            if index != max_index_value:
                break

        JSONFile.set_json_data(json_file, filename)

    @staticmethod
    def get_persons(filename):
        return json.load(open(filename, "r", encoding="UTF-8"))["Persons"]

    @staticmethod
    def set_json_data(data, filename):
        f = open(filename, "w", encoding="UTF-8")
        f.write(json.dumps(data, ensure_ascii=False))
        f.close()

    @staticmethod
    def get_vkid_by_id(idd, group_file_name):
        data = JSONFile.read_json(group_file_name)
        return data["Persons"][str(idd)]['vkid']

    @staticmethod
    def get_id_by_vkid(vkid, group_file_name):
        data = JSONFile.read_json(group_file_name)
        for index in data['Persons']:
            if data["Persons"][index]['vkid'] == str(vkid):
                return index

    @staticmethod
    def get_name_by_vkid(vkid, group_file_name):
        data = JSONFile.read_json(group_file_name)
        for index in data['Persons']:
            if data["Persons"][index]['vkid'] == str(vkid):
                return data["Persons"][index]['name']

    @staticmethod
    def read_keyboard(filename, directory="keyboards/"):
        return open(directory+filename, "r", encoding="UTF-8").read()

    @staticmethod
    def set_setting(setting_name, value, user_id, group_file_name):
        data = JSONFile.read_json(group_file_name)
        for index in data['Persons']:
            if index == str(user_id):
                data['Persons'][index]['settings'][setting_name] = value
        JSONFile.set_json_data(data, group_file_name)
