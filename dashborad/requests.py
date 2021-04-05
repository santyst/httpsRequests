#prueba de commit

from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from flask_httpauth import HTTPTokenAuth
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

app = Flask(__name__)
api = Api(app)
app.config['SECRET_KEY'] = 'top secret!'
token_serializer = Serializer(app.config['SECRET_KEY'], expires_in=3600)
auth = HTTPTokenAuth('Bearer')

API = '/api/v1/'

users= ['santiago']

for user in users:
    token = token_serializer.dumps({'username': user}).decode('utf-8')
    print('*** token for {}: {}\n'.format(user, token))


''' Jsons de respuesta '''

#Device screen brightness and LED set interface
#GetScreen Brightness
 
Brightness = {
    'getscreenluminancevalue':60,
    'getledenable': 1
}

#GetDevice Volume

Volume = {
    'getvolumevalue': 1
}

#GetUserList Of Device

UserList = [
    {'selectalluserlist': {
     'default_id': 1,
     'admin': 2
    }
    }
]

# GetDevice standby config time

Standby_time = {
    'getfrdstandbytime': 0
}

# GetAuto Maintenance

AutoMaintenance = {
    'getautomaintaintype':1,
    'getautomaintainday':3,
    'getautomaintainweek':3,
    'getautomaintainhour':0,
    'getautomaintainmin':0
}

# GetSnapshot Info

Snapshot = {
  'getrecordsavetime': 72,
  'getsaverecordenable': 1,
  'getsavejpegenable': 1
}

# GetTemperature Measurement Types

TempMeasure = {
    'gettemperaturetype': 0
}

# GetGallerySize

Gallerysize = {
    'getpiclibtotalnum':0 
}

# get Temperature measurement set

GetTemp = {
    'gettempdetectionen': 1,
    'gettempalarmvalue': 38.2,
    'gettemperature': 0.0
}

# Restore factory set

Restore = {
    'restoretodefault': 1
}

# Obtain system maintenance

MainSys = {
    'getonlineupdatetype':1,
    'getonlineupdateday':2, 
    'getonlineupdateweek':2,
    'getonlineupdatestatus': 0
}

# Get face recognition set config

FaceRecog = {
    'getstrangerpassen':1,
    'getmaskdetectionen':0,
    'getrelaytime':200,
    'getrelaydir':0,
    'getlivenesscheck':0,
    'getthermalmapenable':1
}

# Get smtp set info 

SmtpConfig = {
    'getsmtpserver':1,
    'getsmtpuser':1,
    'getsmtppasswd':1,
    'getsmtpreceiver':1,
    'getsmtpreceiver1':1,
    'getsmtpreceiver2':1,
    'getsmtpsender':1,
    'getsmtptheme':1,
    'getsmtpanoen':1,
    'getsmtpfileen':1,
    'getsmtpport':1,
    'getsmtpenctype':1,
    'getsmtpinterval':1,
    'getsmtphealthen':1,
    'getsmtphealthinterval':1,
    'getsmtpen':1,
    'getsmtpeableautosend':1,
    'getsmtpautosendinterval':1,
}

# Get mqtt settting info

Mqtt = {
    'getmqttenable':1,
    'getmqttport':1,
    'getmqttretain':1,
    'getmqttpqos':1,
    'setmqttpqos':1,
    'getmqttusername':1,
    'getmqttpasswd':1,
    'getmqttserver':1,
    'getmqtttopic2pulish':1,
    'getmqtttopic2subscribe':1,
    'getmqttstatus':1
}

# Get date setting info

DateSetting = {
    'getsystemtimeyear':2021,
    'getsystemtimemonth':4,
    'getsystemtimeday':5,
    'getsystemtimehour':8,
    'getsystemtimeminutes':41,
    'getsystemtimeseconds':30,
    'getntpserver':'time.nist.gov',
    'getntpport':123,
    'getntinterval':10,
    'getntpdateformat':0,
    'getntpdateseparator':0,
    'getntptimeformat':0,
    'getntptimezone':14,
    'getntpcontrol':0,
    'getntpcontrol':0
}

