# postfix-python-policy-service
This is just an example policy service, written in python, to create a custom policy service for [Postfix SMTP Access Policy Delegation](http://www.postfix.org/SMTPD_POLICY_README.html)

## Example Postfix integration
### Installation
```
git clone https://github.com/mat1010/postfix-python-policy-service.git /opt/postfix-python-policy-service
```
### Test the script itself is working
```
echo sender=foo@bar.de | /opt/postfix-python-policy-service/policy.py && cat /tmp/python-policy-service.log

action=dunno

XX:XX:XX,XXX DEBUG Sender address: foo@bar.de
XX:XX:XX,XXX DEBUG {'sender': 'foo@bar.de'}

```

### Postfix Configuration
#### master.cf
##### as unix socket
```
/etc/postfix/master.cf:
  ...
  policy  unix  -       n       n       -       0       spawn
    user=nobody argv=/opt/postfix-python-policy-service/policy.py
  ...
```
##### as tcp listener
```
 /etc/postfix/master.cf:
   127.0.0.1:9998  inet  n       n       n       -       0       spawn
     user=nobody argv=/opt/postfix-python-policy-service/policy.py
```
#### main.cf
##### as unix socket
```
/etc/postfix/main.cf:
  smtpd_recipient_restrictions =
      ...
      reject_unauth_destination
      check_policy_service unix:private/policy
      ...
```
##### as tcp listener
```
 /etc/postfix/main.cf:
   smtpd_recipient_restrictions =
       ...
       reject_unauth_destination
       check_policy_service inet:127.0.0.1:9998
       ...
```
