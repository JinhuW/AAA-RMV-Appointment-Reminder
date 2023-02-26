import requests
import json
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from bs4 import BeautifulSoup
from datetime import datetime
from dotenv import load_dotenv

import os

load_dotenv()  # Load environment variables from .env file

ma_aaa_rmv = [
  {
    "id": "3802389",
    "name": "AAA Acton Branch Office, 342 Great Road, Acton, MA 01720 (978) 266-1000",
    "geo": "42.5019318, -71.4207243"
  },
  {
    "id": "4900998",
    "name": "AAA Auburn  Branch Office, 711 Southbridge Street, Auburn, MA 01501 (508) 832-0200",
    "geo": "42.18262, -71.85862"
  },
  {
    "id": "3697037",
    "name": "AAA Boston Branch Office, 141 Congress Street, Boston MA 02110 (617) 443-9300",
    "geo": "42.3559987, -71.0561823"
  },
  {
    "id": "3755041",
    "name": "AAA Burlington Branch Office, 34 Cambridge Street, Suite 140 Burlington, MA 01803 (781) 272-3272",
    "geo": "42.4845874, -71.18755999999999"
  },
  {
    "id": "3755052",
    "name": "AAA Fairhaven Branch Office, 32 Fairhaven Commons Way, Fairhaven, MA 02719 (508) 997-7811",
    "geo": "41.6444428, -70.88748939999999"
  },
  {
    "id": "3755129",
    "name": "AAA Framingham Branch Office, 653 Worcester Road, Framingham, MA 01701 (508) 875-2000",
    "geo": "42.29875, -71.42327999999999"
  },
  {
    "id": "3755133",
    "name": "AAA Franklin Branch Office, 85 Franklin Village Drive #14, Franklin, MA 02038 (508) 528-9300 *At our new location across the plaza!*",
    "geo": "42.0885346, -71.4216939"
  },
  {
    "id": "5213038",
    "name": "AAA Greenfield Branch Office, 91 Main St., Greenfield, MA 01301 (413) 785-1381",
    "geo": "42.5873581, -72.6057146"
  },
  {
    "id": "5213046",
    "name": "AAA Hadley Branch Office, 458 Russell Street, Hadley, MA 01035 (413) 785-1381",
    "geo": "42.3655104, -72.5364269"
  },
  {
    "id": "3755140",
    "name": "AAA Haverhill Branch Office, 90 Kenoza Avenue, Haverhill, MA 01830 (978) 373-3611",
    "geo": "42.7831866, -71.074522"
  },
  {
    "id": "3755145",
    "name": "AAA Leominster Branch Office, 36 Watertower Plaza #7, Leominster, MA 01453 (978) 537-4000",
    "geo": "42.54258000000001, -71.75675319999999"
  },
  {
    "id": "3755150",
    "name": "AAA Lowell Branch Office, 585 Pawtucket Boulevard, Lowell, MA 01854 (978) 937-3061",
    "geo": "42.64118, -71.35524"
  },
  {
    "id": "3701015",
    "name": "AAA Marlborough Branch Office, 197 Boston Post Road West/Route 20 West, Marlborough, MA 01752 (508) 303-2400",
    "geo": "42.3403895, -71.59062829999999"
  },
  {
    "id": "3755165",
    "name": "AAA Newburyport Branch Office, 45 Storey Avenue, Newburyport, MA 01950 (978) 499-4200",
    "geo": "42.8195713, -70.907018"
  },
  {
    "id": "3755170",
    "name": "AAA Newton Branch Office, 165 Needham Street, Unit N303 Newton, MA 02461 (617) 332-9900",
    "geo": "42.3120678, -71.2132491"
  },
  {
    "id": "3755177",
    "name": "AAA North Andover Branch Office, 75 Turnpike Street, North Andover, MA 01845 (978) 681-9200",
    "geo": "42.6771186, -71.1320899"
  },
  {
    "id": "3755185",
    "name": "AAA North Reading Branch Office, 72 Main Street, North Reading, MA 01864 (978) 357-7120",
    "geo": "42.57013600000001, -71.1120363"
  },
  {
    "id": "3755189",
    "name": "AAA Peabody Branch Office, 300 Andover Street, Peabody, MA 01960 (978) 535-5300",
    "geo": "42.5488882, -70.95667089999999"
  },
  {
    "id": "3755197",
    "name": "AAA Pittsfield  Branch Office, 660 Merrill Road, Pittsfield, MA 01201 (413) 445-5635",
    "geo": "42.4658922, -73.2030267"
  },
  {
    "id": "3755201",
    "name": "AAA Plymouth Branch Office, 29 Home Depot Drive, Plymouth, MA 02360 (508) 747-6100",
    "geo": "41.9340863, -70.659902"
  },
  {
    "id": "3755204",
    "name": "AAA Quincy Branch Office, 650 Adams Street Quincy, MA 02169 (617) 472-4900",
    "geo": "42.25560000000001, -71.03251"
  },
  {
    "id": "3755209",
    "name": "AAA Raynham Branch Office, 600 South Street West Raynham, MA 02767 (508) 823-6000",
    "geo": "41.9042161, -71.0448715"
  },
  {
    "id": "3755215",
    "name": "AAA Rockland Branch Office, 900 Hingham Street Rockland, MA 02370 (781) 871-5880",
    "geo": "42.1604728, -70.9028649"
  },
  {
    "id": "3716284",
    "name": "AAA Saugus Branch Office, 214 Broadway Saugus, MA 01906 (781) 231-3000",
    "geo": "42.4871953, -71.0160981"
  },
  {
    "id": "3720214",
    "name": "AAA Somerset Branch Office, 869 Grand Army of the Republic Highway, Somerset, MA 02725 (508) 672-2600",
    "geo": "41.72996759999999, -71.1718551"
  },
  {
    "id": "3696961",
    "name": "AAA South Attleboro Branch Office, 405 Washington Street South Attleboro, MA 02703 (508) 399-9000",
    "geo": "41.9178198, -71.3596716"
  },
  {
    "id": "3755301",
    "name": "AAA South Dennis Branch Office, 500 Route 134, South Dennis, MA 02660-3426 (508) 760-4778",
    "geo": "41.6944287, -70.1502521"
  },
  {
    "id": "5361913",
    "name": "AAA Springfield Branch Office, 1891 Wilbraham Road, Springfield, MA 01129 (413) 785-1381",
    "geo": "42.11456949999999, -72.4980102"
  },
  {
    "id": "3755311",
    "name": "AAA Tewksbury Branch Office, 345 Main Street Tewksbury, MA 01876 (978) 946-0432",
    "geo": "42.6230203, -71.2661541"
  },
  {
    "id": "3755315",
    "name": "AAA Waltham Branch Office, 856 Lexington Street Waltham, MA 02452 (781) 899-9000",
    "geo": "42.404766, -71.2343985"
  },
  {
    "id": "3755318",
    "name": "AAA Webster Branch Office, 400 South Main Street Webster, MA 01570 (508) 943-0058",
    "geo": "42.0501803, -71.8798332"
  },
  {
    "id": "7244441",
    "name": "AAA West Springfield Branch Office, 150 Capital Drive, West Springfield, MA 01089 (413) 785-1381",
    "geo": "42.13674, -72.61856999999999"
  },
  {
    "id": "3720293",
    "name": "AAA Westwood Branch Office, 335 Providence Highway Westwood, MA 02090 (781) 461-6800",
    "geo": "42.2165, -71.18224"
  },
  {
    "id": "3755326",
    "name": "AAA Worcester Branch Office, 25 Mountain Street East Worcester, MA 01606 (508) 853-7000",
    "geo": "42.3232958, -71.7906144"
  }
]
google_map_api_key = os.environ.get('GOOGLE_API_KEY')
sender_email=os.environ.get('NOTIFICATION_SENDER_EMAIL')
sender_email_pass = os.environ.get('NOTIFICATION_SENDER_EMAIL_PASSWORD')
sms_token=os.environ.get('SMS_TOKEN')