# get daylight time

DaylightTime = {
    'getsummertimetmisdst':0,
    'getsummertimetmisdst':0,
    'getsummertimetmoffset':1,
    'getsummertimeoffsetflag':0,
    'getsummertimestartyear':2020,
    'getsummertimestartmon':2,
    'getsummertimestartweektype':0,
    'getsummertimestartweekday':0,
    'getsummertimestartmday':1,
    'getsummertimestarthour':3,
    'getsummertimestartmin':3,
    'getsummertimeendyear':2020,
    'getsummertimeendmon':10,
    'getsummertimeendweektype':0,
    'getsummertimeendweekday':0,
    'getsummertimeendmday':1,
    'getsummertimeendhour':3,
    'getsummertimeendmin':3,
    'getntpcontrol':0
}

# Get date info

DateGet = {
    'getsystemtimeyear':2021,
    'getsystemtimemonth':4,
    'getsystemtimeday':5,
    'getsystemtimehour':9,
    'getsystemtimeminutes':29,
    'getsystemtimeseconds':40,
    'getntpserveer':'',
    'getntpport':123,
    'getntinterval':10,
    'getdateformat':'',
    'getntptimezone':14,
    'getntpcontrol':0,
    'getsummertimetmisdst':0
}


Post_Success={
    'Status': 'SUCCESS',
    'Msg':'El llamado post funciona.'
}

tokens = {
    "secret-token-1": "john",
    "secret-token-2": "susan"
}

@auth.verify_token
def verify_token(token):
    try:
        data = token_serializer.loads(token)
    except:  # noqa: E722
        return False
    if 'username' in data:
        return data['username']

""" @auth.verify_password
def authenticate(username, password):
	if username and password:
		if username == 'admin' and password == '12345':
			return True
		else:
			return False
	return False """
    
@app.route('/api/v1/data/all', methods=['GET'])
@auth.login_required

def api_all():
    return jsonify(Data)

@app.route('/api/v1/send', methods=['POST'])
@auth.login_required

def post_json():
    request_data = request.get_json()

    language = request_data['language']
    framework = request_data['framework']

    # python_version = request_data['version_info']['python']

    # an index is needed because of the array
    # example = request_data['examples'][0]

    # boolean_test = request_data['boolean_test']

    return jsonify(Post_Success)


'''              Llamados para tabletas.              '''

#Device screen brightness and LED set interface

#GetScreen Brightness

@app.route('{}get-device-brightness'.format(API), methods=['GET'])
@auth.login_required

def api_device_brightness():
    return jsonify(Brightness)

#SetScreen Brightness

@app.route('{}set-device-brightness'.format(API), methods=['POST'])
@auth.login_required

def set_device_brightness():

    request_brightness = request.get_json()

    setscreenluminancevalue = request_brightness['setscreenluminancevalue']
    setledenable = request_brightness['setledenable']

    return jsonify({'setscreenluminancevalue': setscreenluminancevalue, 'setledenable': setledenable, 'status': 'OK'})


# Volume set interface

#GetDevice Volume

@app.route('{}get-device-volume'.format(API), methods=['GET'])
@auth.login_required

def api_device_volume():
    return jsonify(Volume)

#SetDevice Volume

@app.route('{}set-device-volume'.format(API), methods=['POST'])
@auth.login_required

def set_device_volume():

    request_volume = request.get_json()

    setvolumevalue = request_volume['setvolumevalue']

    return jsonify({'setvolumevalue': setvolumevalue, 'status': 'OK'})


# Device Security Configuration Interface

#GetUserList Of Device

@app.route('{}get-device-userlist'.format(API), methods=['GET'])
@auth.login_required

def api_device_userlist():

    return jsonify(UserList)

#AddDevice User

@app.route('{}set-device-user'.format(API), methods=['POST'])
@auth.login_required

