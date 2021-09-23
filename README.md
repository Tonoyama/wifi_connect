# wifi_connect

https://hackmd.io/HmfdeiPgRNyhNUzkS_HRqg?view#WiFi%E3%81%AE%E8%87%AA%E5%8B%95%E6%8E%A5%E7%B6%9A%E3%81%AE%E8%A8%AD%E5%AE%9A


```
crontab -e
```

1分毎に接続があるか確認。なければ接続。

```
*/1 * * * * sudo /usr/bin/sh /home/pi/wifi_connect/wifi.sh
```

確認。

```
crontab -l
```