def parse(query: str) -> dict:
    if '?' not in query:
        return {}
    else:
        return {kv.split("=")[0]: kv.split("=")[1] for kv in query.split('?')[1].split('&') if kv}


if __name__ == '__main__':
    assert parse('https://example.com/path/to/page?name=ferret&color=purple') == {'name': 'ferret', 'color': 'purple'}
    assert parse('https://example.com/path/to/page?name=ferret&color=purple&') == {'name': 'ferret', 'color': 'purple'}
    assert parse('http://example.com/') == {}
    assert parse('http://example.com/?') == {}
    assert parse('http://example.com/?name=Dima') == {'name': 'Dima'}
    assert parse('http://example.com/?color=red') == {'color': 'red'}


def parse_cookie(query: str) -> dict:
    result =  {_.split('=')[0]: "=".join(_.split("=")[1:]) for _ in query.split(';') if _}
    return result


if __name__ == '__main__':
    assert parse_cookie('name=Dima;') == {'name': 'Dima'}
    assert parse_cookie('') == {}
    assert parse_cookie('name=Dima;age=28;') == {'name': 'Dima', 'age': '28'}
    assert parse_cookie('name=Dima=User;age=28;') == {'name': 'Dima=User', 'age': '28'}
    assert parse_cookie('name=Dima=User;age=28;job=dev') == {'name': 'Dima=User', 'age': '28', 'job': 'dev'}