def get_geo_value(address):
    params = {
        'address': address,
        'key': 'AIzaSyD9Ar8hdQG5jrXX_Nn77lVFx9amMZYn3po'
    }

    response = requests.get('https://maps.googleapis.com/maps/api/geocode/json', params=params)
    json_data = response.json()

    # Get the latitude and longitude from the response
    location = json_data['results'][0]['geometry']['location']
    return f"{location['lat']}, {location['lng']}"

def get_drive_time(origin, destination):
    url = f'https://maps.googleapis.com/maps/api/directions/json?origin={origin}&destination={destination}&key={google_map_api_key}&mode=driving'

    response = requests.get(url)
    json_data = response.json()

    # Get the duration in seconds from the response
    duration = json_data['routes'][0]['legs'][0]['duration']['value']

    # Convert seconds to hours and minutes
    mins, remainder = divmod(duration, 60)
    return mins

def get_the_earliest_appointment(calendar):
    url = "https://app.acuityscheduling.com/schedule.php?action=showCalendar&fulldate=1&owner=16564485&template=weekly"

    payload = f"type=13578181&calendar={calendar}&skip=true&options%5Bqty%5D=1&options%5BnumDays%5D=5&ignoreAppointment=&appointmentType=13578181"
    headers = {
        "accept-language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
        "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Cookie": "PHPSESSID=ofs931akk5q6as056255l4ehv5",
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    # Parse the HTML content of the webpage using BeautifulSoup
    soup = BeautifulSoup(response.content, "html.parser")

    # Find the HTML element that contains the available appointment dates
    dates_container = soup.find_all("input", type="radio")

    # Extract the available appointment dates from the container
    available_dates = [date.get("value") for date in dates_container]

    if len(available_dates) > 0:
        return available_dates[0]
    else:
        return ""

def get_all_ma_rmv(my_address, top, accepted_drive_mins=100000):
    all_available_rmv = []
    for rmv_info in ma_aaa_rmv:
        available_time = get_the_earliest_appointment(rmv_info["id"])
        if available_time != "" and (datetime.strptime(available_time, '%Y-%m-%d %H:%M') - datetime.today()).days < 5:
            drive_time =  get_drive_time(get_geo_value(my_address), rmv_info["geo"])
            if accepted_drive_mins > drive_time:
                rmv_info["dis"] = drive_time
                rmv_info["time"] = available_time
                all_available_rmv.append(rmv_info)
    return sorted(all_available_rmv, key=lambda x: x['dis'])[:top]

def send_email(subject, body, to, cc=None, bcc=None, attachments=None):
    # Set up the email message
    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['To'] = to
    if cc:
        msg['Cc'] = cc
    if bcc:
        msg['Bcc'] = bcc
    msg.attach(MIMEText(body))

    # Attach any files to the email
    if attachments:
        for attachment in attachments:
            with open(attachment, 'rb') as f:
                part = MIMEApplication(f.read(), Name=attachment)
                part['Content-Disposition'] = f'attachment; filename="{attachment}"'
                msg.attach(part)

    # Connect to the Outlook server and send the email
    with smtplib.SMTP('smtp.office365.com', 587) as server:
        server.starttls()
        server.login(sender_email, sender_email_pass)
        server.sendmail(sender_email, [to], msg.as_string())

def sendSMSNotification(content, receivers):
    url = "https://api.d7networks.com/messages/v1/send"
    payload = json.dumps(
        {
            "messages": [
                {
                    "channel": "sms",
                    "recipients": receivers,
                    "content": content,
                    "msg_type": "text",
                    "data_coding": "text",
                }
            ],
            "message_globals": {
                "originator": "SignOTP",
                "report_url": "https://the_url_to_recieve_delivery_report.com",
            },
        }
    )
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer {sms_token}",
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    return response

def main():
  print("***********************Fetching AAA RMV appointment**********************\n")
  # available_rmv_list = get_all_ma_rmv("330 pleasant st watertown 02472 ma", 3, 50)
  # message_content = ""
  # index = 0;
  # for rmv in available_rmv_list:
  #   index += 1
  #   name = rmv["name"]
  #   available_time = rmv["time"]
  #   drive_mins = rmv["dis"]
  #   message_content += f"{index}.RMV name: {name}, Available Time: {available_time}, Drive Mins: {drive_mins} mins \n"
  #   print("Summary:")
  
  # print(f"Message Content:\n {message_content}\n")
  # print("************************Sending appointment result************************\n")
  
  # if sender_email_pass and sender_email:
  #   send_email("AAA reservation notification", message_content, "jinhuwang1127@gmail.com")
  # if sms_token:
  #   sendSMSNotification(f"AAA reservation notification \n {message_content}", ["+18484666289"])
  if sender_email_pass and sender_email:
    print(sender_email)
  if sms_token:
    print("true")

  print("*****************************Done******************************************\n")

if __name__ == "__main__":
    main()