# Websphere xor password

WebSphere Application Server - encrypt|decrypt {XOR} password.

# Usage

## Encrypt

```bash
./xor_password.py -e PASSWORD
```

Example:
```bash
./xor_password.py -e 12345678
> Encode mode
> Encoded password: {XOR}bm1sa2ppaGc=
```

## Decrypt

```bash
./xor_password.py -d ENCRYPTED_PASSWORD
```

Example:
```bash
./xor_password.py -d {XOR}bm1sa2ppaGc=
> Decode mode
> Decoded password: 12345678
```