def set_device_user():

    request_user = request.get_json()

    addusername = request_user['addusername']
    addpassword = request_user['addpassword']
    addpasswordstrength = request_user['addpasswordstrength']
    addulocalconfigdatabit = request_user['addulocalconfigdatabit']
    adduremoteconfigdatabit = request_user['adduremoteconfigdatabit']
    adducameraconfigdatabit = request_user['adducameraconfigdatabit']
    adduserlevel = request_user['adduserlevel']

    return jsonify({'status': 'OK'})


# Standby set interface

#GetDevice StandbyConfig Time

@app.route('{}get-device-standby-time'.format(API), methods=['GET'])
@auth.login_required

def api_device_standby_time():

    return jsonify(Standby_time)

#AddDevice User

@app.route('{}set-device-standby-time'.format(API), methods=['POST'])
@auth.login_required

def set_device_standby_time():

    request_standbytime = request.get_json()

    setfrdstandbytime = request_standbytime['setfrdstandbytime']

    return jsonify({'status': 'OK'})


# Automatic maintenance interface

# GetAuto Maintenance

@app.route('{}get-device-automaintenance'.format(API), methods=['GET'])
@auth.login_required

def api_device_automaintenance():

    return jsonify(AutoMaintenance)

# SetAuto Maintenance

@app.route('{}set-device-automaintenance'.format(API), methods=['POST'])
@auth.login_required

def set_device_automaintenance():

    request_automaintenance = request.get_json()

    setautomaintaintype = request_automaintenance['setautomaintaintype']
    setautomaintainday = request_automaintenance['setautomaintainday']
    setautomaintainweek = request_automaintenance['setautomaintainweek']
    setautomaintainhour = request_automaintenance['setautomaintainhour']
    setautomaintainmin = request_automaintenance['setautomaintainmin']

    return jsonify({'status': 'OK'})


# Snapshot set interface

# GetSnapshot Info

@app.route('{}get-device-snapshot'.format(API), methods=['GET'])
@auth.login_required

def api_device_snapshot():

    return jsonify(Snapshot)

# SetSnapshot Info

@app.route('{}set-device-snapshot'.format(API), methods=['POST'])
@auth.login_required

def set_device_snapshot():

    request_snapshot = request.get_json()

    setrecordsavetime = request_snapshot['setrecordsavetime']
    setsaverecordenable = request_snapshot['setsaverecordenable']
    setsavejpegenable = request_snapshot['setsavejpegenable']

    return jsonify({'status': 'OK'})


#Display Configuration interface

# GetTemperature Measurement Types

@app.route('{}get-device-temptype'.format(API), methods=['GET'])
@auth.login_required

def api_device_temptype():

    return jsonify(TempMeasure)

# SetDisplay config

@app.route('{}set-device-displayconfig'.format(API), methods=['POST'])
@auth.login_required

def set_device_displayconf():

    request_displayconf = request.get_json()

    setdevname = request_displayconf['setdevname']
    setlanguage = request_displayconf['setlanguage']
    setrecyclerecord = request_displayconf['setrecyclerecord']
    setdrvid = request_displayconf['setdrvid']
    setoutdevice = request_displayconf['setoutdevice']
    setvideomode = request_displayconf['setvideomode']
    settemperatureType = request_displayconf['settemperatureType']


    return jsonify({'status': 'OK'})


# Visitor query interface

# GetGallerySize

@app.route('{}get-device-gallerysize'.format(API), methods=['GET'])
@auth.login_required

def api_device_gallerysize():

    return jsonify(Gallerysize)

# GetGallery all info

@app.route('{}set-device-galleryinfo'.format(API), methods=['POST'])
@auth.login_required

def set_device_galleryinfo():

    request_galleryinfo = request.get_json()

    getpiclibinfoall = request_galleryinfo['getpiclibinfoall']


    return jsonify({'status': 'OK'})


# Temperature measurement set interface

# get Temperature measurement set

