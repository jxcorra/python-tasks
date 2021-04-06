import doctest
import re
import typing
import urllib.parse
from datetime import datetime


IP_RE = r'(?:\d{1,3}\.?){4}'
DATE_RE = r'.+?'
URL_RE = r'[^"]+'
STATUS_RE = r'\d+'
SIZE_RE = r'\d+'
UA_RE = r'[^"]+'
GET_REQUEST_RE = (rf'(?P<ip>{IP_RE})'
                  rf'(?:\s\-\s?){{2}}'
                  rf'\[(?P<date>{DATE_RE})\]'
                  rf'\s"(?P<url>{URL_RE})"'
                  rf'\s(?P<status>{STATUS_RE})'
                  rf'\s(?P<size>{SIZE_RE})'
                  rf'\s".*?"'
                  rf'\s"(?P<ua>{UA_RE})"')
REQUEST_INFO_KEY_MAPPER = {
    'ip': None,
    'date': lambda date_str: datetime.strptime(date_str, '%d/%b/%Y:%H:%M:%S %z'),
    'url': lambda url: urllib.parse.unquote(url),
    'status': lambda status_str: int(status_str),
    'size': lambda size_str: int(size_str),
    'ua': None,
}


Request = typing.NewType('Request', typing.Dict[str, typing.Union[str, int]])


def get_requests(from_log: str) -> typing.List[Request]:
    """
    Parses every `GET` request line of nginx log and returns list of `Request`
    >>> get_requests('66.249.65.159 - - [06/Nov/2014:19:10:38 +0600] "GET /news/53f8d72920ba2744fe873ebc.html HTTP/1.1" 404 177 "-" "Mozilla/5.0 (iPhone; CPU iPhone OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5376e Safari/8536.25 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"')
    [{'ip': '66.249.65.159', 'date': datetime.datetime(2014, 11, 6, 19, 10, 38, tzinfo=datetime.timezone(datetime.timedelta(seconds=21600))), 'url': 'GET /news/53f8d72920ba2744fe873ebc.html HTTP/1.1', 'status': 404, 'size': 177, 'ua': 'Mozilla/5.0 (iPhone; CPU iPhone OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5376e Safari/8536.25 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'}]
    >>> get_requests('')
    []
    >>> get_requests('some other line')
    []
    """
    result = []
    for line in from_log.split('\n'):
        if match := re.search(GET_REQUEST_RE, line.strip()):
            result.append(parse_get(match))

    return result


def parse_get(request_match: re.Match) -> Request:
    result = {}

    for key, mapper in REQUEST_INFO_KEY_MAPPER.items():
        if group := request_match.group(key):
            result[key] = mapper(group) if mapper else group

    return result


if __name__ == '__main__':
    doctest.testmod()
