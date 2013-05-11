

# coding: utf-8

import urllib #URLを扱うため

import sys #sys.stdin.encoding などを扱うため

import json #JSONを扱うため

from xml.dom import minidom #minidom、XML解析用

#from pp import pp #pp関数用（O'REILLY社 入門自然言語処理 p.469）

#import Skype4Py



weather_xml_url = u"http://weather.livedoor.com/forecast/rss/primary_area.xml"

weather_json_url = u"http://weather.livedoor.com/forecast/webservice/json/v1?city=130010"





def isWeatherCity(city_name):

    xdoc = minidom.parse(urllib.urlopen(weather_xml_url))

    elements = xdoc.getElementsByTagName("city") #cityタグ要素の配列



    # elements の中を全部 for ループでまわして、cityのidを調べる

    for element in elements:

        # title 属性が city と同じとき

        if element.getAttribute("title") == city_name:

            city_id = element.getAttribute("id") #cityID にid属性を代入

            print u"__Debug... city_id = " + city_id

            return True

    return False





def isCityID(city_name):

    city_id = None

    xdoc = minidom.parse(urllib.urlopen(weather_xml_url))

    elements = xdoc.getElementsByTagName("city") #cityタグ要素の配列



    # elements の中を全部 for ループでまわして、cityのidを調べる

    for element in elements:

        # title 属性が city と同じとき

        if element.getAttribute("title") == city_name:

            city_id = element.getAttribute("id") #cityID にid属性を代入

            print u"__Debug... city_id = " + city_id

            return city_id

    return None





def WeatherReport(msg):
    #city_name = msg.Body
    city_name = msg
    city_id = None

    xdoc = minidom.parse(urllib.urlopen(weather_xml_url))

    elements = xdoc.getElementsByTagName("city") #cityタグ要素の配列



    #検索したい地域名を input



    # elements の中を全部 for ループでまわして、cityのidを調べる

    for element in elements:

        # title 属性が city と同じとき

        if element.getAttribute("title") == city_name:

            city_id = element.getAttribute("id") #cityID にid属性を代入

            print u"__Debug... city_id = " + city_id



    # city_id が分かったとき、JSONのULRを完成させる

    if not city_id is None:

        weather_json_url = u"http://weather.livedoor.com/forecast/webservice/json/v1?city="+city_id

        print u"__Debug... weather_json_url = " + weather_json_url

    else:
	#msg.Chat.SendMessage(u"地名が分かりませんでした。")

        print u"kobako: 地名が分かりませんでした。"

        return



    # URLからJSONファイルをロードして辞書を作る

    json_file = urllib.urlopen(weather_json_url)

    jdoc = json.load(json_file)



    #pinpointLocations の地名を表示

    for location in jdoc["pinpointLocations"]:

        print u"__Debug... " + location["name"]



    #title を表示
    #msg.Chat.SendMessage(jdoc["title"] + u"をお知らせします。")

    print u"kobako: " + jdoc["title"] + u"をお知らせします。"

    

    #forecasts を表示

    for forecast in jdoc["forecasts"]:

        #天気を表示
	#msg.Chat.SendMessage(forecast["dateLabel"] + "(" + forecast["date"]+ u") の天気は " + forecast["telop"] + u" です。")

        print u"kobako: " + forecast["dateLabel"] + "(" + forecast["date"]+ u") の天気は " + forecast["telop"] + u" です。"

        #気温を表示

        try:

		#msg.Chat.SendMessage(forecast["dateLabel"] + "(" + forecast["date"]+ u") の最高気温は " + forecast["temperature"]["max"]["celsius"] + u"℃ です。最低気温は " + forecast["temperature"]["min"]["celsius"] + u"℃ です。")            
		print u"kobako: " + forecast["dateLabel"] + "(" + forecast["date"]+ u") の最高気温は " + forecast["temperature"]["max"]["celsius"] + u"℃ です。最低気温は " + forecast["temperature"]["min"]["celsius"] + u"℃ です。"

        except:

            #気温が未発表のときは TypeError: 'NoneType' object has no attribute '__getitem__'　でエラーになる。
            #msg.Chat.SendMessage(forecast["dateLabel"] + "(" + forecast["date"]+ u") の気温は、まだ発表されていません。")

            print u"kobako: " + forecast["dateLabel"] + "(" + forecast["date"]+ u") の気温は、まだ発表されていません。"



    #お天気情報テキストを表示
    #msg.Chat.SendMessage(jdoc["description"]["text"] + "\n" + " (" + jdoc["description"]["publicTime"] + ")")

    print u"kobako: \n" + jdoc["description"]["text"]

    print u" (" + jdoc["description"]["publicTime"] + ")"



data =  {

    u"スクリプト言語":

      {u"Perl": u"パール",

       u"Python": u"パイソン"},

    u"関数型言語":

      {u"Erlang": u"アーラング",

       u"Haskell": u"ハスケル"}

    }



if __name__ == "__main__":

    input_city_name = raw_input(u"地名を入力してください: ").decode(sys.stdin.encoding)

    WeatherReport(input_city_name)



    