@app.route('{}get-device-gettemp'.format(API), methods=['GET'])
@auth.login_required

def api_device_gettemp():

    return jsonify(GetTemp)

# Set temperature measurement Config

@app.route('{}set-device-tempmeasure'.format(API), methods=['POST'])
@auth.login_required

def set_device_tempmeasure():

    request_tempmeasure = request.get_json()

    settempdetectionen = request_tempmeasure['settempdetectionen']
    settempalarmvalue = request_tempmeasure['settempalarmvalue']
    settemperature = request_tempmeasure['settemperature']

    return jsonify({'status': 'OK'})


# System maintenance interface

# Device restart

@app.route('{}set-device-restart'.format(API), methods=['POST'])
@auth.login_required

def set_device_restart():

    request_restart = request.get_json()

    setuser = request_restart['setuser']
    setsystemreboot = request_restart['setsystemreboot']

    return jsonify({'status': 'OK'})

# Restore factory set

@app.route('{}get-device-restore-factory'.format(API), methods=['GET'])
@auth.login_required

def api_device_restore():

    return jsonify(Restore)

# Set auto online update

@app.route('{}set-device-auto-online'.format(API), methods=['POST'])
@auth.login_required

def set_device_autoonile():

    request_autoonline = request.get_json()

    setonlineupdatetype = request_autoonline['setonlineupdatetype']
    setonlineupdateday = request_autoonline['setonlineupdateday']
    setonlineupdateweek = request_autoonline['setonlineupdateweek']

    return jsonify({'status': 'OK'})

# Obtain system maintenance

@app.route('{}get-device-system-maintenance'.format(API), methods=['GET'])
@auth.login_required

def api_device_sysmaintenance():

    return jsonify(MainSys)


#  Face recognition interface 

# Get Face recognition set config

@app.route('{}get-device-face-recognition'.format(API), methods=['GET'])
@auth.login_required

def api_device_Facerecog():

    return jsonify(FaceRecog)

# Set face recognition set config

@app.route('{}set-device-face-recognition'.format(API), methods=['POST'])
@auth.login_required

def set_device_facerecog():

    request_facerecog = request.get_json()

    setstrangerpassen = request_facerecog['setstrangerpassen']
    setmaskdetectionen = request_facerecog['setmaskdetectionen']
    setrelaytime = request_facerecog['setrelaytime']
    setrelaydir = request_facerecog['setrelaydir']
    setlivenesscheck = request_facerecog['setlivenesscheck']
    setthermalmapenable = request_facerecog['setthermalmapenable']


    return jsonify({'status': 'OK'})


# SMTP protocol interface

# get smtp config

@app.route('{}get-device-smtp'.format(API), methods=['GET'])
@auth.login_required

def api_device_smtpget():

    return jsonify(SmtpConfig)

# set smtp config

@app.route('{}set-device-smtp'.format(API), methods=['POST'])
@auth.login_required

def set_device_smtpset():

    request_smtpset = request.get_json()

    setuser = request_smtpset['setuser']
    setsmtpserver = request_smtpset['setsmtpserver']
    setsmtpuser = request_smtpset['setsmtpuser']
    setsmtppasswd = request_smtpset['setsmtppasswd']
    setsmtpreceiver = request_smtpset['setsmtpreceiver']
    setsmtpreceiver1 = request_smtpset['setsmtpreceiver1']
    setsmtpreceiver2 = request_smtpset['setsmtpreceiver2']
    setsmtpsender = request_smtpset['setsmtpsender']
    setsmtptheme = request_smtpset['setsmtptheme']
    setsmtpen = request_smtpset['setsmtpen']
    setsmtpanoen = request_smtpset['setsmtpanoen']
    setsmtpfileen = request_smtpset['setsmtpfileen']
    setsmtpport = request_smtpset['setsmtpport']
    setsmtpenctype = request_smtpset['setsmtpenctype']
    setsmtpinterval = request_smtpset['setsmtpinterval']
    setsmtphealthen = request_smtpset['setsmtphealthen']
    setsmtphealthinterval = request_smtpset['setsmtphealthinterval']


    return jsonify({'status': 'OK'})

