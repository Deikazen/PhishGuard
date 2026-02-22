from urllib.parse import urlparse
import pandas as pd

def get_features(url):
    features = {}

    # Konversi ke string jaga-jaga kalau ada data bukan string
    url = str(url)

    if not url.startswith(('http://', 'https://')):
        parse_url = "http://" + url
    else:
        parse_url = url
    
    try:
        parsed = urlparse(parse_url)
        hostname = parsed.netloc
        path = parsed.path
    except ValueError:
        temp_url = parse_url.replace("http://", "").replace("https://", "")
        
        if "/" in temp_url:
            parts = temp_url.split('/', 1)
            hostname = parts[0]
            path = "/" + parts[1]
        else:
            hostname = temp_url
            path = ""

    # A. Fitur Panjang
    features['url_length'] = len(url)
    features['hostname_length'] = len(hostname)
    features['path_length'] = len(path)

    # B. Fitur Karakter Spesial
    features['count_dot'] = url.count('.')
    features['count_hyphen'] = url.count('-')
    features['count_at'] = url.count('@')
    features['count_question'] = url.count('?')
    features['count_percent'] = url.count('%')
    features['count_www'] = url.count('www')

    # C. Fitur Pola 
    features['count_digits'] = sum(c.isdigit() for c in url)
    features['count_letters'] = sum(c.isalpha() for c in url)

    return list(features.values())