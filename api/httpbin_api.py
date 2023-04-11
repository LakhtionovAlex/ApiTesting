from api.client import Client


class HttpBinApi(Client):
    HTML = '/html'
    BASE_URL = "https://httpbin.org"
    TIME = '/delay'

    def list_html(self):
        """
        :method:    get
        :rout:      /html
        :status:    200
        """
        url = self.BASE_URL + self.HTML
        return self.get(url)

    def robots(self):
        """
        :method:    get
        :rout:      /robots.txt
        :status:    200
        """
        url = self.BASE_URL + '/robots.txt'
        return self.get(url)

    def ip(self):
        """
        :method:    get
        :rout:      /ip
        :status:    200
        """
        url = self.BASE_URL + '/ip'
        return self.get(url)

    def time_out(self, delay=1):
        """
        :method:    get
        :rout:      /ip
        :status:    200
        """
        url = self.BASE_URL + self.TIME + f'/3'
        try:
            return self.get(url, timeout=delay)
        except Exception as ex:
            return False, ex


http_bin_api = HttpBinApi()
