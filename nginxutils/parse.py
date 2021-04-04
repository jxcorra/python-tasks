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


def get_requests(from_log: str) -> typing.List[str]:
    result = []
    for line in from_log.split('\n'):
        if match := re.search(GET_REQUEST_RE, line.strip()):
            result.append(parse_get(match))

    return result


def parse_get(request_match: re.Match) -> typing.Dict[str, typing.Union[str, int]]:
    result = {}

    for key, mapper in REQUEST_INFO_KEY_MAPPER.items():
        if group := request_match.group(key):
            result[key] = mapper(group) if mapper else group

    return result
