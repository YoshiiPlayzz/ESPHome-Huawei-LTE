## Login
Um sich anmelden zu können müssen folgende Sachen implementiert werden:
- [ ] Login Daten verschlüsseln wie [hier](https://github.com/Salamek/huawei-lte-api/blob/8d0d1a8069595e8b64c50a9ccf0137a82b48ca91/huawei_lte_api/api/User.py#L56) (SHA256 oder Base64)
- [ ] Login Prozess über post ("/user/login")
- [ ] Holen der Session Tokens aus dem Header 