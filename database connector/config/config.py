import os
"""_____________________________________________________________________
    Configuration file for the "Database" module
    Last modification: 31.03.2021
    Author of the modification: Golyshev Ilya
    Email: ilia.golyshev@t-systems.com
   _____________________________________________________________________"""
__version__ = '1.0.0'

"""_____________________________________________________________________
    Parameters required for configuring paths in the module
        1. Full path to the directory from which the entire module is
           launched
   _____________________________________________________________________"""
"""1"""
work_path = "/home/acs_system"

"""_____________________________________________________________________
    Parameters for connecting to the database
      1. the name of the database
      2. base ip address encoded in base64
      3. the user through which base64-encoded access is performed
      4. the password is encoded in base64
      5. date format
   _____________________________________________________________________"""
"""1"""
db_name = "database_acs"
"""2"""
host_db = "MTAuMjE2LjAuMTk3"
"""3"""
user_db = "dXNlcl9hY3M="
"""4"""
password_db = "dXNlcl9hY3M="
"""5"""
date_format = "%d.%m.%Y %H:%M:%S"

"""_____________________________________________________________________
    Parameters for configuration logger
      1. format output logger
      2. format output exception logger
      3. name of the folder where the logs are located
      4. name of the log file
      5. Period for creating a new log file
      6. The number of backup files with the logs
   _____________________________________________________________________"""
"""1"""
format_logger = '%(asctime)s - %(filename)-30s - %(levelname)-8s - %(message)s'
"""2"""
str_log_exception = 'EXCEPTION IN ({}, LINE {} "{}"): {}'
"""3"""
dir_log = 'logs'
"""4"""
name_log_file = 'removal_equipment'
"""5"""
period_create_new_log_file = 'midnight'
"""6"""
log_backup_count = 14


"""_____________________________________________________________________
    Parameters for configuring flask API
      1. server host
      2. server ip
      2. server port
   _____________________________________________________________________"""
"""1"""
host = "0.0.0.0"
"""2"""
ip_address = "10.216.0.197"
"""3"""
port = 5050


"""_____________________________________________________________________
    Parameters for configuring word template
      1. name of the template for taking out equipment
      2. name of the directory where the templates are located
      3. name of the directory where the completed templates are saved
      4. columns names in word template
      5. the name of the folder in which the templates of documents on 
         the removal of equipment are located
      6. the name of the folder in which the templates of documents on 
         the removal of chairs are located
      7. dictionary of city comparisons and templates
      8. dictionary of comparisons of legal entities ' names in English 
         and Russian 
   _____________________________________________________________________"""
"""1"""
name_word_template_technic = {
    "Санкт-Петербург": "Шаблон для выноса техники СПб.docx",
    "Воронеж": "Служебная записка Воронеж.docx"
}
"""2"""
folder_to_template = "word_template"
"""3"""
folder_with_documents = "result_docs"
"""4"""
word_columns = ['Сотрудник, на кого оформлена техника',
                'Модель', 'Инвентарный номер', 'Табельный номер']
"""5"""
folder_removal_technic = 'technic'
"""6"""
folder_removal_chair = 'chair'
"""7"""
name_word_template_chair = {
    "Санкт-Петербург": "Шаблон для выноса кресла СПб.docx",
    "Воронеж": "Служебная записка Воронеж.docx"
}
"""8"""
dict_legal_entities = {
    'DT IT RUS': 'OOO «ДТ АйТи РУС»',
    'T-Systems RUS': 'ООО «Т-Системс РУС»',
    'T-Systems CIS': 'ООО «Т-Системс СиАйЭс»'
}


"""_____________________________________________________________________
    Parameters required to set up a connection to the SVN
        1. Username for authorization in SVN encoded in base64
        2. Password for authorization in SVN encoded in base64
        3. URL for getting files with images of floors encoded in base64
        4. Name of the local folder for storing floor images
   _____________________________________________________________________"""
"""1"""
username_SVN = "aWdvbHlzaGU="
"""2"""
password_SVN = "VmZ2ZjEwMDQ5OQ=="
"""3"""
url_to_docs = "aHR0cHM6Ly9zdWJ2ZXJzaW9uLnQtc3lzdGVtcy5ydS9zdm4vQUlfcHJvamVjdHMvRmFjaWxpdHkvRGF0YV9mb3JfbW9kdWxlcy9yZW1vdmFsX2VxdWlwbWVudA=="
"""4"""
dir_for_url_to_docs = "result_docs"

"""_____________________________________________________________________
    Parameters required for connecting to Exchange
      1. name of the contact group that lists are sent to
      2. email login used to connect to exchange(base64 encoded)
      3. email password used to connect to exchange(base64 encoded)
      4. email login of the FMB account that connects to 
         exchange(base64 encoded)
      5. the server through which exchange connects to mail
      6. certificate for server access
   _____________________________________________________________________"""
"""1"""
dl_spb = "removal_equipment_spb"
"""1"""
dl_vrn = "removal_equipment_vrn"
"""2"""
username_fmb = "aWxpYS5nb2x5c2hldkB0LXN5c3RlbXMuY29t"
"""3"""
password_fmb = "U2VyZzMwMDRfXzE0"
"""4"""
fmb = "UlVfZXF1aXBtZW50QHRlbGVrb20uY29t"
"""5"""
server = "he105150.emea1.cds.t-internal.com"
"""6"""
certificate = os.path.join(work_path, 'email_certificate/certif.cer')


"""_____________________________________________________________________
    Parameters required for email template
      1. Email template folder name
      2. Email template file name
      3. Email subject for managers
      4. dictionary of city maps and mail templates for users
      5. the name of the mail template for the manager after successfully
         sending the notification to the user
   _____________________________________________________________________"""
"""1"""
email_template_folder = "template"
"""2"""
dict_manager_template = {
    "Воронеж": "template-manager-vrn.html",
    "Санкт-Петербург": "template-manager-spb.html"
}
"""3"""
email_subject = "Вынос оборудования"
"""4"""
dict_user_template = {
    "Воронеж": "template-user-vrn.html",
    "Санкт-Петербург": "template-user-spb.html"
}
"""5"""
email_template_response = "template-manager-response.html"
"""6"""
dict_template_repeat_chair_request = {
    "Воронеж": "template-manager-vrn-repeat.html",
    "Санкт-Петербург": "template-manager-spb-repeat.html"
}

"""_____________________________________________________________________
    Parameters required for qrcode
      1. name of the folder where the qr code is saved
      2. file name with qr code
   _____________________________________________________________________"""
"""1"""
folder_for_qrcode = 'qrcode'
"""2"""
qr_name = 'qrcode.jpg'

"""_____________________________________________________________________
    Parameters required for issuing equipment that doesn't belong to 
    anyone
    
   _____________________________________________________________________"""
list_warehouse_users = [
    'nikolai.zinchenko@t-systems.com',
    'sergei.gerasimov@t-systems.com',
    'vladimir.zakharov@telekom.com',
    'ilia.sokolov@t-systems.com',
    'sergey.belov@t-systems.com',
    'yulia.afanasieva@t-systems.com',
    'mikhail.klychev@t-systems.com',
    'maksim.korobov@telekom.com',
    'evgenii.gaidar@telekom.com',
    'd.zavyalov@t-systems.com'
]