# MQTT protocol interface

# Get mqtt setting info

@app.route('{}get-device-mqtt'.format(API), methods=['GET'])
@auth.login_required

def api_device_mqtt():

    return jsonify(Mqtt)

# Set mqtt setting info

@app.route('{}set-device-mqtt'.format(API), methods=['POST'])
@auth.login_required

def set_device_mqttset():

    request_mqttset = request.get_json()

    setmqttenable = request_mqttset['setmqttenable']
    setmqttport = request_mqttset['setmqttport']
    setmqttretain = request_mqttset['setmqttretain']
    setmqttpqos = request_mqttset['setmqttpqos']
    setmqttpqos = request_mqttset['setmqttpqos']
    setmqttusername = request_mqttset['setmqttusername']
    setmqttpasswd = request_mqttset['setmqttpasswd']
    setmqttserver = request_mqttset['setmqttserver']
    setmqtttopic2pulish = request_mqttset['setmqtttopic2pulish']
    setmqtttopic2subscribe = request_mqttset['setmqtttopic2subscribe']
    setheartbeat = request_mqttset['setheartbeat']


    return jsonify({'status': 'OK'})


# Network inrterface

# Set network info 

@app.route('{}set-device-network'.format(API), methods=['POST'])
@auth.login_required

def set_device_network():

    request_network = request.get_json()

    netip = request_network['netip']
    netmask = request_network['netmask']
    gateway = request_network['gateway']
    dns1 = request_network['dns1']
    dns2 = request_network['dns2']
    mac = request_network['mac']
    dhcpenable = request_network['dhcpenable']
    dnsautoenalbe = request_network['dnsautoenalbe']


    return jsonify({'status': 'OK'})


# Query interface

# Query travel records

@app.route('{}set-device-query-travel-records'.format(API), methods=['POST'])
@auth.login_required

def set_device_query_travel():

    request_querytravel = request.get_json()

    end_time = request_querytravel['end_time']
    start_time = request_querytravel['start_time']
    from_index = request_querytravel['from_index']
    to_index = request_querytravel['to_index']
    query_by = request_querytravel['query_by']


    return jsonify({'status': 'OK'})

# querying the recording through temp

@app.route('{}set-device-query-temp'.format(API), methods=['POST'])
@auth.login_required

def set_device_query_temp():

    request_querytemp = request.get_json()

    min_temp = request_querytemp['min_temp']
    max_temp = request_querytemp['max_temp']
    from_index = request_querytemp['from_index']
    to_index = request_querytemp['to_index']
    query_by = request_querytemp['query_by']


    return jsonify({'status': 'OK'})


# System setting interface

# Get date setting info 

@app.route('{}get-device-date-setting'.format(API), methods=['GET'])
@auth.login_required

def api_device_date_setting():

    return jsonify(DateSetting)

# Get daylight time 

@app.route('{}get-device-daylight-time'.format(API), methods=['GET'])
@auth.login_required

def api_device_daylight_time():

    return jsonify(DaylightTime)

# Set daylight time

@app.route('{}set-device-daylight-time'.format(API), methods=['POST'])
@auth.login_required

