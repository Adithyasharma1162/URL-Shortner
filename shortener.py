import pyshorteners

def shorten_url(url):
    s = pyshorteners.Shortener()
    short_url = s.tinyurl.short(url)
    return short_url

# Example usage
if __name__ == '__main__':
    long_url = 'https://www.example.com'
    print('Shortened URL:', shorten_url(long_url))