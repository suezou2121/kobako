# coding: utf-8

import re, pprint #pp関数用（O'REILLY社 入門自然言語処理 p.469）　まだまともに使っていない

def pp(obj):
    pp = pprint.PrettyPrinter(indent=4, width=160)
    str = pp.pformat(obj)
    return re.sub(r"\\u([0-9a-f]{4})", lambda x: unichr(int("0x"+x.group(1), 16)), str)

data =  {
    u"スクリプト言語":
      {u"Perl": u"パール",
       u"Python": u"パイソン"},
    u"関数型言語":
      {u"Erlang": u"アーラング",
       u"Haskell": u"ハスケル"}
    }

if __name__ == "__main__":
    print data
    print pp(data)
