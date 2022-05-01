import requests
import json

def track_ratio_event(ratio=0):
    url = "https://www.google-analytics.com/mp/collect?measurement_id=G-3WSTG39V1Z&api_secret=fHTjoqSCS267AkW0J16PjA"
    payload = {
      "client_id": "734782877.1644692550",
      "user_id":"QDCAgEABAAAAAE~",
      "non_personalized_ads": False,
      "events": [
        {
          "name": "yk_projector_btc_usd_ratio",
          "params": {
            "ratio": ratio
          }
        }
      ]
    }
    r = requests.post(url,data=json.dumps(payload),verify=True)


def get_usd_btc_ratio():
    url = 'https://blockchain.info/ticker?base=BTC'
    r = requests.get(url,verify=True)
    ratios = json.loads(r.text)

    return ratios['USD']['15m']


if __name__ == "__main__":
    ratio = get_usd_btc_ratio()
    track_ratio_event(ratio=ratio)
