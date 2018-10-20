# SCRIPTS

## speak.py

## pepibot.py

Este script usa el bot de Telegram [@misspepi_bot](http://telegram.me/misspepi_bot) para quedar a la escucha y reproducir con *speak.py* el mensaje que le envíen los usuarios autorizados

En necesario tener el siguiente fichero json en el mismo directorio donde se encuentre pepibot.py con el token del bot de Telegram y la lista de usuarios autorizados. El formato es el siguiente:

```json
{
  "token": "XXXXXXXXXXXXXXXXXXXXXXXXXXX",
  "authorized_ids": [
    1111111,
    2222222,
    3333333,
    4444444,
    5555555,
    6666666
  ]
}
```

El script lee cada 5 minutos este json para comprobar si se ha actualizado la lista de usuarios autorizados sin necesidad de reiniciar el script