def set_device_daylight_time():

    request_daylight = request.get_json()

    setsummertimetmisdst = request_daylight['setsummertimetmisdst']
    setsummertimetmtype = request_daylight['setsummertimetmtype']
    setsummertimetmoffset = request_daylight['setsummertimetmoffset']
    setsummertimeoffsetflag = request_daylight['setsummertimeoffsetflag']
    setsummertimestartyear = request_daylight['setsummertimestartyear']
    setsummertimestartmon = request_daylight['setsummertimestartmon']
    setsummertimestartweektype = request_daylight['setsummertimestartweektype']
    setsummertimestartweekday = request_daylight['setsummertimestartweekday']
    setsummertimestartmday = request_daylight['setsummertimestartmday']
    setsummertimestarthour = request_daylight['setsummertimestarthour']
    setsummertimestartmin = request_daylight['setsummertimestartmin']
    setsummertimeendyear = request_daylight['setsummertimeendyear']
    setsummertimeendmon = request_daylight['setsummertimeendmon']
    setsummertimeendweektype = request_daylight['setsummertimeendweektype']
    setsummertimeendweekday = request_daylight['setsummertimeendweekday']
    setsummertimeendmday = request_daylight['setsummertimeendmday']
    setsummertimeendhour = request_daylight['setsummertimeendhour']
    setsummertimeendmin = request_daylight['setsummertimeendmin']

    return jsonify({'status': 'OK'})

# Get settings

@app.route('{}get-device-settings'.format(API), methods=['POST'])
@auth.login_required

def set_device_settings():

    request_settings = request.get_json()

    setloginpro = request_settings['setloginpro']
    setlogin = request_settings['setlogin']
    setloginip = request_settings['setloginip']

    return jsonify({'status': 'OK'})

# set date info

@app.route('{}set-device-date-info'.format(API), methods=['POST'])
@auth.login_required

def set_device_dateset():

    request_dateset = request.get_json()

    setuser = request_dateset['setuser']
    setsystemtimeyear = request_dateset['setsystemtimeyear']
    setsystemtimemonth = request_dateset['setsystemtimemonth']
    setsystemtimeday = request_dateset['setsystemtimeday']
    setsystemtimehour = request_dateset['setsystemtimehour']
    setsystemtimeminutes = request_dateset['setsystemtimeminutes']
    setsystemtimeseconds = request_dateset['setsystemtimeseconds']
    setntpserver = request_dateset['setntpserver']
    setntptimezone = request_dateset['setntptimezone']
    setntpcontrol = request_dateset['setntpcontrol']
    setntinterval = request_dateset['setntinterval']
    setntpport = request_dateset['setntpport']

    return jsonify({'status': 'OK'})

# get date info

@app.route('{}get-device-date-info'.format(API), methods=['GET'])
@auth.login_required

def api_device_dateget():

    return jsonify(DateGet)


# User interface

# Login

@app.route('{}device-login'.format(API), methods=['POST'])
@auth.login_required

def set_device_login():

    request_login = request.get_json()

    setloginpro = request_login['setloginpro']
    setlogin = request_login['setlogin']
    setloginip = request_login['setloginip']

    return jsonify({'status': 'OK'})

#logout

@app.route('{}device-logout'.format(API), methods=['POST'])
@auth.login_required

def set_device_logout():

    request_logout = request.get_json()

    setlogout = request_logout['setlogout']

    return jsonify({'status': 'OK'})


# Get travel records 

@app.route('{}get-device-travel-records'.format(API), methods=['POST'])
@auth.login_required

def set_device_travel_records():

    request_travel_records = request.get_json()

    start_time = request_travel_records['start_time']
    end_time = request_travel_records['end_time']
    query_by = request_travel_records['query_by']
    from_index = request_travel_records['from_index']
    to_index = request_travel_records['to_index']

    return jsonify({'status': 'OK'})


# Get temp records

@app.route('{}get-device-temp-records'.format(API), methods=['POST'])
@auth.login_required

def set_device_temp_records():

    request_temp_records = request.get_json()

    min_temp = request_temp_records['min_temp']
    max_temp = request_temp_records['max_temp']
    from_index = request_temp_records['from_index']
    to_index = request_temp_records['to_index']
    query_by = request_temp_records['query_by']

    return jsonify({'status': 'OK'})


# Get passer image

@app.route('{}get-device-passer-image'.format(API), methods=['POST'])
@auth.login_required

def set_device_passer_image():

    request_passer_image = request.get_json()

    pic_id = request_passer_image['pic_id']
    pic_index = request_passer_image['pic_index']

    return jsonify({'status': 'OK'})

app.run()