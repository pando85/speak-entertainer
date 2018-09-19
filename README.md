# SCRIPTS

## speak.py

## pepibot.py

Este script usa el bot de Telegram [@misspepi_bot](http://telegram.me/misspepi_bot) para quedar a la escucha y reproducir con *speak.py* el mensaje que le envíen los usuarios autorizados

Se parsea el fichero *pepibot.yml* para obtener el token del bot de Telegram y los ids de los usuarios. Tiene el siguiente aspecto:

```yaml
---

token: "AAAAAAAAAAAAAA"
authorized_keys:
  - 11111
  - 22222
  - 33333
  - 44444
  - 55555
```