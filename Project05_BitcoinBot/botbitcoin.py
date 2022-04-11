import json
import ssl

import websocket
import bitstamp.client

import credenciais


def cliente():
    return bitstamp.client.Trading(
        username=credenciais.USERNAME,
        key=credenciais.KEY,
        secret=credenciais.SECRET_KEY
    )


def comprar(qtd):
    trading_client = cliente()
    trading_client.buy_market_order(qtd)


def vender(qtd):
    trading_client = cliente()
    trading_client.sell_market_order(qtd)


def ao_abrir(ws):
    print("Abriu a conexão...")

    json_subscribe = """"{
        "event": "bts:subscribe",
        "data": {
            "channel": "live_trades_btcusd"
        }
    }"""

    ws.send(json_subscribe)


def ao_fechar(ws):
    print("Fechou a conexão...")


def ao_erro(ws, erro):
    print("Erro inesperado...")
    print(erro)


def ao_receber_mensagem(ws, mensagem):
    mensagem = json.loads(mensagem)
    price = mensagem['data']['price']
    print(price)

    if price > 90000:
        vender()
    elif price < 80000:
        comprar()
    else:
        print("Aguardando...")


if __name__ == "__main__":
    ws = websocket.WebSocketApp("wss://ws.bitstamp.net",
                                on_open=ao_abrir,
                                on_close=ao_fechar,
                                on_error=ao_erro,
                                on_message=ao_receber_mensagem
                                )

    ws.run_forever(sslopt={"cert_regs": ssl.CERT_NONE})
