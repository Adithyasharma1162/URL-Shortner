def shorten_url(url):
    shortened = url.split('://')[-1][:8]  # Simplified shortening logic
    return f'{shortened}...'

# Example usage
if __name__ == '__main__':
    print(shorten_url('https://www.example.com/some/long/path'))